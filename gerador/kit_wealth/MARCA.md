# Guia de marca: AUVP Wealth

Este guia é a referência de como um documento da AUVP Wealth se parece. Os modelos de
`modelos/` já seguem tudo o que está aqui: na dúvida, o modelo vale mais que a
descrição, e a página de componentes vale mais que qualquer marcação nova.

## As duas identidades

Todo documento da Wealth sai numa de duas identidades. Elas compartilham a mesma
diagramação, a mesma tipografia e os mesmos componentes. Mudam a cor e a logo.

| Identidade | Pasta | Quando usar | Logo |
| --- | --- | --- | --- |
| **Private** | `modelos/private/` | Família atendida pelo AUVP Private Banking | AUVP Private Banking |
| **Verde** | `modelos/verde/` | Cliente da consultoria AUVP Capital, ou cliente de fora da casa | AUVP Capital |

Não se mistura: um documento é inteiro numa identidade. Se não estiver claro qual é a do
cliente, pergunte antes de começar.

## Cores

As cores estão nos tokens do bloco `:root` de cada modelo. **Nenhuma cor se escreve
direto no HTML**: usa-se o token (`var(--brand)`) ou, melhor, o componente que já o usa.

<!-- CORES -->

Regras que valem sempre:

- **O Private não usa amarelo nem dourado em lugar nenhum.** A cor de destaque é o
  turquesa escuro, e só nos lugares do acento: número de etapa, fio de card, marcador de
  lista. O resto fica nos cinzas.
- **No verde, o dourado é acento de linha fina**: borda de card, marcador numérico,
  marcador de lista. Nunca em capa, nunca em gráfico, nunca como fundo.
- **Gráficos usam só a paleta acima**, na ordem dada. Nada de paleta genérica de
  biblioteca de gráficos. Verde e vermelho (`--pos`, `--neg`) só para o que tem sinal:
  retorno positivo ou negativo, gravidade de risco.
- **Capas e páginas no negativo são monocromáticas**: logo, título, réguas, grafismo e
  texto, tudo em branco sobre o degradê.
- **Sobre fundo branco a logo é sempre a preta**; sobre o degradê, a branca.

## Tipografia

- **Uma família só: Anek Latin**, em cinco pesos (300, 400, 600, 700 e 800), já embutida
  em cada modelo. Não se troca, não se acrescenta outra.
- Títulos de página em caixa alta e peso 800 (`h1.t`); subtítulos em caixa alta, peso
  700, com fio embaixo (`h2`); o rótulo acima do título (`.eyebrow`) é só texto.
- Na capa, o título combina uma parte leve (300) e uma em negrito (800): "Wealth
  **Planning**".
- Parágrafos e itens de lista saem justificados e hifenizados. Isso já está no estilo.

## Página

| Formato | Medida | Uso |
| --- | --- | --- |
| A4 retrato | 210 × 297 mm | relatórios e estudos para ler |
| 16:9 | 338,667 × 190,5 mm | apresentações e propostas |

- A página tem tamanho fechado e **não cresce**: o que não cabe fica cortado. Quando um
  conteúdo não cabe, **ele ganha outra página**. Nunca se reduz fonte, entrelinha ou
  espaçamento para caber.
- Toda página de conteúdo tem cabeçalho (seção à esquerda; data e logo à direita) e
  rodapé (número e aviso de confidencialidade). O número é sequencial e a capa não conta.
- Uma página pode ir **no negativo**: fundo em degradê, texto branco. Use para a página
  que precisa se destacar, como a do investimento. Uma ou duas por documento, no máximo.
  O jeito mais seguro é copiar a página no negativo da proposta (a do investimento). Para
  virar uma página clara, são três trocas:
  1. `class="slide"` passa a `class="slide dark"` (no A4, `class="page dark"`);
  2. entra `<div class="grain"></div>` como primeiro filho da `<section>`;
  3. a logo do cabeçalho perde a classe `logo-ink` (`class="logo logo-ink"` passa a
     `class="logo"`), para sair branca.

## Linhas e espaços

- **Dois pesos de linha, e só dois:** 1 px para todo fio (réguas, tabelas, molduras) e
  1,33 px para os acentos (borda de card, topo de indicador, total de tabela). Não há
  barras grossas.
- **Escala de espaços em mm:** 1, 1,5, 2, 3, 4, 5, 6, 8, 10, 12 e 16. Toda margem, recuo e
  intervalo sai daí. Os espaços são generosos de propósito: o branco faz parte do
  acabamento de um material patrimonial.

## Grafismos

Estão em `marca/`. Os modelos já os trazem nas capas; raramente é preciso mexer.

- **Arcos** (`grafismo-arcos.svg`): o único que aparece fora de capa. Nunca aparece
  inteiro: as duas arestas retas saem sempre da página.
- **Leque de quadrados** e **ampulheta**: só em capa.
- Todo grafismo entra a 50% de opacidade.
- Sobre todo degradê há um granulado sutil (`.grain`). Ele já está nos modelos.

## Capas

As capas foram medidas a partir das peças originais da marca e **não se redesenham**. O
que muda é só o texto, que é campo: título (parte leve e parte em negrito), subtítulo,
cliente, responsável e data.

## Componentes

A página `modelos/<identidade>/componentes-*.html` mostra cada componente pronto, um por
página, com o nome e a chave. É dali que se copia a marcação. Os principais:

| Para | Classe | Observação |
| --- | --- | --- |
| Título da página | `h1.t` | um por página |
| Abertura | `.eyebrow` + `h1.t` + `p.lead` | rótulo, título e uma ou duas frases |
| Subtítulo de seção | `h2` | |
| Duas ou três colunas | `.cols2`, `.cols3`, `.cols2u` (1,5 : 1) | |
| Ocupar a sobra vertical do slide | `.center` | envolve o conteúdo principal do 16:9 |
| Painel cinza | `.painel` | a coluna "o que não inclui" |
| Destaque | `.note` | caixa com fio da marca, para o que não pode passar batido |
| Lista com marcador | `ul.lista` | `ul.lista.small` em corpo menor |
| Cartões | `.cards` com `.card` | `style="--n:3"` diz quantos por linha |
| Indicadores | `.kpis` com `.kpi` (`.k` rótulo, `.v` valor, `.s` nota) | `style="--n:2"` diz quantos por linha; `.kpi.grande` lidera a fileira |
| Número em destaque | `.hero` + `.stats` | um número grande e uma fileira de apoio |
| Frentes numeradas | `ol.tl` | duas colunas |
| Etapas em linha | `ol.steps` | `style="--n:4"` |
| Etapas no trilho | `ol.flow` | com etiqueta de prazo |
| Tabela | `table.tb` | `sm` ou `xs` reduzem o corpo; `fix` com `<colgroup>` fixa larguras; `tfoot` é a linha de total |
| Lista de rótulo e valor | `.dl` com `dt`/`dd` | contatos (componente "Contato") |
| Texto legal | `p.legal` | avisos, validade, disclaimer |
| Texto secundário | `.mut`, `.small` | |
| Gráfico | `.chart[data-grafico]` | ver abaixo |
| Imagem | `.imgbox` | ver abaixo |

**Não se criam classes novas nem se escreve CSS novo** no documento. Se nada da página de
componentes serve, o caminho é perguntar à AUVP, não inventar.

Vale copiar uma página ou um componente de **outro modelo da mesma identidade** (da
proposta para uma apresentação em branco, por exemplo). Não vale misturar identidades.

O que se pode ajustar num componente sem perguntar:

- **Quantidade:** tirar ou repetir itens de lista, cartões, etapas e indicadores, e
  acertar o `--n` para o número de itens.
- **Tabela:** tirar linhas e colunas (o `<th>` e os `<td>` da coluna juntos) e acrescentar
  a linha de total em `<tfoot>`.
- **Altura de gráfico e imagem:** aumentar o `min-height` para ocupar a página. Nunca
  diminuir abaixo de `52mm`.

Fonte, cor, espaçamento e margem não se ajustam.

### Links

E-mail, WhatsApp e site podem sair clicáveis no PDF:
`<a href="mailto:ana@exemplo.com">ana@exemplo.com</a>`,
`<a href="https://wa.me/5511988887777">(11) 98888-7777</a>`. O texto do link é o mesmo
que se leria sem ele.

### Gráficos

Um gráfico é a moldura `.chart` com o formato em `data-grafico` (`donut`, `anel`, `bars`
ou `line`). Para desenhá-lo, acrescente os dados em `data-valores`, em JSON, e o script de
PDF desenha o gráfico em vetor, nas cores da identidade:

```html
<div class="chart" data-img="g1" data-grafico="donut" style="flex:1 1 auto;min-height:52mm"
     data-valores='[{"r":"Renda fixa","v":[45]},{"r":"Ações","v":[25]},{"r":"Imóveis","v":[30]}]'>
  …
</div>
```

- `r` é o rótulo; `v` é a lista de valores, um por série.
- `anel` tem duas séries: a posição atual e a meta (`"v":[45,40]`).
- Para duas séries em `bars` ou `line`, nomeie-as em `data-series="Carteira|IPCA + 5%"`.
- Valores aceitam o formato brasileiro (`"1.234,56"`) ou número (`1234.56`).
- **O título do gráfico vai fora da moldura**, num `h2` logo acima dela. O texto dentro
  da moldura (`.cl`, `.cd`) é instrução de preenchimento e some quando o gráfico é
  desenhado.
- Os gráficos do catálogo trazem dado de exemplo e o atributo `data-exemplo`. Ao copiar,
  troque os valores e **tire o `data-exemplo`**: enquanto ele estiver lá, o script avisa.

### Imagens

A moldura `.imgbox` marca onde entra uma imagem. Troque-a por:

```html
<div class="imgcheia" style="flex:1 1 auto;min-height:52mm"><img src="imagens/organograma.png" alt=""></div>
```

A imagem fica numa pasta `imagens/` ao lado do HTML. Imagem não é lugar de gráfico: um
gráfico se faz com `.chart`, para sair nas cores e na fonte da casa.

## Texto

- **Português do Brasil**, registro formal e direto, sem jargão de venda. Sem ponto de
  exclamação, sem emoji.
- **Nenhum travessão** (—) em texto que chega ao cliente: reescreva com vírgula,
  dois-pontos ou parênteses.
- Números no padrão brasileiro: `R$ 1.234.567,89`, `12,5%`, `1,2 mi`. Datas por extenso no
  cabeçalho e na capa: `outubro de 2026`, `28 de outubro de 2026`.
- Títulos curtos, de uma linha. O título diz o assunto da página; a linha de abertura
  (`.lead`) diz a conclusão.
- O nome é **AUVP Wealth**. O método é o da AUVP: Estudo Preliminar de Wealth Planning
  (EPWP), depois o Roadmap.

### Texto da casa

Alguns textos são institucionais e entram como estão: o "Sobre a AUVP Wealth", a
descrição do EPWP, as frentes, os entregáveis e o que fica fora do escopo. O
**disclaimer legal** é texto do jurídico: **não se edita, não se resume e não se tira**.
Todo documento da Wealth fecha com ele.
