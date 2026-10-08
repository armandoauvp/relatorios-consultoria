# Relatório macro automatizado

O relatório macroeconômico sai do conteúdo que o time fecha no mês, sem ninguém preencher
campo por campo. São três passos.

## 1. O rascunho

O Claude transforma o conteúdo do mês no rascunho do modelo: um arquivo JSON com o texto de
cada campo.

- **No claude.ai:** abra uma conversa, cole o texto de [`PROMPT.md`](PROMPT.md) e anexe
  [`CAMPOS.md`](CAMPOS.md), [`rascunho-modelo.json`](rascunho-modelo.json) e o conteúdo do
  mês. Salve o JSON que voltar.
- **No Claude Code, neste repositório:** peça "gere o macro de setembro a partir deste
  arquivo". A skill `relatorio-macro` faz os três passos.

Guarde o rascunho em `macro/<ano>-<mês>/rascunho.json`. É o registro do que foi publicado, e
serve de ponto de partida para o mês seguinte.

## 2. O PDF

```bash
npm run macro -- macro/2026-09/rascunho.json
```

Saem, na mesma pasta, o HTML e o PDF dos quatro segmentos. Para um só:
`--segmentos=private`. O terminal lista o que ficou em branco e os campos do rascunho que o
modelo não tem, que quase sempre são um nome digitado errado.

Sem terminal, a ferramenta faz o mesmo: escolha o relatório macroeconômico do segmento, vá a
**Exportar > Rascunho > Carregar**, escolha o JSON e gere o PDF.

## 3. A revisão

Leia o PDF inteiro antes de enviar. O script garante o desenho, não o conteúdo: confira os
números contra a fonte e o que a lista de campos em branco mostrou.

## Como funciona

`scripts/macro.mjs` não desenha nada. Ele abre a ferramenta num navegador sem janela,
carrega o rascunho e chama as mesmas funções do botão "Exportar": preencher, tirar o que ficou
em branco, repartir as páginas e refazer o sumário. O PDF que sai daqui é o mesmo que sairia
da ferramenta.

Quando o modelo mudar, `npm run macro -- --modelo` refaz `CAMPOS.md` e `rascunho-modelo.json`
(o `npm run all` já faz isso).

`2026-08/` é a primeira rodada: o relatório de agosto de 2026 passado para o modelo novo.
