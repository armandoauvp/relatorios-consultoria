# Rascunho do relatório macro: instruções para o Claude

Cole este texto numa conversa com o Claude, anexe `CAMPOS.md`, `rascunho-modelo.json` e o
conteúdo do mês (Word, PDF ou texto), e peça o rascunho. O que volta é um arquivo JSON que
a ferramenta carrega e que o `npm run macro` transforma em PDF.

---

Você vai transformar o conteúdo do relatório macroeconômico deste mês no rascunho JSON do
modelo da AUVP. Os anexos são:

- `rascunho-modelo.json`: o rascunho vazio, com todos os campos do modelo.
- `CAMPOS.md`: o que vai em cada campo, página por página.
- O conteúdo do mês, escrito pelo time.

Devolva um único arquivo JSON, com a mesma forma do `rascunho-modelo.json`:

```json
{ "documento": "relatorio-macroeconomico", "valores": { … }, "linhas": { … }, "fora": [] }
```

## Regras

1. **Não invente nada.** Todo número, nome e fato vem do conteúdo do mês. O que o conteúdo
   não traz fica `""`: campo vazio sai do documento, sem deixar buraco.
2. **Não reescreva o texto do time.** Distribua o texto nos campos. Pode corrigir erro de
   digitação e ajustar a pontuação, e só isso.
3. **Sem travessão (—).** Onde houver um, reescreva a frase com vírgula, dois-pontos ou
   parênteses. É regra da casa para todos os documentos.
4. **Parágrafos:** num campo de texto longo, separe os parágrafos com uma linha em branco
   (`\n\n`). Cada um vira um parágrafo no documento.
5. **Datas:** `mes_referencia` é o mês de publicação ("Setembro de 2026"); `mes_fechamento`
   é o mês analisado ("Agosto").
6. **Títulos** vão em caixa normal ("Brasil: a trajetória fiscal em foco"): o documento põe
   em caixa alta sozinho.
7. **Não preencha** registro do analista, disclaimer, e-mail, ouvidoria, razão social e
   CNPJ se o conteúdo não trouxer: são dados da casa.

## Onde vai cada parte do conteúdo

- **Resumo executivo:** `titulo_do_mes` é a frase-título do mês; `resumo_executivo` é o
  parágrafo de abertura.
- **Panorama:** os oito indicadores do painel. O rótulo vem escrito (`painel_N_rotulo`) e
  pode ser trocado se o time usar outro indicador; `painel_N_valor` é o número e
  `painel_N_nota` a linha de apoio. `fonte_painel` é a fonte.
- **Principais destaques:** cinco mensagens, cada uma com título e texto.
- **Análises do mês:** são as seções de assunto livre, na ordem em que aparecem no conteúdo:
  - `analise_brasil_*`: a primeira análise, sobre Brasil, com até dois subtítulos e textos.
  - `analise_tema1_*`: a segunda, com linha de abertura (`_lead`), um texto e uma tabela de
    até cinco linhas e quatro colunas (cenários, por exemplo), com fonte.
  - `analise_tema2_*`: a terceira, com abertura e até dois subtítulos e textos.
  - `global_*`: o panorama internacional, com até três subtítulos e textos.
  - `analise_tema3_*`: a quarta, com abertura e dois textos.

  Se o mês tiver menos análises, deixe as que sobram vazias; se tiver mais, junte o que for
  do mesmo assunto ou avise que falta espaço.
- **Como a carteira está posicionada:** `carteira_lead` e a tabela de posição e racional
  (`pos_N_posicao`, `pos_N_racional`). Tem quatro linhas; para mais, escreva `pos_5_…`,
  `pos_6_…` e declare em `linhas`:
  `"linhas": { "pos_1_posicao": { "fora": [], "extra": [5, 6] } }`.
- **Expectativa para classes de ativos:** cada item é um rótulo curto em negrito
  (`classe_rf_1_rotulo`, termine com ponto) e o texto (`classe_rf_1_texto`). Classes: `rf`
  (até 4), `rv` (até 3), `fii` (até 2), `intl` (até 3), `cripto` (1).
- **Fechamento:** mês e acumulado no ano de CDI, Ibovespa, IMA-B, IFIX, dólar e IPCA
  (`fech_<indicador>_mes`, `fech_<indicador>_ano`), e `fechamento_nota`.
- **Riscos e oportunidades:** `riscos_lead`; até cinco riscos e três oportunidades, cada um
  com título, texto e ação (a ação vai sem a palavra "Ação", que o documento já escreve).
- **Perspectivas:** até cinco eventos da agenda (`ag_N_data`, `ag_N_evento`,
  `ag_N_motivo`) e o parágrafo de fecho (`perspectivas_texto`).
- **Síntese:** até três parágrafos (`sintese_1` a `sintese_3`).
- **Notas:** as fontes (`fonte_indicadores`, `fonte_cenarios`).

Ao final, liste em poucas linhas o que do conteúdo não coube em nenhum campo.
