# -*- coding: utf-8 -*-
"""Relatório macroeconômico.

Segue o formato que o time fecha todo mês: um resumo executivo, o painel de
indicadores, os destaques, as análises do mês, a posição da carteira, a
expectativa por classe, o fechamento, riscos e oportunidades, a agenda e a
síntese. É texto corrido: uma seção começa logo depois da outra, e o que não
cabe numa página continua na seguinte (a ferramenta reparte).

Há dois tipos de seção. As da casa têm título fixo, porque existem todo mês:
panorama, destaques, carteira, classes, fechamento, riscos, perspectivas e
síntese. As de análise têm título editável, porque o assunto muda: num mês é a
trajetória fiscal, no outro a eleição ou o crédito. Análise que o mês não pede
fica em branco e some na exportação; análise que falta se monta com os blocos.

O sumário não tem página escrita à mão. Cada seção marca o seu título com
`data-toc`, e a ferramenta refaz o sumário depois de repaginar, com a página em
que cada título caiu.
"""
from layout import *

# Quem assina o relatório. É o time de análise, o mesmo em todo segmento.
ANALISTA = "Douglas Ribeiro"
COORDENADOR = "Manoel Neto"

PUBLICO = {"consultoria": "da Consultoria AUVP", "alta-renda": "do segmento Alta Renda",
           "private": "do segmento Private Banking", "assessoria": "da Assessoria AUVP"}

# Os oito números do painel. O rótulo vem escrito, porque é o mesmo todo mês;
# o valor e a nota são do mês.
PAINEL = ["Selic", "Ibovespa", "IPCA do mês", "Dólar", "Dívida bruta/PIB",
          "Déficit nominal (12 meses)", "Dívida pública dos EUA", "IMA-B (NTN-B)"]

# As classes da expectativa e quantos itens cada uma costuma ter.
CLASSES = [("Renda fixa Brasil", "rf", 4), ("Renda variável Brasil", "rv", 3),
           ("Fundos imobiliários", "fii", 2), ("Internacional", "intl", 3), ("Cripto", "cripto", 1)]

FECHAMENTO = [("CDI", "cdi"), ("Ibovespa", "ibov"), ("IMA-B (NTN-B)", "imab"), ("IFIX", "ifix"),
              ("Dólar (USD/BRL)", "dolar"), ("IPCA", "ipca")]


def _titulo(chave, dica, padrao=None, rotulo=None, fixo=None):
    """O título de uma seção, marcado para o sumário. `rotulo` troca o nome no
    cabeçalho corrido a partir desta seção."""
    texto = fixo if fixo is not None else ph(chave, dica, padrao=padrao)
    r = ' data-rotulo="%s"' % rotulo if rotulo else ""
    return '<h1 class="t" data-toc="%s"%s>%s</h1>' % (chave, r, texto)


def _analise(k, n_sub, lead=True, tabela=False):
    """Uma seção de análise do mês: título, linha de abertura e subtítulos com
    parágrafo. O que ficar em branco sai."""
    partes = [_titulo("analise_%s_titulo" % k, "Título da análise")]
    if lead:
        partes.append('<p class="lead">%s</p>' % ph("analise_%s_lead" % k, "Uma linha de abertura"))
    for i in range(1, n_sub + 1):
        partes.append("<h2>%s</h2>" % ph("analise_%s_%d_subtitulo" % (k, i), "Subtítulo, se houver"))
        partes.append('<p class="small">%s</p>' % ph("analise_%s_%d_texto" % (k, i)))
    if tabela:
        partes.append(table([ph("analise_%s_col_%d" % (k, c)) for c in (1, 2, 3, 4)],
                            [[ph("analise_%s_%d_%d" % (k, l, c)) for c in (1, 2, 3, 4)]
                             for l in (1, 2, 3, 4, 5)],
                            caption=ph("analise_%s_fonte" % k, "Fonte da tabela"), sm=True))
    return "\n".join(partes)


def build(t, seg):
    set_date_ph("mes_referencia")
    P = []
    mes, fech = ph("mes_referencia"), ph("mes_fechamento", "O mês analisado. Ex.: Agosto")

    P.append(cover_a4(t, "Relatório", "Macroeconômico", "Cenário", "e Mercados",
                      [x for x in [t["rotulo"], "Elaborado por " + ANALISTA,
                       ph("registro_analista"), mes] if x], grafismo=2))

    # As seções, na ordem do relatório, com a página em que caem no modelo em
    # branco. É só o ponto de partida do sumário: preenchido, o texto cresce, e
    # a ferramenta recalcula.
    # O número é o do rodapé do modelo, que não conta a capa.
    secoes = [("Panorama macroeconômico", 2), ("Principais destaques", 2),
              ("Análise do mês: Brasil", 3), ("Análise do mês", 3), ("Análise do mês", 4),
              ("Panorama global", 4), ("Análise do mês", 5),
              ("Como a carteira da AUVP está posicionada", 5),
              ("Expectativa para classes de ativos", 6), ("Fechamento do mês", 7),
              ("Principais riscos e oportunidades", 7), ("Perspectivas para o mês", 8),
              ("Síntese executiva e posicionamento recomendado", 9), ("Notas e avisos", 10)]

    P.append(page_a4(t, "Resumo executivo", 2, """<span class="eyebrow">Relatório macro mensal</span>
<h1 class="t">%(tit)s</h1>
<p class="lead">Análise estratégica de cenário macroeconômico, fluxo de capital, geopolítica e
posicionamento de portfólio para investidores %(pub)s.</p>
<p class="small">%(res)s</p>
<h2>Neste relatório</h2>
<ol class="toc" data-auto="">%(toc)s</ol>""" % dict(
        tit=ph("titulo_do_mes", "A frase que resume o mês"), pub=PUBLICO[seg],
        res=ph("resumo_executivo", "O mês em um parágrafo"),
        toc="".join('<li><span class="n">%02d</span><span>%s</span><span class="d"></span>'
                    '<span class="p">%02d</span></li>' % (i, n, pg)
                    for i, (n, pg) in enumerate(secoes, start=1)))))

    P.append(page_a4(t, "Panorama", 3, """%(t1)s
<p class="lead">Painel de indicadores, Brasil e EUA, fechamento de %(fech)s</p>
%(kpis)s
<div class="gap"></div>
<p class="legal">Fonte: %(fonte)s</p>
<div class="esp"></div>
%(t2)s
<p class="lead">As cinco mensagens que %(fech)s confirmou e que moldam %(mes)s</p>
<ol class="tl">%(dest)s</ol>""" % dict(
        t1=_titulo("panorama", "", fixo="Panorama macroeconômico"),
        t2=_titulo("destaques", "", fixo="Principais destaques"),
        fech=fech, mes=mes, fonte=ph("fonte_painel", "Ex.: BCB, IBGE, Tesouro Nacional, Bloomberg"),
        kpis=kpis([(ph("painel_%d_rotulo" % i, padrao=r), ph("painel_%d_valor" % i),
                    ph("painel_%d_nota" % i)) for i, r in enumerate(PAINEL, start=1)]),
        dest="".join("<li><h4>%s</h4><p>%s</p></li>" % (ph("destaque_%d_titulo" % i),
                                                       ph("destaque_%d_texto" % i))
                     for i in range(1, 6)))))

    # As análises do mês. Três formas, na ordem do relatório de referência: a
    # de subtítulos, a de cenários em tabela e a de linha de abertura.
    P.append(page_a4(t, "Brasil", 4, """%(a1)s
<div class="esp"></div>
%(a2)s""" % dict(a1=_analise("brasil", 2, lead=False).replace(
                     'data-toc="analise_brasil_titulo"',
                     'data-toc="analise_brasil_titulo" data-rotulo="Brasil"', 1),
                 a2=_analise("tema1", 1, tabela=True))))

    P.append(page_a4(t, "Brasil", 5, """%(a3)s
<div class="esp"></div>
%(g)s""" % dict(a3=_analise("tema2", 2),
                g=_titulo("global_titulo", "Título do panorama global",
                          padrao="Panorama global", rotulo="Internacional")
                  + "".join('\n<h2>%s</h2>\n<p class="small">%s</p>'
                            % (ph("global_%d_subtitulo" % i), ph("global_%d_texto" % i))
                            for i in (1, 2, 3)))))

    P.append(page_a4(t, "Internacional", 6, """%(a4)s
<div class="esp"></div>
%(t)s
<p class="lead">%(lead)s</p>
%(tab)s""" % dict(
        a4=_analise("tema3", 0).replace('<p class="lead">', '<p class="lead">', 1)
           + '\n<p class="small">%s</p>\n<p class="small">%s</p>' % (
               ph("analise_tema3_texto_1"), ph("analise_tema3_texto_2")),
        t=_titulo("carteira", "", fixo="Como a carteira da AUVP está posicionada", rotulo="Carteira"),
        lead=ph("carteira_lead", "Ex.: o que sustenta as decisões deste mês"),
        tab=table(["Posição", "Racional"],
                  [[ph("pos_%d_posicao" % i), ph("pos_%d_racional" % i)] for i in range(1, 5)],
                  sm=True, widths=[30, 70]))))

    P.append(page_a4(t, "Carteira", 7, """%(t)s
<p class="lead">Estratégia de referência institucional, sem substituir a personalização por cliente.</p>
%(classes)s""" % dict(
        t=_titulo("classes", "", fixo="Expectativa para classes de ativos"),
        classes="\n".join("<h2>%s</h2>\n%s" % (nome, "\n".join(
            '<p class="small"><strong>%s</strong> %s</p>' % (
                ph("classe_%s_%d_rotulo" % (k, i), "Ex.: IPCA (40% da referência estrutural)"),
                ph("classe_%s_%d_texto" % (k, i))) for i in range(1, n + 1)))
            for nome, k, n in CLASSES))))

    P.append(page_a4(t, "Mercados", 8, """%(t1)s
<p class="lead">Desempenho acumulado no ano dos principais indicadores de referência</p>
%(tab)s
<div class="gap"></div>
<p class="legal">%(nota)s</p>
<div class="esp"></div>
%(t2)s
<p class="lead">%(lead)s</p>
<h2>Riscos no radar</h2>
%(riscos)s""" % dict(
        t1='<h1 class="t" data-toc="fechamento" data-rotulo="Mercados">Fechamento de %s</h1>' % fech,
        tab=table(["Indicador", "No mês", "Acumulado no ano"],
                  [[n, ph("fech_%s_mes" % k), ph("fech_%s_ano" % k)] for n, k in FECHAMENTO],
                  nums=[1, 2], sm=True),
        nota=ph("fechamento_nota", "Uma leitura curta dos números"),
        t2=_titulo("riscos", "", fixo="Principais riscos e oportunidades"),
        lead=ph("riscos_lead", "Ex.: cenários monitorados para o último trimestre"),
        riscos=_cartoes("risco", 5))))

    P.append(page_a4(t, "Mercados", 9, """<h2>Oportunidades</h2>
%(oport)s
<div class="esp"></div>
%(t)s
<p class="lead">Eventos críticos que definem o mês</p>
%(tab)s
<div class="gap"></div>
<p class="small">%(fecho)s</p>""" % dict(
        oport=_cartoes("oportunidade", 3),
        t='<h1 class="t" data-toc="perspectivas" data-rotulo="Agenda">Perspectivas para %s</h1>' % mes,
        tab=table(["Data", "Evento / indicador", "Por que importa"],
                  [[ph("ag_%d_data" % i), ph("ag_%d_evento" % i), ph("ag_%d_motivo" % i)]
                   for i in range(1, 6)], sm=True, widths=[16, 30, 54]),
        fecho=ph("perspectivas_texto", "O que a combinação desses eventos significa"))))

    P.append(page_a4(t, "Síntese", 10, """%(t)s
<p class="small">%(s1)s</p>
<p class="small">%(s2)s</p>
<p class="small">%(s3)s</p>""" % dict(
        t=_titulo("sintese", "", fixo="Síntese executiva e posicionamento recomendado"),
        s1=ph("sintese_1"), s2=ph("sintese_2"), s3=ph("sintese_3"))))

    P.append(page_a4(t, "Notas e avisos", 11, """%(t)s
<h2>Fontes</h2>
<div class="dl">
  <dt>Indicadores macro</dt><dd>%(f1)s</dd>
  <dt>Cenários e projeções</dt><dd>%(f2)s</dd>
</div>
<h2>Avisos legais</h2>
<p class="legal">%(disc)s</p>
<p class="legal">Este relatório tem caráter exclusivamente informativo e educacional e não constitui oferta, recomendação individualizada, proposta de investimento ou solicitação de compra ou venda de qualquer ativo. As opiniões refletem a leitura do time na data de fechamento e podem mudar sem aviso prévio. Projeções são exercícios sujeitos a erro e não representam promessa ou garantia de resultado.</p>
<p class="legal">Rentabilidade passada não representa garantia de rentabilidade futura. Antes de investir, avalie a adequação do produto ao seu perfil e leia os documentos oficiais de cada investimento. É proibida a reprodução, redistribuição ou compartilhamento total ou parcial deste documento sem autorização prévia e por escrito.</p>
<h2>Contato</h2>
<div class="dl">
  <dt>Analista responsável</dt><dd>%(an)s</dd>
  <dt>Registro</dt><dd>%(reg)s</dd>
  <dt>Coordenador responsável</dt><dd>%(coord)s</dd>
  <dt>E-mail</dt><dd>%(email)s</dd>
  <dt>Ouvidoria</dt><dd>%(ouv)s</dd>
  <dt>Razão social</dt><dd>%(razao)s</dd>
  <dt>CNPJ</dt><dd>%(cnpj)s</dd>
</div>""" % dict(
        t=_titulo("notas", "", fixo="Notas e avisos"),
        f1=ph("fonte_indicadores", "Ex.: BCB, IBGE, Tesouro Nacional, Bloomberg"),
        f2=ph("fonte_cenarios"),
        disc=ph("disclaimer_regulatorio", "Texto aprovado pelo compliance para este segmento"),
        an=ANALISTA, reg=ph("registro_analista"), coord=COORDENADOR,
        email=ph("email_contato"), ouv=ph("canal_ouvidoria"),
        razao=ph("razao_social"), cnpj=ph("cnpj"))))

    return P


def _cartoes(tipo, n):
    """Riscos e oportunidades: o tema, a leitura e a ação da carteira."""
    return '<div class="cards" style="--n:3">%s</div>' % "".join(
        '<div class="card"><h4>%s</h4><p>%s</p><p><strong>Ação.</strong> %s</p></div>' % (
            ph("%s_%d_titulo" % (tipo, i)), ph("%s_%d_texto" % (tipo, i)),
            ph("%s_%d_acao" % (tipo, i))) for i in range(1, n + 1))
