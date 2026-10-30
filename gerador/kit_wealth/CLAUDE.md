# Kit AUVP Wealth

Esta pasta é o kit de documentos da AUVP Wealth. Todo documento da Wealth feito aqui
(proposta, snapshot, estudo, relatório, apresentação) sai no padrão da marca, a partir
dos modelos desta pasta. O objetivo é que dois documentos feitos por pessoas diferentes
pareçam do mesmo lugar.

Responda sempre em português do Brasil.

## Antes de tudo

1. Leia `MARCA.md` inteiro. É a regra.
2. Para montar um documento, siga a skill `documento-wealth`
   (`.claude/skills/documento-wealth/SKILL.md`).

## O que há aqui

| Pasta | O que é |
| --- | --- |
| `modelos/private/`, `modelos/verde/` | os modelos nas duas identidades. **Nunca se editam**: copiam-se |
| `modelos/*/componentes-*.html` | o catálogo de componentes, de onde se copia marcação |
| `referencia/` | o PDF de cada modelo: é assim que o resultado tem que ficar |
| `marca/` | logos, grafismos e fontes, para uso fora dos documentos |
| `ferramentas/pdf.mjs` | confere o documento e gera o PDF |
| `documentos/` | onde ficam os documentos dos clientes, uma pasta por cliente |

## Regras que não se quebram

- **Todo documento parte de um modelo.** Copie o modelo para
  `documentos/<cliente>/<documento>.html` e edite a cópia. Não se escreve documento do
  zero, não se gera HTML novo com outro desenho, não se usa outra ferramenta (Word,
  Gamma, Canva) para o documento final.
- **Uma identidade por documento**: `private` para cliente do Private Banking, `verde`
  para cliente da consultoria ou de fora da casa. Se não souber qual, pergunte.
- **Não se mexe no `<style>`** nem se cria classe, cor ou fonte nova. Página nova se faz
  com uma `<section>` copiada do mesmo documento e os componentes do catálogo.
- **Conteúdo que não cabe ganha outra página.** Nunca reduza fonte, espaço ou margem.
- **O disclaimer legal entra sempre e como está.** Não se edita, não se resume.
- **Texto da casa** (quem somos, método, escopo, entregáveis) não se reescreve sem pedido
  expresso de quem pediu o documento.
- **Nenhum dado é inventado.** Valor, nome, data, percentual: o que não veio no material
  do cliente fica como campo pendente e é listado no fim, nunca preenchido com um
  exemplo. A skill diz onde fica o limite entre fazer uma conta e inventar.
- **Arquivos de trabalho** (scripts, rascunhos, fotos de conferência) ficam fora de
  `documentos/` e são apagados no fim. Em `documentos/<cliente>/` ficam só o HTML, o PDF
  e a pasta `imagens/`, se houver.
- **Todo documento termina exportado e conferido** com `node ferramentas/pdf.mjs`, sem
  nenhum erro de estouro.

## Preenchendo campos

Os campos aparecem no HTML assim:

```html
<span class="ph" data-campo="nome_cliente" title="Ex.: Maria e João Silva">{{nome_cliente}}</span>
```

Troque o `<span>` inteiro pelo texto: `Maria e João Silva`. O `title` é a dica do que vai
ali.

Campos com a classe `ph pronto` já trazem um texto padrão. Mantenha-o, ou ajuste-o ao
caso, e tire o `<span>` em volta do mesmo jeito.

Uma linha de capa ou de lista que não se aplica ao caso sai inteira, com a tag que a
envolve. Não fica vazia nem com o campo à mostra.
