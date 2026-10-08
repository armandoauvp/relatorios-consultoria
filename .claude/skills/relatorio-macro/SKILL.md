---
name: relatorio-macro
description: Gera o relatório macroeconômico mensal da AUVP a partir do conteúdo que o time fecha no mês (Word, PDF ou texto). Use quando pedirem o macro de um mês, para transformar o conteúdo no rascunho JSON do modelo e gerar os PDFs dos segmentos.
---

# Relatório macro do mês

1. Leia `macro/PROMPT.md` e siga as regras dele. Leia `macro/CAMPOS.md` e
   `macro/rascunho-modelo.json` para saber os campos. Se o modelo mudou desde a última vez,
   rode antes `npm run macro -- --modelo`.
2. Leia o conteúdo do mês que a pessoa indicou. Se houver o rascunho do mês anterior em
   `macro/<ano>-<mês>/rascunho.json`, use-o como referência de formato, nunca de conteúdo.
3. Escreva `macro/<ano>-<mês>/rascunho.json` (o mês é o de publicação, o mesmo de
   `mes_referencia`).
4. Rode `npm run macro -- macro/<ano>-<mês>/rascunho.json`. Se ele acusar campos que o
   modelo não tem, corrija os nomes e rode de novo.
5. Abra um dos PDFs e confira: sumário, títulos, tabelas e se nenhum texto ficou cortado.
6. Responda com o caminho dos PDFs, a lista de campos que ficaram em branco e o que do
   conteúdo não coube em nenhum campo. Não publique nem envie nada.
