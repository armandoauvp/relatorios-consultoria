/**
 * O relatório macroeconômico a partir de um rascunho, sem abrir a ferramenta.
 *
 *   npm run macro -- macro/2026-08/rascunho.json               # os quatro segmentos
 *   npm run macro -- macro/2026-08/rascunho.json --segmentos=private,consultoria
 *   npm run macro -- --modelo                                  # rascunho vazio e lista de campos
 *
 * O rascunho é o mesmo JSON que a ferramenta baixa em "Rascunho > Baixar": os
 * valores de cada campo, as linhas acrescentadas ou tiradas das tabelas e as
 * páginas tiradas. Quem o escreve, todo mês, é o Claude, a partir do conteúdo
 * que o time fecha (veja macro/README.md).
 *
 * O documento não é montado aqui. O script abre a própria ferramenta num
 * navegador sem janela, carrega o rascunho e chama as mesmas funções do botão
 * "Exportar": preencher, tirar o que ficou em branco, escolher os textos,
 * repartir as páginas, refazer o sumário. O PDF que sai daqui é igual ao que
 * sairia da ferramenta, porque é a ferramenta que o faz.
 *
 * Saem, ao lado do rascunho, o HTML e o PDF de cada segmento, e no terminal a
 * lista do que ficou em branco e dos campos do rascunho que o modelo não tem.
 */
import { createServer } from 'node:http';
import { readFileSync, writeFileSync, existsSync, mkdirSync, statSync } from 'node:fs';
import { dirname, extname, join, resolve, basename } from 'node:path';
import { fileURLToPath } from 'node:url';
import { chromium } from 'playwright';

const raiz = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const DOCS = join(raiz, 'docs');
const DOCUMENTO = 'relatorio-macroeconomico';
const SEGMENTOS = ['consultoria', 'alta-renda', 'private', 'assessoria'];

const args = process.argv.slice(2);
const opcao = (nome) => args.find((a) => a.startsWith(`--${nome}=`))?.slice(nome.length + 3);
const posicionais = args.filter((a) => !a.startsWith('--'));

/* -------------------------------------------------- o rascunho vazio e o guia */

/** O rascunho vazio e a lista de campos, tirados do catálogo da ferramenta. Os
 *  campos são os mesmos nos quatro segmentos; o de referência é o do Private. */
function modelo(saida) {
  const est = JSON.parse(readFileSync(join(DOCS, 'campos', `${DOCUMENTO}-private.json`), 'utf8'));
  const valores = {};
  const linhas = ['# Campos do relatório macroeconômico', '',
    'Gerado por `npm run macro -- --modelo` a partir do modelo. Não edite à mão.', '',
    'Um campo deixado vazio ("") sai do documento. Texto longo com uma linha em branco',
    'no meio vira dois parágrafos.', ''];
  for (const g of est.grupos) {
    const nomes = g.campos.filter((n) => !(n in valores));
    if (!nomes.length) continue;
    linhas.push(`## Página ${String(g.pagina).padStart(2, '0')}: ${g.secao}`, '',
      '| Campo | O que vai | Padrão |', '| --- | --- | --- |');
    for (const n of nomes) {
      const c = est.campos[n] || {};
      valores[n] = c.padrao || '';
      const oque = (c.dica || c.rotulo || n).replace(/\|/g, '/');
      linhas.push(`| \`${n}\` | ${oque}${c.tipo === 'longo' ? ' (texto longo)' : ''} | ${c.padrao || ''} |`);
    }
    linhas.push('');
  }
  linhas.push('## Tabelas que crescem', '',
    'As tabelas de linhas numeradas aceitam mais linhas: basta escrever os campos da linha',
    'nova (por exemplo `pos_5_posicao`, `pos_5_racional`) e declarar o número em `linhas`,',
    'com a chave do primeiro campo da tabela:', '',
    '```json', '"linhas": { "pos_1_posicao": { "fora": [], "extra": [5, 6] } }', '```', '');
  for (const t of est.tabelas || []) {
    const primeiro = t.linhas.flat().find((c) => c.c)?.c;
    if (primeiro && /^[a-z0-9]+_\d+_/.test(primeiro)) linhas.push(`- \`${primeiro}\``);
  }
  mkdirSync(saida, { recursive: true });
  writeFileSync(join(saida, 'rascunho-modelo.json'), JSON.stringify(
    { documento: DOCUMENTO, valores, linhas: {}, fora: [] }, null, 1) + '\n');
  writeFileSync(join(saida, 'CAMPOS.md'), linhas.join('\n') + '\n');
  console.log(`${saida}/rascunho-modelo.json e ${saida}/CAMPOS.md: ${Object.keys(valores).length} campos`);
}

/* ------------------------------------------------------- o servidor da ferramenta */

const TIPOS = { '.html': 'text/html', '.js': 'text/javascript', '.css': 'text/css',
  '.json': 'application/json', '.svg': 'image/svg+xml', '.png': 'image/png', '.woff2': 'font/woff2' };

function servir() {
  const srv = createServer((req, res) => {
    const caminho = join(DOCS, decodeURIComponent(new URL(req.url, 'http://x').pathname));
    const arquivo = existsSync(caminho) && statSync(caminho).isDirectory() ? join(caminho, 'index.html') : caminho;
    if (!arquivo.startsWith(DOCS) || !existsSync(arquivo)) { res.writeHead(404); res.end(); return; }
    res.writeHead(200, { 'content-type': TIPOS[extname(arquivo)] || 'application/octet-stream' });
    res.end(readFileSync(arquivo));
  });
  return new Promise((ok) => srv.listen(0, '127.0.0.1', () => ok(srv)));
}

/* ------------------------------------------------------------------- a geração */

async function gerar(arquivo) {
  const rascunho = JSON.parse(readFileSync(arquivo, 'utf8'));
  if (rascunho.documento && rascunho.documento !== DOCUMENTO) {
    console.error(`O rascunho é de "${rascunho.documento}", não do relatório macroeconômico.`);
    process.exit(1);
  }
  const segmentos = (opcao('segmentos') || SEGMENTOS.join(',')).split(',').map((s) => s.trim());
  const saida = resolve(opcao('out') || dirname(resolve(arquivo)));
  mkdirSync(saida, { recursive: true });

  const srv = await servir();
  const url = `http://127.0.0.1:${srv.address().port}/`;
  const navegador = await chromium.launch();
  let problemas = 0;
  try {
    for (const seg of segmentos) {
      const pagina = await navegador.newPage();
      await pagina.goto(url);
      await pagina.waitForFunction("typeof estado !== 'undefined' && !!estado.catalogo");
      // Dentro da ferramenta: escolher o documento e o segmento, pôr o
      // rascunho no lugar do que se digitaria, e montar como o botão
      // "Exportar" monta.
      const r = await pagina.evaluate(async ({ seg, doc, rascunho }) => {
        estado.produto = seg;
        estado.documento = estado.catalogo.documentos.find((d) => d.chave === doc);
        const vs = variantesDoProduto(estado.documento, seg);
        const v = vs.find((x) => x.sufixo === seg) || vs[0];
        if (!v) return { erro: `sem variante para ${seg}` };
        await escolherVariante(v);
        estado.valores = { ...(rascunho.valores || {}) };
        estado.linhas = rascunho.linhas || {};
        estado.graficos = rascunho.graficos || {};
        estado.imagens = rascunho.imagens || {};
        estado.fora = new Set(rascunho.fora || []);
        if (Array.isArray(rascunho.paginas)) estado.paginas = rascunho.paginas;
        const html = await montarFinal('exportar');
        const { campos } = estado.estrutura;
        return {
          html,
          faltam: emBranco().map((c) => `pág. ${String(c.pagina).padStart(2, '0')} ${c.secao}: ${c.nome}`),
          // Campo que o modelo não conhece é, quase sempre, nome digitado
          // errado: o texto dele não entraria em lugar nenhum.
          desconhecidos: Object.keys(estado.valores)
            .filter((n) => !campos[n] && !/^[a-z0-9]+_\d+_[a-z0-9_]+$/.test(n)),
        };
      }, { seg, doc: DOCUMENTO, rascunho });
      await pagina.close();
      if (r.erro) { console.error(`${seg}: ${r.erro}`); problemas += 1; continue; }

      const nome = join(saida, `${DOCUMENTO}-${seg}`);
      writeFileSync(`${nome}.html`, r.html);
      const impressao = await navegador.newPage();
      await impressao.setContent(r.html, { waitUntil: 'load' });
      await impressao.emulateMedia({ media: 'print' });
      await impressao.pdf({ path: `${nome}.pdf`, printBackground: true, preferCSSPageSize: true });
      await impressao.close();

      console.log(`\n${basename(nome)}.pdf`);
      if (r.desconhecidos.length) {
        problemas += 1;
        console.log(`  campos que o modelo não tem (conferir o nome): ${r.desconhecidos.join(', ')}`);
      }
      if (r.faltam.length) {
        console.log(`  ${r.faltam.length} campo(s) em branco, que saem do documento:`);
        r.faltam.forEach((f) => console.log(`    ${f}`));
      }
    }
  } finally {
    await navegador.close();
    srv.close();
  }
  process.exit(problemas ? 1 : 0);
}

if (args.includes('--modelo')) modelo(resolve(opcao('out') || join(raiz, 'macro')));
else if (posicionais.length) await gerar(posicionais[0]);
else {
  console.error('Uso: npm run macro -- <rascunho.json> [--segmentos=private,consultoria] [--out=pasta]');
  console.error('     npm run macro -- --modelo');
  process.exit(1);
}
