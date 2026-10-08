# -*- coding: utf-8 -*-
"""Wealth Planning Snapshot.

A fotografia patrimonial que a AUVP Wealth entrega depois da primeira leitura
de um caso. Era feita no Gamma, com a identidade da Wealth; passa a sair no
desenho do Private Banking, com a mesma estrutura de páginas.

Ao contrário da proposta, aqui quase tudo é do cliente: o perfil, os números,
as conclusões, quem está em cada núcleo do patrimônio. O que o modelo fixa é a
ordem da leitura — fotografia, conclusões, núcleos, tributação, sucessão,
governança, frentes e follow-up — e o que é posição da casa e vale para
qualquer caso: as regras da tributação de dividendos e altas rendas, os
critérios de comparação entre pessoa física e holding, os temas de governança
a examinar. Esse texto vem preenchido e continua sendo campo (`padrao`), para
quem escreve corrigir o que não se aplica e deixar o resto.

As listas têm mais linhas do que um caso costuma usar: a que ficar em branco
sai na exportação, com o marcador junto. As duas tabelas têm as linhas
numeradas (`ind_1_…`, `fr_1_…`), e a ferramenta acrescenta quantas mais forem
precisas. Página que não se aplica ao caso se desmarca na ferramenta.
"""
from layout import *

# Os indicadores da fotografia. Os rótulos são os que quase todo caso tem, e
# vêm escritos; os valores são sempre do cliente.
INDICADORES = [
    "Patrimônio brasileiro declarado",
    "Patrimônio no exterior",
    "Imóveis na pessoa física",
    "Imóveis em holding",
    "Patrimônio financeiro",
    "Previdência privada",
    "Renda mensal declarada",
    "Renda de aluguéis (PF)",
]

# Os quatro núcleos em que o patrimônio de uma família costuma se dividir.
NUCLEOS = [
    ("pf", "Pessoa física", "esq cima"),
    ("imob", "Estrutura imobiliária", "dir cima"),
    ("geracao", "Geração seguinte", "esq baixo"),
    ("empresas", "Empresas operacionais", "dir baixo"),
]

# O que a comparação entre pessoa física e holding tem de cobrir, na leitura da
# reforma do consumo. Critério da casa, não do caso.
CONSUMO_CRITERIOS = [
    "IBS e CBS, além do imposto de renda",
    "Natureza residencial ou comercial dos imóveis",
    "Créditos e redutores aplicáveis",
    "Custos administrativos",
    "Tributação dos resultados distribuídos",
]

GOV_TEMAS = [
    "Regras de deliberação e solução de impasses",
    "Saída e apuração de haveres",
    "Entrada de herdeiros e garantias",
    "Contratos entre partes relacionadas",
    "Separação entre riscos empresariais e patrimônio familiar",
]

EFI_TEMAS = [
    "Renda, vacância e liquidez",
    "Custo de manutenção",
    "Potencial de desenvolvimento",
    "Reserva de valor e função familiar ou operacional",
]

ROADMAP = [
    ("Arquitetura patrimonial",
     "Ex.: a relação entre pessoa física, holdings, empresas operacionais e copropriedades"),
    ("Tributação",
     "Ex.: cenários para imóveis, aluguéis, dividendos e patrimônio financeiro"),
    ("Sucessão e governança",
     "Ex.: quem coordenar (cônjuge, filhos, sócios) e o que preservar"),
    ("Riscos e eficiência",
     "Ex.: segregação funcional, contratos, garantias, liquidez e função dos ativos"),
]


def _itens(prefixo, n, dica=""):
    """Uma lista de `n` campos em branco. O que não for preenchido sai."""
    return '<ul class="lista small">%s</ul>' % "".join(
        "<li>%s</li>" % ph("%s_%d" % (prefixo, k), dica) for k in range(1, n + 1))


def _padrao(prefixo, textos, extra=0):
    """Uma lista já escrita, item a item editável, e `extra` itens em branco
    para o que o caso pedir a mais."""
    li = ["<li>%s</li>" % ph("%s_%d" % (prefixo, k), padrao=x)
          for k, x in enumerate(textos, start=1)]
    li += ["<li>%s</li>" % ph("%s_%d" % (prefixo, k))
           for k in range(len(textos) + 1, len(textos) + extra + 1)]
    return '<ul class="lista small">%s</ul>' % "".join(li)


def _titulo(nome, padrao):
    return '<h1 class="t">%s</h1>' % ph(nome, "Título da página", padrao=padrao)


def build(t, seg):
    set_date_ph("data_snapshot")
    S = []

    # --------------------------------------------------------------- capa
    S.append(cover_slide(
        t, "Wealth Planning", "Snapshot",
        ph("subtitulo_snapshot", "A linha sob o título",
           padrao="Fotografia patrimonial e frentes de evolução"),
        [ph("nome_cliente"), "Elaborado por " + ph("nome_responsavel"), ph("data_snapshot")]))

    # ----------------------------------------------------- fotografia patrimonial
    S.append(slide(t, "Fotografia patrimonial", 2, """<h1 class="t">Fotografia patrimonial</h1>
<div class="center"><div class="cols2" style="grid-template-columns:1fr 1.5fr;align-items:start">
  <div class="painel">
    <h2>Perfil</h2>
    %(perfil)s
  </div>
  <div>
    <h2>Indicadores principais</h2>
    %(tab)s
  </div>
</div></div>
<p class="legal" style="margin:0">%(obs)s</p>""" % dict(
        perfil=_itens("perfil", 8, "Ex.: residente fiscal no Brasil; casado sob comunhão parcial"),
        tab=table(["Indicador", "Valor"],
                  [[ph("ind_%d_indicador" % k, padrao=r), ph("ind_%d_valor" % k, "Ex.: ≈ R$ 13 milhões")]
                   for k, r in enumerate(INDICADORES, start=1)],
                  nums=[1], sm=True, widths=[62, 38]),
        obs=ph("fotografia_observacao", "Ressalva sobre a origem dos números",
               padrao="Valores aproximados, informados pelo cliente e ainda não integralmente "
                      "conciliados."))))

    # ------------------------------------------------------ conclusões preliminares
    S.append(slide(t, "Conclusões", 3, """<h1 class="t">Conclusões preliminares</h1>
<div class="center">%(tl)s</div>
<div class="note"><p>%(sint)s</p></div>""" % dict(
        tl='<ol class="tl">%s</ol>' % "".join(
            "<li><h4>%s</h4><p>%s</p></li>" % (
                ph("conclusao_%d_titulo" % k, "Ex.: Organização, Fragmentação"),
                ph("conclusao_%d_texto" % k, "Duas ou três linhas"))
            for k in (1, 2, 3, 4)),
        sint=ph("conclusoes_sintese", "A prioridade, numa frase",
                padrao="A prioridade é compreender, coordenar e racionalizar o patrimônio "
                       "existente antes de criar novas estruturas."))))

    # ------------------------------------------------------------------ núcleos
    S.append(slide(t, "Estrutura patrimonial", 4, """%(tit)s
<div class="nucleos">
  %(n1)s
  <div class="nc-centro"><div class="disco">%(centro)s</div></div>
  %(n2)s
  %(n3)s
  %(n4)s
</div>""" % dict(
        tit=_titulo("nucleos_titulo", "Patrimônio com diferentes núcleos"),
        centro=ph("nucleos_centro", "O que está no centro", padrao="Patrimônio familiar"),
        **{"n%d" % i: '<div class="nucleo %s"><h4>%s</h4><p>%s</p></div>' % (
            pos, ph("nucleo_%s_titulo" % k, padrao=nome),
            ph("nucleo_%s_texto" % k, "Quem e o quê: participações, percentuais, ativos"))
           for i, (k, nome, pos) in enumerate(NUCLEOS, start=1)})))

    # --------------------------------------------------------- reforma do consumo
    S.append(slide(t, "Análise tributária", 5, """%(tit)s
<div class="center"><div class="cols2" style="grid-template-columns:1fr 1.5fr;align-items:start">
  <div>
    <h2>Dados da carteira</h2>
    %(dados)s
  </div>
  <div class="painel">
    <h2>Leitura</h2>
    <p class="small">%(leitura)s</p>
    <p class="small">%(comp)s</p>
    %(crit)s
  </div>
</div></div>
<div class="note"><p>%(concl)s</p></div>""" % dict(
        tit=_titulo("consumo_titulo", "Reforma do consumo (IBS e CBS)"),
        dados=_itens("consumo_dado", 6, "Ex.: 38 imóveis na pessoa física"),
        leitura=ph("consumo_leitura", "O que os dados indicam para este caso"),
        comp=ph("consumo_comparacao", padrao="A comparação entre manutenção dos imóveis na "
                "pessoa física e sua exploração por holdings deve abranger:"),
        crit=_padrao("consumo_criterio", CONSUMO_CRITERIOS, extra=1),
        concl=ph("consumo_conclusao", padrao="A migração de imóveis para uma sociedade não é "
                 "automaticamente mais eficiente. A resposta tende a variar conforme a função, "
                 "o histórico e a utilização de cada grupo de ativos."))))

    # ----------------------------------------------------------- imposto de renda
    S.append(slide(t, "Análise tributária", 6, """%(tit)s
<div class="center"><div class="cols3" style="grid-template-columns:1fr 1.2fr 1.2fr;align-items:stretch">
  <div>
    <h2>Contexto</h2>
    %(ctx)s
  </div>
  <div class="painel">
    <h2>%(m_t)s</h2>
    <p class="small">%(m)s</p>
  </div>
  <div class="painel">
    <h2>%(a_t)s</h2>
    <p class="small">%(a)s</p>
  </div>
</div></div>
<div class="note"><p>%(concl)s</p></div>""" % dict(
        tit=_titulo("ir_titulo", "Imposto de renda"),
        ctx=_itens("ir_contexto", 5, "Ex.: renda mensal de ≈ R$ 100 mil; recebe dividendos"),
        m_t=ph("ir_mensal_titulo", padrao="Eixo mensal"),
        m=ph("ir_mensal_texto", padrao="A Lei nº 15.270/2025 prevê retenção de 10% quando uma "
             "mesma pessoa jurídica paga a uma mesma pessoa física mais de R$ 50 mil em "
             "dividendos no mês."),
        a_t=ph("ir_anual_titulo", padrao="Eixo anual"),
        a=ph("ir_anual_texto", padrao="A tributação mínima das altas rendas alcança rendimentos "
             "anuais superiores a R$ 600 mil e pode chegar à alíquota mínima de 10% a partir da "
             "base legal de R$ 1,2 milhão."),
        concl=ph("ir_conclusao", padrao="A oportunidade está em coordenar política de "
                 "distribuição, necessidade de caixa e tributação anual, sem fracionamentos "
                 "artificiais ou pagamentos sem fundamento econômico."))))

    # ------------------------------------------------------- integração sucessória
    S.append(slide(t, "Sucessão", 7, """%(tit)s
<div class="center"><div class="cols2" style="align-items:start">
  <div>
    <h2>Elementos observados</h2>
    %(obs)s
  </div>
  <div class="painel">
    <h2>Questões centrais a coordenar</h2>
    %(q)s
  </div>
</div></div>
<div class="note"><p>%(concl)s</p></div>""" % dict(
        tit=_titulo("sucessao_titulo", "Integração sucessória"),
        obs=_itens("sucessao_elemento", 7, "Ex.: casamento sob comunhão parcial; dois filhos"),
        q=_itens("sucessao_questao", 7, "Ex.: equilíbrio entre os filhos; preservação de controle"),
        concl=ph("sucessao_conclusao", padrao="O ponto central não é apenas transmitir bens, mas "
                 "coordenar propriedade, controle, renda, gestão e equilíbrio familiar."))))

    # ---------------------------------------------------- governança e eficiência
    S.append(slide(t, "Governança", 8, """%(tit)s
<div class="center"><div class="cols2" style="align-items:stretch">
  <div class="painel">
    <h2>Governança e segregação</h2>
    <h3>Contexto</h3>
    %(g_ctx)s
    <h3>Temas a examinar</h3>
    %(g_temas)s
  </div>
  <div class="painel">
    <h2>Eficiência econômica</h2>
    <h3>A carteira contém</h3>
    %(e_ctx)s
    <h3>Temas a examinar</h3>
    %(e_temas)s
  </div>
</div></div>
<div class="note"><p>%(concl)s</p></div>""" % dict(
        tit=_titulo("governanca_titulo", "Governança e função dos ativos"),
        g_ctx=_itens("governanca_contexto", 5, "Ex.: participações de 50% em sociedades"),
        g_temas=_padrao("governanca_tema", GOV_TEMAS),
        e_ctx=_itens("eficiencia_contexto", 4, "Ex.: imóveis de renda e terrenos"),
        e_temas=_padrao("eficiencia_tema", EFI_TEMAS),
        concl=ph("governanca_conclusao", padrao="A análise deve buscar previsibilidade, "
                 "organização e uso racional dos ativos, e não transferências patrimoniais "
                 "indiscriminadas."))))

    # ---------------------------------------------------------- frentes sugeridas
    S.append(slide(t, "Frentes de evolução", 9, """%(tit)s
<div class="center">%(tab)s</div>""" % dict(
        tit=_titulo("frentes_titulo", "Frentes sugeridas de evolução patrimonial"),
        tab=table(["Prioridade", "Frente", "Conteúdo"],
                  [[ph("fr_%d_prioridade" % k, "Alta, Média ou Monitoramento"),
                    ph("fr_%d_frente" % k, "Ex.: Sucessão e governança familiar"),
                    ph("fr_%d_conteudo" % k, "O que a frente examina, numa frase")]
                   for k in range(1, 7)],
                  sm=True, widths=[14, 26, 60]))))

    # ------------------------------------------------------------------ follow-up
    S.append(slide(t, "Próximos passos", 10, """<h1 class="t">Follow-up</h1>
<p class="lead">%(sub)s</p>
<div class="center"><ol class="steps" style="--n:4">%(st)s</ol></div>
<div class="note"><p>%(concl)s</p></div>
<p class="legal" style="margin:4mm 0 0">Este Snapshot possui natureza preliminar e foi elaborado
com base nas informações disponibilizadas. A implementação de qualquer medida dependerá de
análise jurídica, tributária, societária, registral e documental específica.</p>""" % dict(
        sub=ph("roadmap_titulo", "O nome do roadmap proposto",
               padrao="Roadmap integrado patrimonial e tributário"),
        st="".join("<li><h4>%s</h4><p>%s</p></li>" % (
            ph("roadmap_%d_titulo" % k, padrao=nome), ph("roadmap_%d_texto" % k, dica))
            for k, (nome, dica) in enumerate(ROADMAP, start=1)),
        concl=ph("followup_conclusao", padrao="Primeiro compreender e coordenar. Depois decidir "
                 "o que deve ser preservado, ajustado, ampliado ou descartado."))))

    return S
