# -*- coding: utf-8 -*-
"""Monta o kit da AUVP Wealth para os parceiros externos.

    python3 gerador/kit_wealth.py              # kit/auvp-wealth/ e kit/auvp-wealth.zip
    python3 gerador/kit_wealth.py --sem-pdf    # sem os PDFs de referência

Os parceiros que tocam a Wealth produzem os próprios relatórios, com o Claude
Code, fora desta ferramenta. O kit é o que eles recebem: uma pasta que funciona
sozinha, com as instruções que o Claude Code lê ao abri-la, o guia de marca, os
modelos nas duas identidades e um script que confere e exporta o PDF.

As duas identidades são o Private Banking, para a família que o Private atende,
e o verde da consultoria, para cliente da consultoria ou de fora da casa. O
verde não existe em `modelos/`: a Wealth só aparece na ferramenta no Private, e
o kit não deve mudar o que a ferramenta oferece.

Nada aqui é escrito à mão no kit. Os modelos saem dos mesmos construtores de
`modelos/`, o texto vem de `gerador/kit_wealth/`, as cores do guia saem dos
temas: se a marca mudar, rodar de novo e mandar o zip novo basta.
"""
import json
import os
import shutil
import subprocess
import sys
import zipfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import build  # noqa: E402
from layout import *  # noqa: E402,F403
import blocos  # noqa: E402
import d_wealth_proposta  # noqa: E402
import d_wealth_snapshot  # noqa: E402

FONTE = os.path.join(ROOT, "gerador", "kit_wealth")
KIT = os.path.join(ROOT, "kit")
SAIDA = os.path.join(KIT, "auvp-wealth")

# O verde é o tema da consultoria sem o rótulo "Consultoria" na faixa da capa:
# o documento pode ir para quem não é cliente dela.
IDENTIDADES = {
    "private": dict(THEMES["private"]),
    "verde": dict(THEMES["consultoria"], nome="Wealth", nome_full="AUVP Wealth", rotulo=""),
}
NOME_IDENTIDADE = {"private": "AUVP Private Banking", "verde": "AUVP Capital (verde)"}


# --------------------------------------------------- documentos em branco
# Os em branco da ferramenta fecham com os avisos de investimento. Os da Wealth
# fecham com o disclaimer jurídico da proposta e o contato do responsável.

def _identificacao():
    return [ph("nome_cliente", "Ex.: Maria e João Silva"),
            "Responsável: " + ph("nome_responsavel"),
            ph("capa_linha_livre", "Uma linha a mais na capa; apague a linha se não precisar"),
            ph("data_documento")]


CONTATO = """<h2>Fale conosco</h2>
<div class="dl">
  <dt>Responsável</dt><dd>%s</dd>
  <dt>WhatsApp</dt><dd>%s</dd>
  <dt>E-mail</dt><dd>%s</dd>
</div>""" % (ph("nome_responsavel"), ph("whatsapp_contato"), ph("email_contato"))


def livre_a4(t, seg):
    set_date_ph("data_documento")
    return [
        cover_a4(t, ph("capa_titulo_1", "Primeira palavra do título, em peso leve", padrao="Wealth"),
                 ph("capa_titulo_2", "Segunda palavra do título, em negrito", padrao="Planning"),
                 ph("capa_rodape_1", "Primeira palavra da linha de baixo, em peso leve", padrao="Estudo"),
                 ph("capa_rodape_2", "Segunda palavra da linha de baixo, em negrito", padrao="Patrimonial"),
                 _identificacao()),
        page_a4(t, "Avisos", 2, """<h1 class="t">Disclaimer legal e de responsabilidade profissional</h1>
%s
<div style="margin-top:8mm">%s</div>""" % (d_wealth_proposta.DISCLAIMER, CONTATO)),
    ]


def livre_slide(t, seg):
    set_date_ph("data_documento")
    return [
        cover_slide(t, ph("capa_titulo_1", "Primeira parte do título, em peso leve", padrao="Wealth"),
                    ph("capa_titulo_2", "Segunda parte do título, em negrito", padrao="Planning"),
                    ph("capa_subtitulo", "Uma linha sob o título", padrao="O assunto desta apresentação"),
                    _identificacao()),
        slide(t, "Avisos", 2, """<h1 class="t">Disclaimer legal e de responsabilidade profissional</h1>
<div class="center">%s</div>""" % d_wealth_proposta.DISCLAIMER),
    ]


# ------------------------------------------------------------ componentes
# Um componente por página, com o nome e a chave no alto: é o catálogo de onde
# o Claude Code do parceiro copia a marcação, em vez de inventar uma. Os
# gráficos vêm com dado de exemplo, para mostrar o desenho e o `data-valores`.

MESES6 = MESES_CURTOS[:6]
AMOSTRA = {
    "donut": [{"r": r, "v": [v]} for r, v in
              [("Renda fixa", 45), ("Ações", 25), ("Imóveis", 20), ("Exterior", 10)]],
    "anel": [{"r": r, "v": [a, m]} for r, a, m in
             [("Renda fixa", 45, 40), ("Ações", 25, 30), ("Imóveis", 20, 15), ("Exterior", 10, 15)]],
    "bars": [{"r": m, "v": [v]} for m, v in zip(MESES6, [12, 18, 15, 22, 19, 26])],
    "bars2": [{"r": m, "v": [a, b]} for m, a, b in
              zip(MESES6, [12, 18, 15, 22, 19, 26], [10, 14, 16, 18, 20, 21])],
    "line": [{"r": m, "v": [v]} for m, v in
             zip(MESES_CURTOS, [100, 102, 101, 104, 107, 106, 109, 112, 111, 115, 118, 121])],
    "line2": [{"r": m, "v": [a, b]} for m, a, b in
              zip(MESES_CURTOS, [100, 102, 101, 104, 107, 106, 109, 112, 111, 115, 118, 121],
                  [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111])],
}

# Os componentes de `layout.py` que os documentos da Wealth usam e que a
# biblioteca de blocos não traz.
EXTRAS = [
    ("cartoes", "Cartões", "Três blocos curtos com o fio da marca à esquerda, como em Quem somos.",
     lambda i: cards([(ph("bl%d_card_%d_titulo" % (i, k)), ph("bl%d_card_%d_texto" % (i, k)))
                      for k in (1, 2, 3)], n=3)),
    ("frentes", "Frentes numeradas", "Lista numerada em duas colunas, como as frentes do diagnóstico.",
     lambda i: timeline([(ph("bl%d_frente_%d_titulo" % (i, k)), ph("bl%d_frente_%d_texto" % (i, k)))
                         for k in (1, 2, 3, 4)])),
    ("trilho", "Etapas no trilho", "Etapas sobre um trilho contínuo, com etiqueta de prazo.",
     lambda i: flow([(ph("bl%d_etapa_%d_prazo" % (i, k)), ph("bl%d_etapa_%d_titulo" % (i, k)),
                      ph("bl%d_etapa_%d_texto" % (i, k))) for k in (1, 2, 3, 4)])),
    ("legal", "Texto legal", "Parágrafo em corpo menor, para aviso, validade e disclaimer.",
     lambda i: '<p class="legal">%s</p>' % ph("bl%d_texto" % i)),
    ("nota_rodape", "Nota de rodapé",
     "Número no texto e referência no pé da página, para citar lei ou fonte. O bloco "
     "<code>notas</code> vai por último na página; a numeração segue pelo documento inteiro.",
     lambda i: ('<p>%s<sup class="nr">1</sup></p>\n'
                '<div class="notas">\n  <p><sup class="nr">1</sup>%s</p>\n</div>'
                % (ph("bl%d_texto" % i), ph("bl%d_nota_1" % i)))),
    ("numero", "Número em destaque", "Um número grande com legenda e uma fileira de apoio.",
     lambda i: hero(ph("bl%d_numero" % i), ph("bl%d_legenda" % i),
                    [(ph("bl%d_apoio_%d_numero" % (i, k)), ph("bl%d_apoio_%d_legenda" % (i, k)))
                     for k in (1, 2, 3)])),
    ("kpis_destaque", "Números com destaque", "O primeiro número maior que os outros, que lidera a fileira.",
     lambda i: kpis([(ph("bl%d_kpi_%d_rotulo" % (i, k)), ph("bl%d_kpi_%d_valor" % (i, k)),
                      ph("bl%d_kpi_%d_nota" % (i, k))) for k in (1, 2, 3)], n=4, destaque=True)),
    ("contato", "Contato", "Rótulo e valor, para o responsável e os canais de contato.",
     lambda i: CONTATO),
]


def _catalogo():
    itens = [(k, b["nome"], b["descricao"], b["html"]) for k, b in blocos.BLOCOS.items()]
    return itens + [(k, n, d, h) for k, n, d, h in EXTRAS]


def _com_amostra(chave, html):
    tipo = chave.replace("grafico_", "")
    if tipo not in AMOSTRA:
        return html
    # `data-exemplo` marca o dado de mentira: o script de PDF avisa se ele
    # chegar a um documento copiado do catálogo.
    dados = json.dumps(AMOSTRA[tipo], ensure_ascii=False)
    return html.replace('class="chart"', "class=\"chart\" data-exemplo data-valores='%s'" % dados, 1)


def _rotulo(n, chave, nome, descricao):
    return ('<p class="mut small" style="margin-bottom:4mm">Componente %02d · <strong>%s</strong> '
            '(<code>%s</code>). %s</p>') % (n, nome, chave, descricao)


def _indice(itens):
    return table(["Componente", "Chave", "Para quê"],
                 [[nome, "<code>%s</code>" % k, desc] for k, nome, desc, _ in itens],
                 xs=True, widths=[24, 18, 58])


def componentes(slide_fmt):
    def builder(t, seg):
        set_date_ph("data_documento")
        itens = _catalogo()
        pagina = slide if slide_fmt else page_a4
        P = [pagina(t, "Componentes", 1, """<h1 class="t">Catálogo de componentes</h1>
<p class="lead">Cada página mostra um componente pronto. Copie a marcação do arquivo HTML e troque os
campos <code>{{…}}</code> pelo texto. Os gráficos desenham a partir do atributo
<code>data-valores</code>.</p>""" + ("" if slide_fmt else _indice(itens)))]
        if slide_fmt:
            # No 16:9 o índice não cabe com a abertura: vai numa página só dele.
            meio = (len(itens) + 1) // 2
            for parte in (itens[:meio], itens[meio:]):
                P.append(slide(t, "Componentes", 1, _indice(parte)))
        for n, (chave, nome, desc, html) in enumerate(itens, start=1):
            P.append(pagina(t, "Componentes", 1, _rotulo(n, chave, nome, desc) +
                            _com_amostra(chave, html(n))))
        return P
    return builder


# ---------------------------------------------------------------- o kit

DOCUMENTOS = [
    ("proposta-wealth-planning", dict(formato="slide", titulo="Wealth Planning, proposta: %s",
                                      builder=d_wealth_proposta.build)),
    ("snapshot-patrimonial", dict(formato="slide", titulo="Wealth Planning Snapshot: %s",
                                  builder=d_wealth_snapshot.build)),
    ("apresentacao-em-branco", dict(formato="slide", titulo="Apresentação: %s", builder=livre_slide)),
    ("documento-em-branco-a4", dict(formato="a4", titulo="Documento: %s", builder=livre_a4)),
    ("componentes-apresentacao", dict(formato="slide", titulo="Componentes 16:9: %s",
                                      builder=componentes(True))),
    ("componentes-a4", dict(formato="a4", titulo="Componentes A4: %s", builder=componentes(False))),
]

ASSETS = [
    ("assets relatórios/SVG/LOGO PRIVATE BANKING BRANCA.svg", "logo-private-branca.svg"),
    ("assets relatórios/SVG/LOGO PRIVATE BANKING PRETA.svg", "logo-private-preta.svg"),
    ("assets relatórios/1x/LOGO PRIVATE BANKING BRANCA.png", "logo-private-branca.png"),
    ("assets relatórios/1x/LOGO PRIVATE BANKING PRETA.png", "logo-private-preta.png"),
    ("assets relatórios/SVG/" + LOGO_CAPITAL, "logo-capital-branca.svg"),
    ("assets relatórios/SVG/" + LOGO_CAPITAL.replace("BRANCA", "PRETA"), "logo-capital-preta.svg"),
    ("assets relatórios/1x/" + LOGO_CAPITAL.replace(".svg", ".png"), "logo-capital-branca.png"),
    ("assets relatórios/1x/" + LOGO_CAPITAL.replace("BRANCA.svg", "PRETA.png"), "logo-capital-preta.png"),
    ("assets relatórios/SVG/GRAFISMO 1.svg", "grafismo-leque.svg"),
    ("assets relatórios/SVG/GRAFISMO 2.svg", "grafismo-ampulheta.svg"),
    ("assets relatórios/SVG/GRAFISMO 3.svg", "grafismo-arcos.svg"),
] + [("assets/fonts/AnekLatin-%d.woff2" % w, "fontes/AnekLatin-%d.woff2" % w)
     for w in (300, 400, 600, 700, 800)]


def _cores():
    """A tabela de cores do guia, tirada dos temas: é o que impede o guia de
    dizer uma cor e o modelo usar outra."""
    linhas = ["| Papel | Token | Private | Verde |", "| --- | --- | --- | --- |"]
    p, v = IDENTIDADES["private"], IDENTIDADES["verde"]
    for papel, token, chave in [
            ("Cor base (capa, cabeçalho de tabela, títulos de seção)", "--brand", "brand"),
            ("Acento (fio de card, número de etapa, marcador)", "--accent", "accent"),
            ("Acento sobre fundo escuro", "--accent-dk", "accent_dk"),
            ("Texto", "--ink", "ink"), ("Texto secundário", "--ink-2", "ink2"),
            ("Fio", "--line", "line"), ("Fundo de apoio", "--soft", "soft")]:
        linhas.append("| %s | `%s` | `%s` | `%s` |" % (
            papel, token, p.get(chave, p["accent"]), v.get(chave, v["accent"])))
    linhas += ["", "Gráficos, nesta ordem (`--c1` a `--c8`):", "",
               "- **Private:** " + " · ".join("`%s`" % c for c in p["chart"]),
               "- **Verde:** " + " · ".join("`%s`" % c for c in v["chart"])]
    return "\n".join(linhas)


# A imagem que entra no lugar de uma moldura. Na ferramenta esta regra é posta
# na exportação; no kit o documento é editado à mão, e ela vem no modelo.
CSS_KIT = (".imgcheia{overflow:hidden;display:flex}"
           ".imgcheia img{width:100%;height:100%;object-fit:cover;display:block}")


def _com_css_kit(caminho):
    with open(caminho, encoding="utf-8") as f:
        html = f.read()
    with open(caminho, "w", encoding="utf-8") as f:
        f.write(html.replace("</style>", CSS_KIT + "\n</style>", 1))


def _esvazia(pasta):
    # Esvazia em vez de apagar a pasta: no Windows, um terminal aberto nela
    # impede remover o diretório, e o rmtree parava no meio.
    for nome in os.listdir(pasta):
        cheio = os.path.join(pasta, nome)
        if os.path.isdir(cheio):
            shutil.rmtree(cheio)
        else:
            os.remove(cheio)


def monta_kit():
    if os.path.isdir(SAIDA):
        _esvazia(SAIDA)
    shutil.copytree(FONTE, SAIDA, dirs_exist_ok=True)

    guia = os.path.join(SAIDA, "MARCA.md")
    with open(guia, encoding="utf-8") as f:
        texto = f.read()
    with open(guia, "w", encoding="utf-8") as f:
        f.write(texto.replace("<!-- CORES -->", _cores()))

    for ident, t in IDENTIDADES.items():
        pasta = os.path.join(SAIDA, "modelos", ident)
        os.makedirs(pasta)
        seg = "private" if ident == "private" else "consultoria"
        for nome, doc in DOCUMENTOS:
            caminho, n = build.monta(doc, seg, NOME_IDENTIDADE[ident], t, out=pasta,
                                     nome=nome + ".html")
            _com_css_kit(caminho)
            print("  %-58s %2d páginas" % (os.path.relpath(caminho, ROOT), n))

    os.makedirs(os.path.join(SAIDA, "marca", "fontes"))
    for origem, destino in ASSETS:
        shutil.copyfile(os.path.join(ROOT, origem), os.path.join(SAIDA, "marca", destino))
    shutil.copyfile(os.path.join(ROOT, "docs", "graficos.js"),
                    os.path.join(SAIDA, "ferramentas", "graficos.js"))


def pdfs_de_referencia():
    # O mesmo script que o parceiro vai usar: se ele quebrar, quebra aqui antes.
    subprocess.run(["node", os.path.join("ferramentas", "pdf.mjs"), "modelos",
                    "--saida=referencia", "--modelo"], cwd=SAIDA, check=True)


def zipa():
    destino = SAIDA + ".zip"
    with zipfile.ZipFile(destino, "w", zipfile.ZIP_DEFLATED) as z:
        for raiz, _, arquivos in os.walk(SAIDA):
            for a in sorted(arquivos):
                cheio = os.path.join(raiz, a)
                z.write(cheio, os.path.join("auvp-wealth", os.path.relpath(cheio, SAIDA)))
    print("%s (%.1f MB)" % (os.path.relpath(destino, ROOT), os.path.getsize(destino) / 1e6))


def main(args):
    monta_kit()
    if "--sem-pdf" not in args:
        pdfs_de_referencia()
    zipa()
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
