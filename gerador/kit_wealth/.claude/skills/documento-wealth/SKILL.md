---
name: documento-wealth
description: Monta um documento da AUVP Wealth (proposta de Wealth Planning, snapshot patrimonial, estudo, relatório ou apresentação) a partir do material do cliente, no padrão de marca, e exporta em PDF. Use sempre que pedirem um documento, relatório, proposta ou apresentação da Wealth.
---

# Documento da AUVP Wealth

## 1. Entender o pedido

Antes de escrever qualquer coisa, tenha claro:

- **Cliente:** o nome como deve aparecer na capa.
- **Identidade:** `private` (cliente do Private Banking) ou `verde` (cliente da
  consultoria ou de fora da casa). Se não foi dito, pergunte.
- **Documento:** qual dos modelos serve (tabela abaixo).
- **Material:** o que a pessoa mandou (Word, PDF, planilha, anotações). Leia tudo.

| Pedido | Modelo | Formato |
| --- | --- | --- |
| Proposta do Estudo Preliminar de Wealth Planning (EPWP) | `proposta-wealth-planning.html` | 16:9 |
| Fotografia patrimonial do cliente, snapshot | `snapshot-patrimonial.html` | 16:9 |
| Outra apresentação: devolutiva, roadmap, reunião | `apresentacao-em-branco.html` | 16:9 |
| Outro documento para ler: estudo, parecer, relatório | `documento-em-branco-a4.html` | A4 |

Se o pedido for um dos dois primeiros, use o modelo pronto: a ordem das páginas já é a
da casa. Os em branco trazem só a capa e o fecho com o disclaimer; o meio se monta.

## 2. Copiar o modelo

```bash
mkdir -p documentos/<cliente>
cp modelos/<identidade>/<modelo>.html documentos/<cliente>/<documento>.html
```

Use nomes de pasta e arquivo em minúsculas, sem acento e com hífen:
`documentos/maria-joao-silva/proposta-wealth-planning.html`.

Abra também o PDF correspondente em `referencia/<identidade>/` para ver como cada página
deve ficar.

## 3. Preencher

- Troque cada `<span class="ph" …>{{campo}}</span>` pelo texto (ver `CLAUDE.md`).
- Datas: o mesmo campo de data aparece na capa e no cabeçalho de cada página. Na capa ele
  leva a data inteira (`28 de outubro de 2026`); no cabeçalho, mês e ano
  (`outubro de 2026`).
- `capa_linha_livre` é uma linha a mais na identificação da capa, para o que o caso pedir
  (a família, o número do estudo, "Versão para discussão"). Sem uso, a linha sai inteira.
- Valores em formato brasileiro: `R$ 18.600`, `12,5%`.
- O que não veio no material fica como campo. Não invente. O limite é este:
  - **pode:** conta direta sobre números do material (percentual de um total que veio,
    soma, variação), desde que a conta esteja certa;
  - **pode, mas avise no fim:** ligar uma coisa a outra que o material não ligou (qual
    caminho responde a qual risco), resumir ou reordenar o que veio;
  - **não pode:** número, nome, prazo, gravidade ou recomendação que o material não traz.
- Linhas de tabela que sobrarem saem inteiras (`<tr>…</tr>`).

## 4. Montar páginas novas (documentos em branco, ou página a mais)

1. Copie uma `<section class="slide">` (ou `class="page"`) de conteúdo do próprio documento:
   o fecho serve. Assim cabeçalho, logo e rodapé ficam iguais.
2. Troque o nome da seção no cabeçalho (`<div class="sec">…</div>`).
3. Esvazie o `<div class="pg-body">` e monte o conteúdo com os componentes de
   `modelos/<identidade>/componentes-apresentacao.html` (16:9) ou `componentes-a4.html` (A4).
   Copie a marcação do componente e troque os campos `{{bl…}}` pelo texto.
4. Uma ideia por página: título (`h1.t`), uma linha de abertura (`p.lead`) e um ou dois
   componentes. No 16:9, envolva o miolo em `<div class="center">`.
5. Não se preocupe com o número da página: o script de PDF numera em sequência na
   exportação.
6. O fecho com o disclaimer é sempre a última página.

Para um gráfico, use o componente de gráfico e preencha `data-valores` (ver `MARCA.md`).

Para citar lei ou fonte, use o componente **Nota de rodapé**: `<sup class="nr">1</sup>` no
texto e o bloco `<div class="notas">` como último elemento do `pg-body`, que desce sozinho
até o pé da página. O número se escreve à mão e segue pelo documento inteiro (1, 2, 3…),
sem recomeçar a cada página; a nota fica na mesma página da chamada.

## 5. Conferir e exportar

```bash
node ferramentas/pdf.mjs documentos/<cliente>/<documento>.html --fotos
```

O `--fotos` grava também um PNG por página em `<documento>-paginas/`, para conferir o
resultado olhando.

- **ERRO de estouro:** o conteúdo daquela página não cabe. Divida-o em duas páginas, ou
  passe parte para a seguinte. Não reduza fonte nem espaço. Rode de novo até sair sem
  erro.
- **aviso de campo sem preencher:** confira se é mesmo algo que o material não trouxe.
- **aviso de moldura vazia:** um gráfico sem `data-valores` ou uma imagem que não veio.
  Preencha ou tire o bloco.

Depois de gerado, olhe as fotos página por página, ao lado das de referência
(`referencia/<identidade>/`): capa, títulos, tabelas, nenhum texto cortado, nenhum
`{{campo}}` à mostra, nenhuma página com cara de outro documento. Apague a pasta
`-paginas/` no fim: ela é só para conferir.

## 6. Responder

Diga onde estão o HTML e o PDF, liste os campos que ficaram pendentes, o que do
material não coube em nenhuma página e o que você ligou, resumiu ou calculou por conta
própria (para quem pediu validar). Não envie o documento a ninguém.
