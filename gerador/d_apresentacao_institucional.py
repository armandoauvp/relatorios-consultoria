# -*- coding: utf-8 -*-
"""Apresentação institucional da consultoria, a versão curta.

Substitui o deck de 16 páginas feito no Illustrator ("apresentação consultoria
2026"), que os consultores achavam engessado: era a casa inteira contada em
sequência, e na reunião o consultor pulava metade. Aqui ficam só as páginas que
eles usam de fato — capa, quem somos, na mídia, o time e os benefícios — e entram
três ideias tiradas do material do Clube do Valor: a roda de soluções em volta
do patrimônio, a recomendação chegando no celular do cliente e o cashback
mostrado como comparação, e não como parágrafo.

É material para mandar e para projetar, e é da casa, não de quem apresenta:
não tem data, assinatura, nome de cliente nem contato de consultor. Qualquer
consultor usa o mesmo arquivo, sem preencher nada.
"""
from layout import *
from layout import _b64  # noqa: F401  (nome privado não vem no import *)


# As fotos são da casa, e não espaço de imagem: o prêmio do BTG e os recortes de
# imprensa são os mesmos em toda apresentação. Saem do PDF do deck anterior; o
# fundo cinza dos recortes foi levado ao branco para assentar no papel do slide.
FOTO_PREMIO = "assets/institucional/premio-btg.jpg"
FOTO_MIDIA = "assets/institucional/na-midia.jpg"


def olho(t, cls="ai-olho"):
    """Só o olho da marca, sem a palavra. O viewBox recorta o desenho do logo
    completo; o resto do arquivo fica fora da caixa e não aparece."""
    return '<span class="%s">%s</span>' % (cls, load_svg(t["logo"], "ey", viewbox="-8 8 351 224"))


def lamina(t, sec, body, dark=False, cls="", fundo=""):
    """O slide do sistema sem a data no cabeçalho. `fundo` entra antes do
    conteúdo, para foto e grafismo ficarem por baixo do texto."""
    return """<section class="slide%(dk)s%(cls)s">
  %(fundo)s%(grain)s
  <div class="in">
    <header class="pg-head">
      <div class="sec">%(sec)s</div>
      <div class="rt">%(logo)s</div>
    </header>
    <div class="pg-body">
%(body)s
    </div>
    <footer class="pg-foot"><span class="no">00</span><span>%(confid)s</span></footer>
  </div>
</section>""" % dict(dk=" dark" if dark else "", cls=(" " + cls) if cls else "",
                     fundo=fundo, grain='<div class="grain"></div>' if dark else "",
                     sec=sec, logo=logo_svg(t, 6.3, ink=not dark), body=body, confid=CONFID)


# ------------------------------------------------------------------ conteúdo

TRAJETORIA = [
    ("2020", "nasce a AUVP, como escola de investimentos"),
    ("+50 mil", "alunos formados na maior escola de investimentos do Brasil"),
    ("360°", "um ecossistema financeiro completo, da educação à gestão patrimonial"),
    ("1º lugar", "no ranking do BTG Pactual, pelo segundo ano consecutivo"),
]

# O fecho recapitula o deck em quatro números, já que não leva contato: é o
# que o cliente fica olhando enquanto a conversa segue.
# Cada número vem com um desenho pequeno que retoma o slide de onde ele saiu:
# o pódio do ranking, a grade do processo seletivo, a órbita das soluções e as
# barras do cashback. Em todos, o dourado marca o mesmo papel: o destaque.
_B = 'fill="#fff" fill-opacity=".32"'
_O = 'fill="#EFBF4F"'
MINI = {
    "podio": ('<rect x="3" y="21" width="10.5" height="15" rx="1" %s/>'
              '<rect x="14.75" y="9" width="10.5" height="27" rx="1" %s/>'
              '<rect x="26.5" y="25" width="10.5" height="11" rx="1" %s/>'
              '<path d="M3 36.5h34" stroke="#fff" stroke-opacity=".5" stroke-width=".6"/>') % (_B, _O, _B),
    "grade": "".join('<circle cx="%g" cy="%g" r="%g" %s/>' % (
                 5 + c * 5, 5 + r * 5, 1.7 if (c, r) == (4, 2) else 1.25,
                 _O if (c, r) == (4, 2) else _B) for r in range(7) for c in range(7)),
    "orbita": ('<circle cx="20" cy="20" r="14" fill="none" stroke="#fff" stroke-opacity=".38" stroke-width=".6"/>'
               + "".join('<circle cx="%.2f" cy="%.2f" r="2.6" fill="#fff" fill-opacity=".85"/>' % (
                   20 + 14 * __import__("math").cos(__import__("math").radians(a)),
                   20 + 14 * __import__("math").sin(__import__("math").radians(a)))
                   for a in (-60, 0, 60, 120, 180, 240))
               + '<circle cx="20" cy="20" r="6.5" %s/>' % _O),
    "barras": ('<rect x="3" y="11" width="24" height="6.5" rx="1" %s/>'
               '<rect x="3" y="23" width="24" height="6.5" rx="1" fill="#fff" fill-opacity=".85"/>'
               '<rect x="27.6" y="23" width="9.4" height="6.5" rx="1" %s/>') % (_B, _O),
}

RESUMO = [
    ("podio", "1º lugar", "no ranking do BTG Pactual, pelo segundo ano consecutivo"),
    ("grade", "0,01%", "dos candidatos passam no processo seletivo do nosso time"),
    ("orbita", "360°", "cuidado com o patrimônio inteiro, no Brasil e no exterior"),
    ("barras", "Cashback", "em renda fixa e no aluguel de ações, como saldo na sua conta"),
]

TIME = [
    ("Cultura", "Excelência começa na seleção. O processo prioriza alinhamento cultural, ética e "
                "compromisso com resultado."),
    ("Conhecimento", "O time é avaliado toda semana sobre o conteúdo técnico divulgado por Raul "
                     "Sena, CEO da AUVP Capital."),
    ("Treinamento", "Depois da seleção, um programa intensivo e contínuo: atendimento, "
                    "profundidade técnica e performance real. Não existe espaço para amadores."),
]

# A roda: o que a consultoria resolve em volta da carteira. Ordem no sentido
# horário a partir do alto à direita; os três primeiros ficam à direita da roda.
SOLUCOES = [
    ("Crédito", "Soluções alinhadas ao seu planejamento patrimonial"),
    ("Holdings", "Estruturação familiar e empresarial"),
    ("Seguro de vida", "Com foco em otimizar a sucessão"),
    ("Câmbio", "Operações integradas ao ecossistema"),
    ("Planejamento tributário", "Consultoria tributária e planejamento de saída fiscal"),
    ("Internacional", "Offshore e acesso a mercados internacionais"),
]

NOTIFICACOES = [
    ("Toda semana", "Recomendações de renda fixa",
     "Os títulos que passaram pelo filtro de emissor, prazo e taxa nesta semana."),
    ("Todo mês", "Relatório mensal da carteira",
     "Onde seu patrimônio está, o que rendeu e o que mudou no mês."),
    ("Todo mês", "Relatório macroeconômico",
     "O cenário do mês e o que ele muda, ou não, na sua estratégia."),
]

BENEFICIOS = [
    ("Isenção de taxa de corretagem",
     "Operações sem custo de corretagem, para você maximizar seus rendimentos."),
    ("Cashback em renda fixa",
     "Parte do retorno da renda fixa volta para você em forma de saldo."),
    ("Cashback de aluguel de ações",
     "Além do rendimento habitual, parte do valor gerado pelo aluguel das suas ações volta em saldo."),
    ("Conta internacional gratuita",
     "Sem taxa de abertura ou manutenção, para investir, transferir e movimentar recursos no exterior."),
]


# ------------------------------------------------------------------ desenhos

def campo_pontos():
    """O filtro de 0,01% em duas grades. Dez mil pontos numa grade só viram
    textura cinza na tela; aqui a primeira grade tem cem pontos de cem
    candidatos cada, e um deles abre, como numa lupa, na segunda grade de cem —
    onde um ponto só acende. Um em cem, de um em cem: um em dez mil."""
    p, r = 4.0, 1.05             # passo e raio dos pontos, em unidades do viewBox
    ax, bx, y0 = 2.0, 68.0, 2.0  # canto das duas grades
    sel_c, sel_r = 7, 2          # a célula da primeira grade que abre na segunda
    lit_c, lit_r = 6, 4          # o ponto aceso da segunda grade

    def grade(x0, opac, aceso=None):
        out = []
        for lin in range(10):
            for col in range(10):
                cx, cy = x0 + col * p + p / 2, y0 + lin * p + p / 2
                if aceso == (col, lin):
                    out.append('<circle cx="%g" cy="%g" r="3.4" fill="none" stroke="#fff" stroke-opacity=".5" stroke-width=".3"/>'
                               '<circle cx="%g" cy="%g" r="%g" fill="#EFBF4F"/>' % (cx, cy, cx, cy, r * 1.25))
                else:
                    out.append('<circle cx="%g" cy="%g" r="%g" fill="#fff" fill-opacity="%g"/>' % (cx, cy, r, opac))
        return "".join(out)

    sx, sy = ax + sel_c * p, y0 + sel_r * p          # a célula escolhida
    lado = 10 * p
    return """<svg class="ai-pontos" viewBox="0 0 110 52" aria-label="Um aprovado em dez mil candidatos">
  <path d="M%(sx1)g %(sy)gL%(bx)g %(y0)gL%(bx)g %(yb)gL%(sx1)g %(sy1)gZ" fill="#fff" fill-opacity=".06"/>
  <line x1="%(sx1)g" y1="%(sy)g" x2="%(bx)g" y2="%(y0)g" class="lp"/>
  <line x1="%(sx1)g" y1="%(sy1)g" x2="%(bx)g" y2="%(yb)g" class="lp"/>
  %(ga)s
  <rect x="%(sx)g" y="%(sy)g" width="%(p)g" height="%(p)g" fill="none" stroke="#fff" stroke-width=".35"/>
  <rect x="%(bx)g" y="%(y0)g" width="%(lado)g" height="%(lado)g" fill="none" stroke="#fff" stroke-opacity=".35" stroke-width=".3"/>
  %(gb)s
  <text x="%(ta)g" y="49" class="lg"><tspan class="lgb">10 mil candidatos</tspan> · cada ponto, 100 pessoas</text>
  <text x="%(tb)g" y="49" class="lg"><tspan class="lgb">100 candidatos</tspan> · cada ponto, 1 pessoa</text>
</svg>""" % dict(sx=sx, sy=sy, sx1=sx + p, sy1=sy + p, bx=bx, y0=y0, yb=y0 + lado, p=p, lado=lado,
                 ga=grade(ax, .55),
                 gb=grade(bx, .3, aceso=(lit_c, lit_r)),
                 ta=ax, tb=bx)


# Ícones das soluções, em traço, numa grade de 24 x 24.
ICONES = {
    "Crédito": '<rect x="3" y="6" width="18" height="12" rx="2"/><path d="M3 10.5h18M6.5 14.5h4"/>',
    "Holdings": '<path d="M3 21h18M5 21V9l7-5 7 5v12M9.5 12h1.5M13 12h1.5M9.5 16h1.5M13 16h1.5"/>',
    "Seguro de vida": '<path d="M12 3l7 3v5.5c0 4.6-3 8-7 9.5-4-1.5-7-4.9-7-9.5V6z"/><path d="M9 12.2l2.1 2.1 4-4.2"/>',
    "Câmbio": '<path d="M4 8.5h14.5M15 5l3.5 3.5L15 12M20 15.5H5.5M9 12l-3.5 3.5L9 19"/>',
    "Planejamento tributário": '<path d="M6 3h8l4 4v14H6z"/><path d="M14 3v4h4M9.5 17.5l5-6"/><circle cx="10" cy="12" r="1.1"/><circle cx="14" cy="17" r="1.1"/>',
    "Internacional": '<circle cx="12" cy="12" r="9"/><ellipse cx="12" cy="12" rx="3.8" ry="9"/><path d="M3 12h18M4.6 7.5h14.8M4.6 16.5h14.8"/>',
}


def roda(t):
    """O patrimônio no centro e as seis frentes em órbita, à mesma distância
    dele: nenhuma vale mais que a outra, e por isso todas têm a mesma cor. O
    anel de marcas entre o centro e a órbita é o mostrador dos 360°. Cada nó
    leva o ícone, e o nome fica ao lado dele, sem fio de ligação: o texto
    encosta no nó.

    Desenhado em milímetros numa caixa de 306 x 112 mm. O SVG traz o desenho;
    os textos são HTML posicionados nas mesmas coordenadas, para continuarem
    texto de verdade no PDF."""
    import math
    W, H = 306.0, 112.0
    cx, cy = W / 2, H / 2
    R, rn, rd = 44.0, 6.6, 21.0          # órbita, nó e disco central
    angulos = [-60, 0, 60, 120, 180, 240]  # sentido horário, a partir das 3 horas

    def pt(r, a):
        return cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a))

    marcas = []
    for k in range(0, 360, 6):
        r0, r1 = (26.2, 30.2) if k % 30 == 0 else (27.4, 29.4)
        (x0, y0), (x1, y1) = pt(r0, k), pt(r1, k)
        marcas.append('<line x1="%.2f" y1="%.2f" x2="%.2f" y2="%.2f"%s/>'
                      % (x0, y0, x1, y1, ' class="m30"' if k % 30 == 0 else ""))

    raios, nos, rot = [], [], []
    esc = 7.8 / 24                       # ícone de 7,8 mm dentro do nó
    for (titulo, desc), a in zip(SOLUCOES, angulos):
        nx, ny = pt(R, a)
        (sx, sy), (ex, ey) = pt(rd + 1.5, a), pt(R - rn - 1, a)
        raios.append('<line x1="%.2f" y1="%.2f" x2="%.2f" y2="%.2f"/>' % (sx, sy, ex, ey))
        nos.append('<circle cx="%.2f" cy="%.2f" r="%g" class="no"/>'
                   '<g class="ic" transform="translate(%.3f %.3f) scale(%.4f)">%s</g>'
                   % (nx, ny, rn, nx - 12 * esc, ny - 12 * esc, esc, ICONES[titulo]))
        direita = math.cos(math.radians(a)) > 0
        if direita:
            pos = "left:%.2fmm" % (nx + rn + 7)
        else:
            pos = "right:%.2fmm" % (W - (nx - rn - 7))
        rot.append('<div class="ai-rot %s" style="%s;top:%.2fmm"><h4>%s</h4><p>%s</p></div>'
                   % ("dir" if direita else "esq", pos, ny, titulo, desc))

    return """<div class="ai-roda" style="width:%(W)gmm;height:%(H)gmm">
  <svg viewBox="0 0 %(W)g %(H)g" class="ai-roda-svg">
    <defs><linearGradient id="ai-disco" x1="1" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#023620"/><stop offset="1" stop-color="#000"/></linearGradient></defs>
    <circle cx="%(cx)g" cy="%(cy)g" r="%(R)g" class="orbita"/>
    <g class="raios">%(raios)s</g>
    <g class="marcas">%(marcas)s</g>
    <circle cx="%(cx)g" cy="%(cy)g" r="%(rd)g" fill="url(#ai-disco)"/>
    %(nos)s
  </svg>
  <div class="ai-centro" style="left:%(cx)gmm;top:%(cy)gmm">%(olho)s<span>Seu<br>patrimônio</span></div>
  %(rot)s
</div>""" % dict(W=W, H=H, cx=cx, cy=cy, R=R, rd=rd, marcas="".join(marcas), raios="".join(raios),
                 nos="".join(nos), rot="".join(rot), olho=olho(t))


# Geometria do celular, em mm a partir do canto do slide. As chamadas da
# esquerda saem destes mesmos números, e por isso cada fio chega exatamente no
# meio da notificação dele.
CEL_X, CEL_Y = 165.5, 31.2           # caixa que recorta o aparelho
CEL_BORDA = 1.0 + 2.4 + 4.0          # margem + moldura + respiro da tela, na horizontal
CEL_TOPO = 0.5 + 2.4                 # margem + moldura, na vertical
LISTA_Y, NOTIF_H, NOTIF_GAP = 50.0, 22.0, 3.0
CHAMADA_X, FIO_X = 16.0, 84.0        # onde começam o texto e o fio


def celular(t):
    notif = "".join("""<div class="ai-notif">
        <div class="ai-app">%(olho)s<span>AUVP Capital</span><i>agora</i></div>
        <b>%(tit)s</b><p>%(txt)s</p>
      </div>""" % dict(olho=olho(t, "ai-app-ic"), tit=tit, txt=txt) for _, tit, txt in NOTIFICACOES)
    card_x = CEL_X + CEL_BORDA
    chamadas = []
    for i, (k, tit, _) in enumerate(NOTIFICACOES):
        y = CEL_Y + CEL_TOPO + LISTA_Y + NOTIF_H / 2 + i * (NOTIF_H + NOTIF_GAP)
        # o li fica no ponto onde o fio começa: o texto encosta nele pela
        # direita e o fio segue dali até a notificação
        chamadas.append('<li style="top:%.2fmm;left:%.2fmm"><span>%s</span><b>%s</b>'
                        '<i style="width:%.2fmm"></i></li>'
                        % (y, FIO_X - CHAMADA_X, k, tit, card_x - FIO_X))
    # O celular sangra pelo pé do slide, como no material de referência. Fica
    # numa caixa própria que termina na borda do slide e recorta o resto: assim
    # o aparelho não conta como conteúdo estourando a página.
    return """<div class="ai-cel-clip" style="left:%(cx)gmm;top:%(cy)gmm"><div class="ai-cel">
  <div class="ai-tela">
    <div class="ai-ilha"></div>
    <div class="ai-dia">Segunda-feira</div>
    <div class="ai-hora">08:30</div>
    <div class="ai-lista" style="top:%(ly)gmm">%(notif)s</div>
  </div>
</div></div>
<ol class="ai-chamadas" style="left:%(chx)gmm">%(cham)s</ol>""" % dict(
        cx=CEL_X, cy=CEL_Y, ly=LISTA_Y, notif=notif, chx=CHAMADA_X, cham="".join(chamadas))


def capa(t):
    """A capa com o mesmo cabeçalho e o mesmo pé dos slides de conteúdo: a
    marca e o rótulo não mudam de lugar quando se passa da capa para o resto."""
    return """<section class="slide dark ai-capa">
  <div class="grain"></div><div class="ai-graf-clip">%(graf)s</div>
  <div class="in">
    <header class="pg-head">
      <div class="sec">Consultoria</div>
      <div class="rt">%(logo)s</div>
    </header>
    <div class="pg-body">
      <div class="ai-capa-bloco">
        <div class="rule"></div>
        <h1 class="cv-t"><span class="lt">Conheça a </span>melhor consultoria do Brasil</h1>
        <div class="cv-sub">Gestão financeira transparente e completa</div>
      </div>
    </div>
    <footer class="pg-foot"><span></span><span>%(confid)s</span></footer>
  </div>
</section>""" % dict(graf=graf_arcos(GRAF_SLIDE_W, "bottom-right"), logo=logo_svg(t, 6.3),
                     confid=CONFID)


CHECK = ('<svg viewBox="0 0 24 24" class="ai-ck"><circle cx="12" cy="12" r="12"/>'
         '<path d="M6.8 12.4l3.4 3.3 7-7.2"/></svg>')


# ------------------------------------------------------------------ documento

def build(t, seg):
    S = []

    # 1. Capa — a frase do deck anterior, no desenho de capa do sistema.
    S.append(capa(t))

    # 2. Quem somos — o texto das páginas 2 e 3 do deck anterior, reduzido ao
    # que se lê em voz alta, e a história da casa virando uma linha de marcos.
    S.append(lamina(t, "Sobre nós", """<div class="ai-qs">
  <h1 class="t">Quem somos</h1>
  <p class="ai-lead">A maior consultoria de investimentos de Goiás e uma das mais relevantes do Brasil.</p>
  <p class="ai-txt">Atuamos de forma independente, com foco absoluto na geração de valor para nossos clientes.</p>
  <p class="ai-txt"><strong>A satisfação do cliente vem em primeiro lugar.</strong></p>
</div>
<ol class="ai-marcos">%s</ol>""" % "".join('<li><span class="n">%s</span><span class="l">%s</span></li>' % m
                                       for m in TRAJETORIA),
        dark=True, cls="ai-foto",
        fundo='<img class="ai-bg" alt="" src="data:image/jpeg;base64,%s"><div class="ai-veu"></div>'
              % _b64(FOTO_PREMIO)))

    # 3. Na mídia — os recortes de imprensa como estavam.
    S.append(lamina(t, "Sobre nós", """<h1 class="t">Na mídia</h1>
<p class="lead">O que a imprensa tem falado sobre a AUVP e sobre quem está por trás dela.</p>
<div class="ai-midia"><img alt="Reportagens sobre a AUVP no Entrelinhas, no JBr, no g1 e n'O Globo" src="data:image/jpeg;base64,%s"></div>"""
                    % _b64(FOTO_MIDIA)))

    # 4. O time — os três pilares da página 4, com o 0,01% desenhado: dez mil
    # pontos e um aceso diz o tamanho do filtro melhor do que a porcentagem.
    S.append(lamina(t, "Nosso time", """<h1 class="t">Você será atendido pelos melhores do mercado</h1>
<p class="lead">Quem cuida do seu patrimônio passou por um filtro rigoroso e segue em formação toda semana.</p>
<div class="ai-time">
  <div class="ai-filtro">
    %(pontos)s
    <div class="ai-filtro-tx">
      <div class="ai-big">0,01%%</div>
      <p>dos candidatos passam pelo nosso processo seletivo: um em cada dez mil.</p>
    </div>
  </div>
  <ol class="ai-pilares">%(pilares)s</ol>
</div>""" % dict(pontos=campo_pontos(),
                 pilares="".join('<li><span class="nb">%d</span><div><h4>%s</h4><p>%s</p></div></li>'
                                 % (i, a, b) for i, (a, b) in enumerate(TIME, start=1))),
        dark=True))

    # 5. Soluções 360° — a roda do Clube do Valor (pág. 14) com o conteúdo da
    # nossa página de soluções patrimoniais.
    S.append(lamina(t, "A consultoria", """<h1 class="t">Soluções patrimoniais 360°</h1>
<p class="lead">Além da carteira de investimentos, cuidamos de tudo o que mexe com o seu patrimônio, no Brasil e no exterior.</p>
<div class="ai-roda-box">%s</div>""" % roda(t)))

    # 6. Implementação — a recomendação chegando no celular (Clube do Valor,
    # pág. 16), com o que a consultoria de fato manda e com que frequência.
    S.append(lamina(t, "A consultoria", """<div class="ai-impl">
  <div class="ai-impl-tx">
    <h1 class="t">Implementação da estratégia</h1>
    <p class="lead">A estratégia não fica no papel. O que o seu consultor acompanha chega até você, no celular, no ritmo certo.</p>
  </div>
  <div class="ai-decide">
    <span class="ai-decide-k">Na prática</span>
    <p class="ai-decide-t">O consultor recomenda. Quem decide é sempre você.</p>
    <p class="ai-txt">Cada recomendação vem com o racional por trás, e o seu consultor está no WhatsApp para a dúvida que aparecer no caminho.</p>
  </div>
</div>""",
        dark=True, cls="ai-impl-sl", fundo=celular(t)))

    # 7. Benefícios — os quatro da página 12, com o cashback mostrado como
    # comparação (Clube do Valor, pág. 18). Sem números: o cashback varia por
    # título, e um exemplo com taxa inventada seria lido como promessa.
    S.append(lamina(t, "Benefícios", """<h1 class="t">Benefícios exclusivos AUVP</h1>
<p class="lead">Ao investir com a AUVP Capital, você acessa vantagens que fazem o seu patrimônio render mais.</p>
<div class="ai-bn-corpo"><div class="ai-cash">
  <div class="ai-cash-tx">
    <span class="eyebrow">Cashback na prática</span>
    <h3>O mesmo título de renda fixa, comprado por dois caminhos</h3>
    <p class="legal">O cashback é aplicado conforme novas aplicações em títulos disponíveis na plataforma e varia com o valor investido, a taxa contratada e o emissor.</p>
  </div>
  <div class="ai-barras">
    <div class="ai-barra">
      <span class="ai-barra-k">Na corretora, no banco ou com assessor comissionado</span>
      <div class="ai-trilho"><span class="b1">Rendimento do título</span></div>
    </div>
    <div class="ai-barra">
      <span class="ai-barra-k"><strong>Com a AUVP Capital</strong></span>
      <div class="ai-trilho"><span class="b1 b-marca">Rendimento do título</span><span class="b2">%(ck)s+ cashback</span></div>
      <span class="ai-cb-nota">volta para a sua conta como saldo</span>
    </div>
  </div>
</div>
<div class="ai-benef">%(bens)s</div></div>""" % dict(
        ck=CHECK,
        bens="".join('<div><h4>%s<span>%s</span></h4><p>%s</p></div>' % (CHECK, a, b) for a, b in BENEFICIOS))))

    # 8. Fecho — a chamada da última página do deck anterior. Sem contato: o
    # documento é da casa, e quem apresenta já está na conversa.
    S.append(lamina(t, "Faça parte", """<div class="ai-fim">
  <div class="rule"></div>
  <h1 class="ai-fim-t">Pronto para dar o próximo passo?</h1>
  <p class="ai-txt">Fale com o seu consultor e entenda por que somos a melhor consultoria do Brasil para você.</p>
</div>
<span class="eyebrow ai-resumo-k">Por que a AUVP Capital</span>
<div class="ai-resumo">%s</div>""" % "".join(
        '<div class="ai-rs"><svg viewBox="0 0 40 40" class="ai-rs-ic">%s</svg>'
        '<div><span class="n">%s</span><span class="l">%s</span></div></div>' % (MINI[k], n, l)
        for k, n, l in RESUMO) + """
<p class="legal ai-fim-legal">Material de caráter informativo, que não constitui oferta nem recomendação individualizada. Benefícios sujeitos a elegibilidade e às condições vigentes; rentabilidade passada não garante rentabilidade futura.</p>""",
        dark=True, cls="ai-fecho", fundo='<div class="ai-graf-clip">%s</div>' % graf_arcos(GRAF_SLIDE_W, "top-right")))

    return S


CSS = """
/* ================= apresentação institucional (curta) ================= */
.ai-txt{font-size:11pt;line-height:1.55;color:var(--ink-2);text-align:left}
.slide.dark .ai-txt{color:rgba(255,255,255,.82)}
.slide .lead{text-align:left}

/* foto de fundo com véu escuro, como o "Quem somos" do deck anterior */
.slide.ai-foto{background:#000}
.ai-bg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:70% 50%;z-index:0}
.ai-veu{position:absolute;inset:0;z-index:1;
  background:linear-gradient(90deg,rgba(0,0,0,.96) 0%,rgba(0,0,0,.88) 42%,rgba(0,0,0,.35) 72%,rgba(0,0,0,.1) 100%)}
.slide.ai-foto .grain{z-index:2}
/* overlay de foto é sempre preto; o slide também */
.slide.ai-foto{background:#000}
.ai-qs{max-width:178mm}
.ai-qs .ai-txt{margin:0 0 2mm;font-size:12pt}
.ai-lead{font-size:22pt;line-height:1.25;font-weight:700;margin:2mm 0 6mm;text-align:left;letter-spacing:-.01em}
.ai-marcos{list-style:none;margin:auto 0 4mm;padding:0;display:grid;grid-template-columns:repeat(4,1fr);
  column-gap:8mm;width:225mm}
.ai-marcos li{position:relative;padding-top:9mm;margin:0;text-align:left}
.ai-marcos li::before{content:"";position:absolute;left:0;right:-8mm;top:2mm;height:1px;background:rgba(255,255,255,.35)}
.ai-marcos li:last-child::before{right:0}
.ai-marcos li::after{content:"";position:absolute;left:0;top:.5mm;width:3mm;height:3mm;border-radius:50%;background:#fff}
.ai-marcos li:last-child::after{background:var(--accent)}
.ai-marcos .n{display:block;font-size:24pt;font-weight:800;line-height:1;letter-spacing:-.02em;color:#fff}
.ai-marcos .l{display:block;margin-top:2.5mm;font-size:9.5pt;line-height:1.4;color:rgba(255,255,255,.8)}

/* na mídia */
.ai-midia{flex:1 1 auto;min-height:0;display:flex;align-items:center;justify-content:center}
.ai-midia img{display:block;max-width:100%;max-height:100%;height:auto}

/* o time */
.ai-time{flex:1 1 auto;min-height:0;display:grid;grid-template-columns:150mm 1fr;gap:18mm;align-items:center}
.ai-filtro{display:flex;flex-direction:column;gap:7mm}
.ai-pontos{width:150mm;height:auto;display:block;overflow:visible}
.ai-pontos .lp{stroke:#fff;stroke-opacity:.35;stroke-width:.3}
.ai-pontos .lg{font-family:'Anek Latin',sans-serif;font-size:2.5px;fill:rgba(255,255,255,.62)}
.ai-pontos .lgb{font-weight:700;fill:#fff}
.ai-filtro-tx{display:flex;align-items:center;gap:7mm}
.ai-filtro-tx p{max-width:70mm}
.ai-big{font-size:46pt;font-weight:800;line-height:1;letter-spacing:-.03em;color:#fff}
.ai-filtro-tx p{margin:0;font-size:10.5pt;line-height:1.5;color:rgba(255,255,255,.82);text-align:left}
.ai-pilares{list-style:none;margin:0;padding:0;position:relative}
/* o trilho liga um número ao seguinte e para no último, em vez de seguir solto pelo texto */
.ai-pilares li:not(:last-child)::after{content:"";position:absolute;left:4.5mm;top:9mm;bottom:-8mm;width:1px;background:rgba(255,255,255,.3)}
.ai-pilares li{position:relative;display:grid;grid-template-columns:9mm 1fr;gap:5mm;margin:0 0 8mm}
.ai-pilares li:last-child{margin-bottom:0}
.ai-pilares .nb{width:9mm;height:9mm;border-radius:50%;background:#fff;color:var(--brand);
  display:flex;align-items:center;justify-content:center;font-weight:800;font-size:11pt;position:relative;z-index:1}
.ai-pilares h4{margin:1.2mm 0 1.5mm;font-size:13pt;font-weight:700}
.ai-pilares p{margin:0;font-size:9.8pt;line-height:1.5;color:rgba(255,255,255,.8);text-align:left}

/* a roda */
.ai-roda-box{flex:1 1 auto;min-height:0;display:flex;align-items:center;justify-content:center}
.ai-roda{position:relative;flex:0 0 auto}
.ai-roda-svg{position:absolute;inset:0;width:100%;height:100%;overflow:visible}
.ai-roda .orbita{fill:none;stroke:#C9D1CC;stroke-width:.35}
.ai-roda .raios line{stroke:#C9D1CC;stroke-width:.35}
.ai-roda .marcas line{stroke:#9BA29D;stroke-width:.3}
.ai-roda .marcas line.m30{stroke:var(--brand);stroke-width:.45}
.ai-roda .no{fill:var(--brand)}
.ai-roda .ic *{fill:none;stroke:#fff;stroke-width:1.75;stroke-linecap:round;stroke-linejoin:round}
.ai-centro{position:absolute;transform:translate(-50%,-50%);display:flex;flex-direction:column;align-items:center;gap:1.2mm;
  color:#fff;text-align:center;font-size:8pt;font-weight:700;letter-spacing:.08em;text-transform:uppercase;line-height:1.2}
.ai-olho{display:block;width:13mm}
.ai-olho svg,.ai-app-ic svg{display:block;width:100%;height:auto}
/* título e descrição são um bloco só, centrado na altura do nó */
.ai-rot{position:absolute;width:74mm;transform:translateY(-50%)}
.ai-rot.esq{text-align:right}
.ai-rot h4{margin:0 0 1mm;font-size:12pt;line-height:6.4mm;font-weight:700}
.ai-rot p{margin:0;font-size:9.2pt;line-height:1.4;color:var(--ink-2);text-align:inherit}

/* implementação: o celular */
.ai-impl{flex:1 1 auto;position:relative}
.ai-impl-tx{width:128mm}
/* as chamadas são do mesmo plano do celular: coordenadas do slide, não do texto */
.ai-chamadas{list-style:none;margin:0;padding:0;position:absolute;top:0;z-index:4}
.ai-chamadas li{position:absolute;margin:0;height:0;width:0}
/* alinhados à direita, encostando no começo do fio */
.ai-chamadas b{position:absolute;right:4mm;top:0;transform:translateY(-50%);white-space:nowrap;text-align:right;
  font-size:13pt;font-weight:600;line-height:6mm;color:#fff}
.ai-chamadas span{position:absolute;right:4mm;bottom:3.8mm;white-space:nowrap;text-align:right;
  font-size:7.6pt;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:rgba(255,255,255,.65)}
.ai-chamadas i{position:absolute;left:0;top:-.5px;height:1px;background:#fff}
.ai-chamadas i::after{content:"";position:absolute;right:-1.6mm;top:-1.6mm;width:3.2mm;height:3.2mm;border-radius:50%;background:#fff}
.ai-cel-clip{position:absolute;bottom:0;width:78mm;overflow:hidden;z-index:3}
.ai-cel{position:relative;margin:.5mm 1mm 0;width:76mm;height:178mm;border-radius:11mm;background:#0A0D0B;
  padding:2.4mm;box-shadow:0 0 0 .35mm rgba(255,255,255,.28)}
.ai-tela{position:relative;height:100%;border-radius:9mm;overflow:hidden;padding:5mm 4mm;
  background:linear-gradient(165deg,#E8F1EB 0%,#B9D6C3 38%,#5E9A78 78%,#2F6A4B 100%)}
.ai-ilha{width:24mm;height:6mm;border-radius:4mm;background:#0A0D0B;margin:0 auto 6mm}
.ai-dia{text-align:center;font-size:10.5pt;font-weight:600;color:#1C3A2B}
.ai-hora{text-align:center;font-size:40pt;font-weight:700;line-height:1;color:#123323;letter-spacing:-.02em;margin:1mm 0 7mm}
.ai-lista{position:absolute;left:4mm;right:4mm;display:flex;flex-direction:column;gap:3mm}
.ai-notif{background:rgba(255,255,255,.82);border-radius:4mm;padding:2.6mm 3.2mm;color:#12160F;height:22mm;overflow:hidden}
.ai-app{display:flex;align-items:center;gap:1.6mm;font-size:6.6pt;font-weight:600;letter-spacing:.04em;text-transform:uppercase;color:#4A5248;margin-bottom:1mm}
.ai-app i{margin-left:auto;font-style:normal;text-transform:none;letter-spacing:0;color:#7E8A84}
.ai-app-ic{display:flex;align-items:center;justify-content:center;width:5mm;height:5mm;border-radius:1.3mm;background:#000;padding:.8mm}
.ai-notif b{display:block;font-size:9pt;line-height:1.25}
.ai-notif p{margin:.6mm 0 0;font-size:7.8pt;line-height:1.35;color:#4A5248;text-align:left}
.ai-decide{position:absolute;left:240mm;right:0;top:50%;transform:translateY(-50%)}
.ai-decide-k{display:block;font-size:7.6pt;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:rgba(255,255,255,.65);margin-bottom:2mm}
.ai-decide-t{font-size:16pt;font-weight:800;line-height:1.2;margin:0 0 4mm;text-align:left}
.ai-decide .ai-txt{font-size:9.6pt}
/* o pé passa por cima do celular, com o fundo do slide por trás */
.slide.ai-impl-sl .pg-foot{position:relative;z-index:4}

/* benefícios */
.ai-cash{display:grid;grid-template-columns:92mm 1fr;gap:14mm;align-items:center;
  padding:6mm 0;border-top:1px solid var(--line);border-bottom:1px solid var(--line)}
.ai-cash-tx h3{margin:0 0 3mm;font-size:13pt;line-height:1.3}
.ai-cash-tx .legal{margin:0;font-size:8.2pt;text-align:left}
.ai-barras{display:flex;flex-direction:column;gap:5mm}
.ai-barra-k{display:block;font-size:9pt;color:var(--ink-2);margin-bottom:1.5mm}
.ai-barra-k strong{color:var(--ink)}
.ai-trilho{display:flex;height:11mm}
.ai-trilho span{display:flex;align-items:center;font-size:9pt;font-weight:700;padding:0 4mm;white-space:nowrap}
.ai-trilho .b1{width:72%;background:#DDE3DF;color:var(--ink);border-radius:1.2mm}
.ai-trilho .b1.b-marca{background:var(--brand);color:#fff;border-radius:1.2mm 0 0 1.2mm}
.ai-trilho .b2{width:20%;background:var(--accent);color:#12160F;border-radius:0 1.2mm 1.2mm 0;gap:1.6mm}
.ai-trilho .b2 .ai-ck{width:4.4mm;height:4.4mm}
.ai-trilho .b2 .ai-ck circle{fill:#12160F}
.ai-trilho .b2 .ai-ck path{stroke:var(--accent)}
.ai-cb-nota{display:block;margin:1.5mm 0 0 72%;padding-left:4mm;font-size:8.4pt;color:var(--ink-2)}
.ai-ck{width:6mm;height:6mm;flex:0 0 auto;display:block}
.ai-ck circle{fill:var(--brand)}
.ai-ck path{fill:none;stroke:#fff;stroke-width:2.4;stroke-linecap:round;stroke-linejoin:round}
.ai-bn-corpo{flex:1 1 auto;display:flex;flex-direction:column;justify-content:space-evenly;gap:8mm}
.ai-benef{display:grid;grid-template-columns:repeat(4,1fr);gap:6mm}
.ai-benef>div{background:var(--soft);border-radius:2mm;padding:5mm 5mm 5.5mm}
.ai-benef h4{display:flex;align-items:center;gap:2.5mm;margin:0 0 2mm;font-size:11pt;line-height:1.2}
.ai-benef p{margin:0;font-size:9pt;line-height:1.45;color:var(--ink-2);text-align:left}

/* fecho */
.slide.ai-fecho .graf{z-index:2}
.ai-fim{flex:1 1 auto;display:flex;flex-direction:column;justify-content:center;max-width:200mm}
.ai-fim .rule{width:50.3mm;margin-bottom:10mm}
.ai-resumo-k{margin:0 0 2mm;color:rgba(255,255,255,.65)}
/* o resumo do fecho: quatro painéis, cada um com o desenho do slide de onde
   o número saiu e o número ao lado dele */
.ai-resumo{display:grid;grid-template-columns:repeat(4,1fr);gap:5mm;margin:0 0 8mm}
.ai-rs{display:flex;align-items:center;gap:4.5mm;padding:5mm 5mm;border-radius:2.5mm;
  background:rgba(255,255,255,.06)}
.ai-rs-ic{width:17mm;height:17mm;flex:0 0 auto;display:block}
.ai-rs .n{display:block;font-size:19pt;font-weight:800;line-height:1;letter-spacing:-.02em;color:#fff}
.ai-rs .l{display:block;margin-top:1.8mm;font-size:8.6pt;line-height:1.38;color:rgba(255,255,255,.78)}
/* no fecho o grafismo é só textura: mais apagado que o padrão do sistema */
.slide.ai-fecho .graf{opacity:.2}
.ai-fim-t{margin:0 0 5mm;font-size:36pt;font-weight:800;line-height:1.05;letter-spacing:-.02em;text-transform:uppercase}
.ai-fim .ai-txt{font-size:12.5pt;max-width:150mm}
.ai-fim-legal{margin:0;font-size:7.6pt;max-width:165mm;text-align:left}
/* capa: o mesmo cabeçalho e pé dos outros slides, para a marca não mudar de lugar */
/* O grafismo sangra pelo pé do slide. Solto, o Chromium o empurra para a
   página seguinte na impressão e ele some da capa; dentro de uma caixa do
   tamanho do slide, recortada, ele fica onde está. */
.ai-graf-clip{position:absolute;inset:0;overflow:hidden;z-index:2;pointer-events:none}
.ai-capa .pg-body{justify-content:center}
.ai-capa-bloco{margin:auto 0}
.ai-capa .rule{width:50.3mm;margin-bottom:14mm}
.ai-capa .cv-sub{margin-top:4mm}

"""
