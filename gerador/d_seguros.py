# -*- coding: utf-8 -*-
"""Apresentação de produtos da AUVP Seguros.

A AUVP Seguros é produto próprio, na identidade da consultoria. O material
mostra como a casa trabalha — cotar em várias seguradoras, comparar e
recomendar — e os quatro seguros que oferece.

Não tem campo nenhum: é texto da casa, igual para todo cliente, e não é
confidencial. Por isso sai sem data no cabeçalho e sem o aviso de
confidencialidade no pé.

O tom mais leve vem do desenho, e não do texto: ícones em cada cobertura, o
diagrama de um perfil cotado em várias seguradoras e a fileira de ícones no
cabeçalho que mostra em qual dos quatro seguros se está. A copy entra como foi
aprovada; se ela mudar, muda aqui.
"""
from layout import *

# Ícones em traço, num quadro de 24 × 24, desenhados para este documento.
ICONES = dict(
    # os produtos
    vida='<path d="M12 19.5s-7.5-4.6-7.5-10.2A4.3 4.3 0 0 1 12 6.6a4.3 4.3 0 0 1 7.5 2.7'
         'c0 5.6-7.5 10.2-7.5 10.2z"/><path d="M7 11.5h2.5l1.2-2 2 4 1.3-2H17"/>',
    auto='<path d="M4.8 16H3.5v-3.6L6 8h9.4l3.6 4.4 1.5.5V16h-1.3"/><path d="M9 16h6"/>'
         '<circle cx="7" cy="16.3" r="2"/><circle cx="17" cy="16.3" r="2"/><path d="M6.3 12.4h12.4"/>',
    medico='<path d="M6.5 3.5H5v5a4 4 0 0 0 8 0v-5h-1.5"/><path d="M9 12.5v2a5 5 0 0 0 10 0v-2.2"/>'
           '<circle cx="19" cy="10.2" r="2.1"/>',
    saude='<path d="M9.5 4h5v5.5H20v5h-5.5V20h-5v-5.5H4v-5h5.5z"/>',
    # como trabalhamos
    cotacao='<path d="M12 4 3.5 8.5 12 13l8.5-4.5z"/><path d="M3.5 12.5 12 17l8.5-4.5"/>'
            '<path d="M3.5 16.2 12 20.7l8.5-4.5"/>',
    comparacao='<rect x="4" y="5" width="6.5" height="14" rx="1"/><rect x="13.5" y="5" width="6.5" height="14" rx="1"/>'
               '<path d="M6 9h2.5M6 12h2.5M15.5 9h2.5M15.5 12h2.5"/>',
    recomendacao='<circle cx="12" cy="12" r="8.5"/><path d="M8 12.2l2.7 2.7L16 9.5"/>',
    acompanhamento='<path d="M4.5 14v-2a7.5 7.5 0 0 1 15 0v2"/><rect x="3.5" y="13" width="4" height="6" rx="1.5"/>'
                   '<rect x="16.5" y="13" width="4" height="6" rx="1.5"/><path d="M18.5 19c0 1.4-1.6 2-4 2H13"/>',
    # vida
    morte='<path d="M3.5 12a8.5 8.5 0 0 1 17 0z"/><path d="M12 12v6a2 2 0 0 1-4 0"/><path d="M12 3.5v-1"/>',
    invalidez='<rect x="2.5" y="8.5" width="19" height="7" rx="3.5" transform="rotate(-45 12 12)"/>'
              '<rect x="9.5" y="9.5" width="5" height="5" rx=".6" transform="rotate(-45 12 12)"/>',
    doencas='<path d="M3.5 12.5h4l1.6-3.5 3 7 1.8-3.5h6.6"/>'
            '<path d="M5.4 8.6A4.3 4.3 0 0 1 12 6.6a4.3 4.3 0 0 1 7.3 4.4M6.8 16c1.9 2 4.2 3.5 5.2 4 '
            '1-.5 3.3-2 5.2-4"/>',
    diaria='<rect x="4" y="5.5" width="16" height="14" rx="2"/><path d="M4 10h16M8.5 3.5v4M15.5 3.5v4"/>'
           '<path d="M8 14h3"/>',
    cirurgia='<rect x="2" y="15.8" width="10" height="3" rx="1.5" transform="rotate(-45 7 17.3)"/>'
             '<path d="M9.5 12.7 18.8 4.6c.6 3.6-1.8 7.2-7.2 10.2z"/>',
    internacao='<path d="M3 6v13M3 15.5h18V19M21 15.5v-3a3 3 0 0 0-3-3h-8v6"/><circle cx="6.5" cy="12" r="2"/>',
    # auto
    roubo='<rect x="5" y="10.5" width="14" height="10" rx="2"/><path d="M8 10.5V8a4 4 0 0 1 8 0v2.5"/>'
          '<path d="M12 14.5v2"/>',
    terceiros='<circle cx="9" cy="8" r="3"/><path d="M3.5 19.5a5.5 5.5 0 0 1 11 0"/><circle cx="16.5" cy="9" r="2.5"/>'
              '<path d="M15.6 14.1a4.5 4.5 0 0 1 4.9 5.4"/>',
    assistencia='<circle cx="12" cy="12" r="8.5"/><path d="M12 7.5V12l3 2"/>',
    reserva='<circle cx="8" cy="15" r="4"/><path d="M11 12l8-8M16 7l2.5 2.5M14 9l2 2"/>',
    vidros='<path d="M4 17 6.5 8h11L20 17z"/><path d="M9 14.5l3-3M12 15l4-4"/>',
    # rc profissional
    defesa='<path d="M12 4v16M8 20h8M5 7h14"/><path d="M5 7l-3 6a3 3 0 0 0 6 0zM19 7l-3 6a3 3 0 0 0 6 0z"/>',
    indenizacao='<rect x="3" y="6.5" width="18" height="11" rx="1.5"/><circle cx="12" cy="12" r="2.5"/>'
                '<path d="M6.5 9.5v5M17.5 9.5v5"/>',
    acordos='<path d="M14 3.5H6.5A1.5 1.5 0 0 0 5 5v14a1.5 1.5 0 0 0 1.5 1.5h11A1.5 1.5 0 0 0 19 19V8.5z"/>'
            '<path d="M14 3.5v5h5"/><path d="M8 16c1.2-1.6 2-1.6 2.6 0s1.6 1.4 2.4 0 1.6-1 3 0"/>',
    pericias='<circle cx="10.5" cy="10.5" r="6"/><path d="M15 15l5 5"/>',
    # saúde
    familia='<circle cx="7.5" cy="7" r="2.5"/><circle cx="16.5" cy="7" r="2.5"/><circle cx="12" cy="13" r="1.8"/>'
            '<path d="M3.5 19a4 4 0 0 1 6-3.5M20.5 19a4 4 0 0 0-6-3.5M9 20.5a3 3 0 0 1 6 0"/>',
    empresa='<path d="M3.5 20.5h17M6 20.5v-16h8v16M14 9.5h4v11"/><path d="M8.5 8h3M8.5 11.5h3M8.5 15h3"/>',
    # o diagrama
    pessoa='<circle cx="12" cy="8.5" r="3.5"/><path d="M5 20a7 7 0 0 1 14 0"/>',
    escudo='<path d="M12 3.5 19 6v5.5c0 4.4-3 7.6-7 9-4-1.4-7-4.6-7-9V6z"/>',
    duvida='<path d="M9.3 9.3a2.8 2.8 0 1 1 3.9 2.6c-.8.4-1.2 1-1.2 1.8v.8"/><circle cx="12" cy="17.4" r=".4"/>',
)


def icone(nome, cls="sg-ic"):
    return '<svg class="%s" viewBox="0 0 24 24" aria-hidden="true">%s</svg>' % (cls, ICONES[nome])


def _no(nome, x, y, r, cls):
    """Um nó do diagrama: círculo com o ícone dentro, em coordenadas do SVG."""
    i = r * 1.15
    return ('<circle class="%s" cx="%g" cy="%g" r="%g"/>'
            '<svg class="%s-i" x="%g" y="%g" width="%g" height="%g" viewBox="0 0 24 24">%s</svg>') % (
        cls, x, y, r, cls, x - i / 2, y - i / 2, i, i, ICONES[nome])


def diagrama_unico():
    """Uma seguradora só: o perfil vai a um lugar e volta com uma dúvida."""
    return ('<svg class="sg-dg" viewBox="0 0 120 24" aria-hidden="true">'
            '<path class="fio mudo" d="M17 12H53M67 12H103"/>%s%s%s</svg>') % (
        _no("pessoa", 9, 12, 7, "n-pes"), _no("escudo", 60, 12, 6, "n-mudo"),
        _no("duvida", 111, 12, 7, "n-mudo"))


def diagrama_amplo():
    """O mesmo perfil cotado em cinco seguradoras ao mesmo tempo, e uma só
    recomendação no fim. O caminho escolhido sai na cor da marca."""
    ys = [5, 14.5, 24, 33.5, 43]
    # o caminho escolhido por último, para passar por cima dos outros
    fios = ""
    for j in (0, 1, 3, 4, 2):
        y, cls = ys[j], "fio" + (" sel" if j == 2 else "")
        fios += '<path class="%s" d="M16 24C38 24 38 %g 54 %gM66 %gC82 %g 82 24 103.5 24"/>' % (
            cls, y, y, y, y)
    nos = "".join(_no("escudo", 60, y, 4.5, "n-sel" if j == 2 else "n-seg") for j, y in enumerate(ys))
    return ('<svg class="sg-dg" viewBox="0 0 120 48" aria-hidden="true">%s%s%s%s</svg>') % (
        fios, _no("pessoa", 9, 24, 7, "n-pes"), nos, _no("recomendacao", 111, 24, 7.5, "n-fim"))


PRODUTOS = ["vida", "auto", "medico", "saude"]


def navegacao(atual):
    """Os quatro seguros no cabeçalho, com o desta página aceso."""
    return '<div class="sg-nav">%s</div>' % "".join(
        '<span%s>%s</span>' % (' class="on"' if p == atual else "", icone(p))
        for p in PRODUTOS)


def coberturas(itens, cls="sg-cob"):
    """As coberturas como lista de itens com ícone. A classe decide o arranjo:
    peças em grade (`sg-cob`, com `vert` ou `grande`), faixa (`sg-faixa`) ou
    lista numerada (`sg-lista`)."""
    return '<ul class="%s">%s</ul>' % (cls, "".join(
        '<li><span class="sg-bola">%s</span><span>%s</span></li>' % (icone(i), txt)
        for i, txt in itens))


def medalhao(chave, pequeno=False):
    return '<div class="sg-med%s">%s</div>' % (" pq" if pequeno else "", icone(chave))


def titulo(chave, nome):
    """O medalhão pequeno ao lado do título, para quando o título não tem a
    coluna só para ele."""
    return '<div class="sg-tit">%s<h1 class="t">%s</h1></div>' % (medalhao(chave, True), nome)


# Os quatro seguros dividem o cabeçalho, o rodapé e os ícones, mas não o
# arranjo: cada um põe em primeiro plano o que o seu texto tem de próprio. Vida
# tem mais coberturas e vai no negativo; Auto tem um parágrafo só e corre na
# horizontal; RC tem a frase mais forte e ela vira citação; Saúde tem duas
# modalidades e divide a página.

def pagina(t, no, nome, chave, corpo, dark=False, fundo=""):
    return slide(t, nome, no, corpo, dark=dark, data=False, topo=navegacao(chave),
                 rodape=t["nome_full"], fundo=fundo)


def vida(t, no, nome, chave, textos, lista, itens):
    corpo = """<div class="sg-prod sg-vida">
  <div class="sg-esq">%(med)s<h1 class="t">%(nome)s</h1>
    <p class="lead">%(p1)s</p><p class="sg-apoio">%(p2)s</p></div>
  <div class="sg-dir"><h2>%(lista)s</h2>%(cob)s</div>
</div>""" % dict(med=medalhao(chave), nome=nome, p1=textos[0], p2=textos[1], lista=lista,
                 cob=coberturas(itens, "sg-cob vert"))
    return pagina(t, no, nome, chave, corpo, dark=True,
                  fundo=graf_arcos(GRAF_SLIDE_W, "bottom-right"))


def auto(t, no, nome, chave, textos, lista, itens):
    corpo = """<div class="center sg-auto">
  <div class="sg-topo">%(tit)s<p class="lead">%(p1)s</p></div>
  <div><h2>%(lista)s</h2>%(cob)s</div>
</div>""" % dict(tit=titulo(chave, nome), p1=textos[0], lista=lista,
                 cob=coberturas(itens, "sg-faixa"))
    return pagina(t, no, nome, chave, corpo)


def rc(t, no, nome, chave, textos, lista, itens):
    corpo = """<div class="sg-prod sg-rc">
  <div class="sg-esq">%(tit)s<p class="lead">%(p1)s</p>
    <blockquote class="sg-cit"><p>%(p2)s</p></blockquote></div>
  <div class="sg-dir painel"><h2>%(lista)s</h2>%(cob)s</div>
</div>""" % dict(tit=titulo(chave, nome), p1=textos[0], p2=textos[1], lista=lista,
                 cob=coberturas(itens, "sg-lista"))
    return pagina(t, no, nome, chave, corpo)


def saude(t, no, nome, chave, textos, lista, itens):
    corpo = """<div class="sg-prod sg-saude">
  <div class="sg-bloco"><div class="grain"></div>%(med)s<h1 class="t">%(nome)s</h1></div>
  <div class="sg-dir"><p class="lead">%(p1)s</p><h2>%(lista)s</h2>%(cob)s</div>
</div>""" % dict(med=medalhao(chave), nome=nome, p1=textos[0], lista=lista,
                 cob=coberturas(itens, "sg-cob grande"))
    return pagina(t, no, nome, chave, corpo)


PILARES = [
    ("cotacao", "Cotação ampla", "O mesmo perfil é cotado em várias seguradoras ao mesmo tempo."),
    ("comparacao", "Comparação transparente",
     "Mostramos lado a lado o que cada opção cobre e quanto custa."),
    ("recomendacao", "Recomendação imparcial",
     "Indicamos o que faz mais sentido para você, e não para a seguradora."),
    ("acompanhamento", "Acompanhamento",
     "Estamos com você da cotação à contratação e no pós-venda, inclusive em caso de sinistro."),
]


def build(t, seg):
    S = []

    # ------------------------------------------------------------------ capa
    S.append(cover_slide(
        t, "AUVP", "Seguros", "As melhores seguradoras do mercado,<br>comparadas para você.",
        ['<div class="sg-capa">%s</div>' % "".join(
            '<span>%s</span>' % icone(p) for p in PRODUTOS)],
        confid="", cls="sg-cv"))

    # ------------------------------------------------------- como trabalhamos
    S.append(slide(t, "Como trabalhamos", 2, """<h1 class="t">Não perca dinheiro com seguro.</h1>
<div class="center">
  <div class="sg-cmp">
    <p class="mut">Quem contrata seguro direto com uma única seguradora fica com opções limitadas e
    dificilmente sabe se está pagando o preço justo pela cobertura certa.</p>
    %(unico)s
    <p><strong>Na AUVP Seguros, fazemos esse trabalho por você:</strong> cotamos nas principais seguradoras e
    operadoras do mercado, comparamos coberturas, condições e preços, e apresentamos a opção com o
    melhor custo-benefício para o seu momento de vida.</p>
    %(amplo)s
  </div>
  <ol class="sg-trilha">%(pilares)s</ol>
</div>
<div class="note"><p>Integrada ao ecossistema financeiro da AUVP, cada decisão de proteção
conversa com seus investimentos e com a construção do seu patrimônio.</p></div>""" % dict(
        unico=diagrama_unico(), amplo=diagrama_amplo(),
        pilares="".join('<li><span class="sg-bola">%s</span><h4>%s</h4><p>%s</p></li>' % (
            icone(i), a, b) for i, a, b in PILARES)),
        data=False, rodape=t["nome_full"]))

    # ----------------------------------------------------------------- vida
    S.append(vida(t, 3, "Seguro de Vida", "vida", [
        "Comparamos as principais seguradoras de vida do mercado para encontrar a combinação "
        "ideal entre capital, coberturas e preço, sem pagar por coberturas que você não precisa.",
        "O seguro de vida protege a família e o patrimônio contra imprevistos. Ele garante "
        "recursos para manter o padrão de vida e preservar o legado construído.",
    ], "Principais coberturas", [
        ("morte", "Morte"),
        ("invalidez", "Invalidez por acidente ou doença"),
        ("doencas", "Doenças graves"),
        ("diaria", "Diária por incapacidade temporária"),
        ("cirurgia", "Cirurgias"),
        ("internacao", "Internação hospitalar"),
    ]))

    # ----------------------------------------------------------------- auto
    S.append(auto(t, 4, "Seguro Auto", "auto", [
        "O preço do seguro auto pode variar muito de uma seguradora para outra para o mesmo carro "
        "e o mesmo motorista. Por isso, cotamos nas principais seguradoras e trazemos a melhor "
        "relação entre cobertura e preço para o seu perfil de uso.",
    ], "Principais coberturas", [
        ("roubo", "Colisão, roubo e furto"),
        ("terceiros", "Danos a terceiros (materiais e corporais)"),
        ("assistencia", "Assistência 24h e guincho"),
        ("reserva", "Carro reserva"),
        ("vidros", "Vidros, faróis e retrovisores"),
    ]))

    # ------------------------------------------------------- rc profissional
    S.append(rc(t, 5, "RC Profissional para Médicos", "medico", [
        "Cotamos nas seguradoras especializadas em Responsabilidade Civil Profissional e "
        "comparamos limites, coberturas e preço, para que o médico tenha a proteção adequada à "
        "sua especialidade pagando o justo.",
        "O seguro protege o patrimônio e a carreira do médico contra reclamações e processos de "
        "pacientes, mesmo quando ele age corretamente.",
    ], "Principais coberturas", [
        ("defesa", "Custos de defesa jurídica e honorários advocatícios"),
        ("indenizacao", "Indenizações por danos materiais, corporais e morais a pacientes"),
        ("acordos", "Acordos judiciais e extrajudiciais"),
        ("pericias", "Despesas com perícias"),
    ]))

    # --------------------------------------------------------------- saúde
    S.append(saude(t, 6, "Planos de Saúde", "saude", [
        "Cotamos nas principais operadoras de saúde e comparamos rede credenciada, abrangência, "
        "coparticipação e mensalidade, para encontrar o plano com o melhor custo-benefício para "
        "você, sua família ou sua empresa.",
    ], "Modalidades", [
        ("familia", "Individual e familiar"),
        ("empresa", "Empresarial"),
    ]))

    return S
