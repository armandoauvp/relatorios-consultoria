/**
 * Confere e exporta para PDF os documentos da AUVP Wealth.
 *
 *   node ferramentas/pdf.mjs documentos/proposta-silva.html
 *   node ferramentas/pdf.mjs documentos                  # todos os .html da pasta
 *   node ferramentas/pdf.mjs documentos/x.html --conferir   # só confere, sem PDF
 *   node ferramentas/pdf.mjs modelos --saida=referencia --modelo
 *   node ferramentas/pdf.mjs documentos/x.html --fotos     # e um PNG por página
 *
 * `--fotos` grava as páginas em `<documento>-paginas/01.png…`, para conferir o
 * resultado olhando, sem precisar de leitor de PDF.
 *
 * Para cada arquivo:
 *   0. numera as páginas em sequência (a capa não conta);
 *   1. desenha os gráficos que têm `data-valores` (com `ferramentas/graficos.js`);
 *   2. confere, em modo de impressão, se algum conteúdo estoura a página;
 *   3. lista os campos {{…}} que ficaram sem preencher e as molduras vazias;
 *   4. grava o PDF ao lado do HTML (ou em --saida, espelhando as pastas).
 *
 * Estouro de página é erro: o PDF não sai e o script termina com código 1.
 * Campo pendente é aviso: o PDF sai, mas o documento não está pronto.
 * `--modelo` cala os avisos de campo, para exportar os modelos em branco.
 */
import { chromium } from 'playwright';
import { readdirSync, statSync, mkdirSync } from 'node:fs';
import { dirname, join, relative, resolve, basename } from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';

const aqui = dirname(fileURLToPath(import.meta.url));
const args = process.argv.slice(2);
const opcao = (nome) => args.find((a) => a.startsWith(`--${nome}`));
const saidaArg = opcao('saida=');
const saida = saidaArg ? resolve(saidaArg.slice('--saida='.length)) : null;
const soConferir = !!opcao('conferir');
const modelo = !!opcao('modelo');
const fotos = !!opcao('fotos');
const alvos = args.filter((a) => !a.startsWith('--'));

if (!alvos.length) {
  console.log('Uso: node ferramentas/pdf.mjs <arquivo.html | pasta> [--conferir] [--saida=pasta]');
  process.exit(2);
}

/** Os .html de um alvo, com o caminho relativo à raiz dele (para espelhar). */
function arquivos(alvo) {
  const cheio = resolve(alvo);
  if (!statSync(cheio).isDirectory()) return [{ cheio, rel: basename(cheio) }];
  const achados = [];
  const desce = (dir) => {
    for (const nome of readdirSync(dir).sort()) {
      const c = join(dir, nome);
      if (statSync(c).isDirectory()) desce(c);
      else if (nome.endsWith('.html')) achados.push({ cheio: c, rel: relative(cheio, c) });
    }
  };
  desce(cheio);
  return achados;
}

// O Chromium do Playwright, se instalado; senão o Chrome ou o Edge da máquina,
// para ninguém precisar baixar navegador só para isto.
async function abre() {
  for (const opcoes of [{}, { channel: 'chrome' }, { channel: 'msedge' }]) {
    try { return await chromium.launch(opcoes); } catch { /* tenta o próximo */ }
  }
  console.error('Nenhum navegador encontrado. Rode: npx playwright install chromium');
  process.exit(2);
}

/** Desenha cada `.chart[data-grafico][data-valores]` no lugar da moldura. Duas
 *  passadas: a primeira põe o desenho, a segunda o refaz na proporção da caixa
 *  que ele ocupa na página impressa. */
async function desenhaGraficos(page) {
  await page.addScriptTag({ path: join(aqui, 'graficos.js') });
  const passada = (medir) => page.evaluate((medir) => {
    const erros = [];
    for (const bloco of document.querySelectorAll('.chart[data-grafico][data-valores]')) {
      let linhas;
      try {
        linhas = JSON.parse(bloco.dataset.valores)
          .map((l) => (Array.isArray(l) ? { r: l[0], v: l.slice(1) } : l));
      } catch (e) {
        erros.push(`data-valores inválido (${e.message}): ${bloco.dataset.valores.slice(0, 60)}`);
        continue;
      }
      const series = bloco.dataset.series ? bloco.dataset.series.split('|') : null;
      let caixa;
      if (medir) {
        const r = bloco.getBoundingClientRect();
        let ocupado = 0;
        for (const el of bloco.querySelectorAll('.legend, .g-nota')) ocupado += el.getBoundingClientRect().height;
        caixa = { w: r.width, h: Math.max(60, r.height - ocupado) };
      }
      const html = window.Graficos.desenha(bloco.dataset.grafico, linhas, series, caixa);
      if (!html) { erros.push(`gráfico sem dado válido: ${bloco.dataset.valores.slice(0, 60)}`); continue; }
      bloco.innerHTML = html;
      bloco.classList.add('feito');
    }
    return erros;
  }, medir);
  const erros = await passada(false);
  await page.emulateMedia({ media: 'print' });
  await passada(true);
  return erros;
}

/** O que estoura a página, na mesma regra do `npm run check` da AUVP. */
function estouros() {
  const out = [];
  document.querySelectorAll('.page,.slide').forEach((p, i) => {
    const pg = i + 1;
    const box = p.getBoundingClientRect();
    const grafs = [...p.querySelectorAll('.graf')];
    grafs.forEach((g) => { g.style.display = 'none'; });
    if (p.scrollHeight - p.clientHeight > 1) out.push(`pág ${pg}: altura +${p.scrollHeight - p.clientHeight}px`);
    if (p.scrollWidth - p.clientWidth > 1) out.push(`pág ${pg}: largura +${p.scrollWidth - p.clientWidth}px`);
    const body = p.querySelector('.pg-body');
    if (body && body.scrollHeight - body.clientHeight > 1)
      out.push(`pág ${pg}: conteúdo passa do pé em ${Math.round(body.scrollHeight - body.clientHeight)}px`);
    p.querySelectorAll('table,.kpis,.cards,.steps,.tl,.dl,.flow').forEach((el) => {
      const r = el.getBoundingClientRect();
      if (r.right > box.right + 1) out.push(`pág ${pg}: ${el.className.split(' ')[0] || el.tagName} sai pela direita`);
    });
    p.querySelectorAll('.cols2>*,.cols3>*,.cols2u>*').forEach((cel) => {
      const c = cel.getBoundingClientRect();
      for (const el of cel.querySelectorAll('table,.kpis,.cards,.chart,.imgbox')) {
        if (el.getBoundingClientRect().right > c.right + 1) {
          out.push(`pág ${pg}: ${el.tagName.toLowerCase()} invade a coluna ao lado`);
          break;
        }
      }
    });
    grafs.forEach((g) => { g.style.display = ''; });
  });
  return out;
}

/** O que ainda falta preencher. */
function pendencias() {
  const campos = new Set();
  document.querySelectorAll('.ph:not(.pronto)').forEach((el) => campos.add(el.dataset.campo || el.textContent));
  const soltos = (document.body.innerText.match(/\{\{[^}]+\}\}/g) || []).map((x) => x.slice(2, -2));
  soltos.forEach((x) => campos.add(x));
  const vazios = [];
  document.querySelectorAll('.page,.slide').forEach((p, i) => {
    p.querySelectorAll('[data-exemplo]').forEach(() => {
      vazios.push(`pág ${i + 1}: gráfico ainda com o dado de exemplo do catálogo (tire o data-exemplo ao trocar os valores)`);
    });
    p.querySelectorAll('.chart:not(.feito), .imgbox').forEach((el) => {
      const nome = (el.querySelector('.cl') || {}).textContent || 'moldura';
      vazios.push(`pág ${i + 1}: ${el.classList.contains('chart') ? 'gráfico' : 'imagem'} sem conteúdo (${nome.trim()})`);
    });
  });
  return { campos: [...campos], vazios };
}

const browser = await abre();
const page = await browser.newPage();
let falhas = 0;
let total = 0;

for (const alvo of alvos) {
  for (const { cheio, rel } of arquivos(alvo)) {
    total++;
    await page.emulateMedia({ media: 'screen' });
    await page.goto(pathToFileURL(cheio).href, { waitUntil: 'load' });
    await page.evaluate(() => document.fonts.ready);
    // Página copiada leva o número da original: renumera na ordem do arquivo.
    await page.evaluate(() => document.querySelectorAll('.pg-foot .no').forEach((el, i) => {
      el.textContent = String(i + 1).padStart(2, '0');
    }));
    const errosGrafico = await desenhaGraficos(page);
    const problemas = [...errosGrafico, ...(await page.evaluate(estouros))];
    const { campos, vazios } = await page.evaluate(pendencias);
    const paginas = await page.evaluate(() => document.querySelectorAll('.page,.slide').length);

    console.log(`\n${relative(process.cwd(), cheio)}  (${paginas} páginas)`);
    for (const p of problemas) console.log(`  ERRO  ${p}`);
    if (!modelo) {
      if (campos.length) console.log(`  aviso ${campos.length} campo(s) sem preencher: ${campos.join(', ')}`);
      for (const v of vazios) console.log(`  aviso ${v}`);
    }

    if (problemas.length) {
      falhas++;
      console.log('  PDF não gerado: corrija o estouro (dê outra página ao conteúdo, não reduza a fonte).');
      continue;
    }
    if (soConferir) { console.log('  ok, sem estouro'); continue; }
    const destino = saida ? join(saida, rel.replace(/\.html$/, '.pdf')) : cheio.replace(/\.html$/, '.pdf');
    mkdirSync(dirname(destino), { recursive: true });
    await page.pdf({ path: destino, printBackground: true, preferCSSPageSize: true });
    console.log(`  PDF   ${relative(process.cwd(), destino)}`);
    if (fotos) {
      const pasta = destino.replace(/\.pdf$/, '-paginas');
      mkdirSync(pasta, { recursive: true });
      const els = await page.$$('.page,.slide');
      for (let n = 0; n < els.length; n++) {
        await els[n].screenshot({ path: join(pasta, `${String(n + 1).padStart(2, '0')}.png`) });
      }
      console.log(`  fotos ${relative(process.cwd(), pasta)} (${els.length} PNG)`);
    }
  }
}

await browser.close();
console.log(falhas ? `\n${falhas} de ${total} arquivo(s) com estouro de página.` : `\n${total} arquivo(s) sem estouro.`);
process.exit(falhas ? 1 : 0);
