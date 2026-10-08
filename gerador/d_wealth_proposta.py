# -*- coding: utf-8 -*-
"""Proposta de Wealth Planning.

Até aqui a AUVP Wealth fazia este material no Gamma, com identidade própria:
verde cheio, verde-limão, logo da Wealth. Ele passa a sair no desenho do
Private Banking, com o mesmo conteúdo e a mesma ordem de antes.

É a proposta do Estudo Preliminar de Wealth Planning (EPWP), a primeira fase do
método — a de leitura. Quase tudo aqui é texto da casa: quem somos, o que o
estudo compreende e não compreende, as quatro frentes, os entregáveis e o
disclaimer jurídico. Muda de cliente para cliente só o nome, os valores, quem
assina e o prazo de validade.

O disclaimer é texto do jurídico e fica fixo de propósito. Se ele mudar, muda
aqui, e o `npm run build` leva a mudança para o modelo.
"""
from layout import *

SOBRE = [
    ("Quem somos",
     "Boutique especializada em planejamento patrimonial e sucessório para famílias de alta "
     "renda, com foco em proteção de ativos e otimização fiscal dentro dos parâmetros legais."),
    ("Nosso diferencial",
     "Abordagem integrada entre gestão jurídica e patrimonial, garantindo segurança legal e "
     "maximização dos resultados financeiros para nossos clientes."),
    ("Experiência",
     "Nosso time de especialistas conta com mais de 20 anos de atuação com clientes de alto "
     "patrimônio, desenvolvendo estruturas personalizadas para proteção patrimonial e "
     "planejamento sucessório eficiente."),
]

NAO_COMPREENDE = [
    "Não é um Roadmap Executivo aprofundado",
    "Não modela estruturas societárias ou internacionais definitivas",
    "Não simula carga tributária com números",
    "Não define regime de tributação aplicável a entidades no exterior",
    "Não substitui a fase de Roadmap, que é autônoma e posterior",
]

FRENTES = [
    ("Mapeamento patrimonial, familiar e de residência",
     "Levantamento integrado do patrimônio financeiro e das participações, das jurisdições "
     "envolvidas e da situação de residência fiscal de cada integrante do casal. Identificação "
     "de titularidade formal, do regime de bens aplicável e das pendências cadastrais e "
     "documentais existentes."),
    ("Diagnóstico de riscos",
     "Identificação dos riscos e exposições patrimoniais, tributárias, sucessórias e "
     "societárias incidentes sobre a estrutura atual, com mapa de riscos organizado por "
     "criticidade e ordem de enfrentamento."),
    ("Sinalização de impactos normativos",
     "Indicação dos pontos da estrutura atual potencialmente afetados pela legislação em vigor "
     "e em curso de regulamentação, com destaque para o regime de tributação de entidades "
     "controladas no exterior e para os efeitos das reformas tributárias brasileiras, em nível "
     "diagnóstico e sem quantificação."),
    ("Tipologia de caminhos possíveis",
     "Indicação, em alto nível, dos caminhos de aprofundamento que o caso comporta (rota de "
     "residência fiscal, rota de estruturação internacional, rota sucessória ou rota de "
     "reorganização societária), com a recomendação da fase de Roadmap adequada e da "
     "sequência entre elas."),
]

ENTREGAVEIS = [
    "Mapa patrimonial, familiar e de residência fiscal consolidado",
    "Diagnóstico de riscos tributários, sucessórios e societários",
    "Sinalização dos impactos normativos pertinentes ao caso",
    "Tipologia de caminhos possíveis para aprofundamento",
    "Indicação do Roadmap subsequente recomendado e da sequência entre as frentes",
]

FORA_DO_ESCOPO = [
    "Modelagem comparativa de estruturas societárias e internacionais",
    "Definição ou formalização de opções de regime tributário perante a Receita Federal",
    "Procedimentos de comunicação e declaração de saída ou de ingresso de residência fiscal",
    "Diretrizes de protocolo familiar, acordo de quotistas ou acionistas",
    "Minutas de testamento, doação, contrato social ou estatuto",
    "Atos de registro civil, consularização ou tradução juramentada",
    "Roadmap de execução e compliance recorrente (declarações fiscais, FATCA, CRS)",
]


def _lista(itens, cls="lista"):
    return '<ul class="%s">%s</ul>' % (cls, "".join("<li>%s</li>" % i for i in itens))


def build(t, seg):
    set_date_ph("data_proposta")
    S = []

    # --------------------------------------------------------------- capa
    S.append(cover_slide(
        t, "Wealth", "Planning",
        ph("subtitulo_proposta", "A linha sob o título",
           padrao="Diagnóstico patrimonial estratégico"),
        [ph("nome_cliente", "Ex.: Maria e João Silva"),
         "Elaborada por " + ph("nome_responsavel"), ph("data_proposta")]))

    # ------------------------------------------------------------- quem somos
    S.append(slide(t, "Quem somos", 2, """<h1 class="t">Sobre a AUVP Wealth</h1>
<p class="lead">Soluções personalizadas em gestão patrimonial, sucessória e fiscal.</p>
<div class="center">%(cards)s</div>""" % dict(cards=cards(SOBRE, n=3))))

    # ------------------------------------------------------------------ escopo
    S.append(slide(t, "Escopo", 3, """<h1 class="t">O que compreende este estudo</h1>
<p class="lead"><strong>Estudo Preliminar de Wealth Planning (EPWP).</strong> É a primeira fase
do método AUVP: a fase de leitura.</p>
<div class="center"><div class="cols2" style="align-items:start">
  <div>
    <h2>O que compreende</h2>
    <p>Uma leitura preliminar do patrimônio, da estrutura familiar e das exposições tributárias
    e sucessórias da família, em contexto multijurisdicional.</p>
    <p>Identifica os caminhos possíveis de aprofundamento e a ordem em que devem ser
    enfrentados.</p>
  </div>
  <div class="painel">
    <h2>O que não compreende</h2>
    %(nao)s
  </div>
</div></div>
<div class="note"><p>“O EPWP é a primeira lente. O Roadmap é a arquitetura. São fases distintas,
com escopo e investimento próprios.”</p></div>""" % dict(nao=_lista(NAO_COMPREENDE))))

    # ----------------------------------------------------------------- frentes
    S.append(slide(t, "Método", 4, """<h1 class="t">Frentes de diagnóstico</h1>
<p class="lead">O EPWP é estruturado em quatro frentes complementares de leitura. Cada frente é
diagnóstica: identifica e sinaliza, sem modelar nem recomendar arquitetura específica.</p>
<div class="center">%(tl)s</div>""" % dict(tl=timeline(FRENTES))))

    # -------------------------------------------------------------- entregáveis
    S.append(slide(t, "Escopo", 5, """<h1 class="t">Entregáveis e limites desta fase</h1>
<p class="lead">O Estudo Preliminar de Wealth Planning entrega leitura, diagnóstico e tipologia
de caminhos. Toda modelagem específica, recomendação de arquitetura e redação de instrumentos é
objeto de fase posterior.</p>
<div class="center"><div class="cols2" style="align-items:start">
  <div>
    <h2>Entregáveis desta fase</h2>
    <p class="small"><strong>Apresentação executiva</strong>, contendo:</p>
    %(ent)s
    <p class="small" style="margin-top:3mm"><strong>Reunião executiva de devolutiva</strong>,
    para apresentação dos pontos centrais e dos caminhos indicados.</p>
  </div>
  <div class="painel">
    <h2>Fora do escopo desta fase</h2>
    %(fora)s
  </div>
</div></div>
<div class="note"><p>O EPWP é a leitura técnica preliminar do caso. A modelagem específica, o
desenho da arquitetura recomendada e a redação dos instrumentos são objeto exclusivo da fase de
Roadmap aprofundado, contratada em separado.</p></div>""" % dict(
        ent=_lista(ENTREGAVEIS, "lista small"), fora=_lista(FORA_DO_ESCOPO, "lista small"))))

    # ------------------------------------------------------------ investimento
    # No negativo, como a remuneração da carta de apresentação: é a página do
    # preço, e o Private sempre a destaca do resto.
    S.append(slide(t, "Investimento", 6, """<h1 class="t">Investimento para o diagnóstico</h1>
<div class="center">
  %(kpis)s
  <div class="cols2" style="align-items:start">
    <div>
      <h2>Execução</h2>
      <p>%(exec)s</p>
      <p class="mut small">A AUVP Wealth combina visão estratégica, expertise jurídica e
      tributária e métodos avançados de gestão de ativos e governança familiar, entregando uma
      estrutura sólida para o presente e preparada para o futuro patrimonial.</p>
    </div>
    <div>
      <h2>Fale conosco</h2>
      <div class="dl">
        <dt>Responsável</dt><dd>%(resp)s</dd>
        <dt>WhatsApp</dt><dd>%(whats)s</dd>
        <dt>E-mail</dt><dd>%(email)s</dd>
      </div>
    </div>
  </div>
</div>
<p class="legal" style="margin:0">Esta proposta tem validade de %(val)s a partir de sua
apresentação. Após esse prazo, os valores e condições aqui descritos deverão ser reavaliados em
função de eventual alteração normativa, mudança nas informações fornecidas ou revisão de
premissas.</p>""" % dict(
        kpis=kpis([("Valor do investimento para o EPWP",
                    ph("valor_epwp", "Ex.: R$ 18.600"), ""),
                   ("Valor do investimento para o Roadmap executivo",
                    ph("valor_roadmap", "Ex.: R$ 20.400"), "")], n=2),
        exec=ph("condicao_execucao", "Como a fase de execução é cobrada",
                padrao="Dependerá da estrutura escolhida pelo cliente."),
        resp=ph("nome_responsavel"), whats=ph("whatsapp_contato"), email=ph("email_contato"),
        val=ph("validade_proposta", "Prazo de validade da proposta", padrao="60 dias")),
        dark=True))

    # --------------------------------------------------------------- disclaimer
    S.append(slide(t, "Avisos", 7, """<h1 class="t">Disclaimer legal e de responsabilidade profissional</h1>
<div class="center"><div class="cols2" style="align-items:start">
  <div>
    <p class="legal">Os trabalhos da AUVP Wealth são concebidos e executados em estrita
    observância à legislação brasileira aplicável e às normas das demais jurisdições pertinentes
    ao caso, orientando-se por licitude, propósito negocial legítimo, substância econômica e
    integral cumprimento das obrigações principais e acessórias.</p>
    <p class="legal">A AUVP não concebe, recomenda ou operacionaliza estruturas destinadas à
    ocultação patrimonial, à omissão de rendimentos, à simulação de atos ou negócios jurídicos,
    ou a qualquer finalidade que caracterize evasão fiscal, e condiciona a continuidade de seus
    trabalhos à disponibilização completa e verídica das informações e documentos
    solicitados.</p>
    <div class="note"><p>Em decorrência dessa premissa, nenhum conteúdo deste documento
    constitui promessa, garantia ou compromisso de redução de carga tributária, de obtenção de
    economia fiscal, de deferimento de pleito perante autoridade administrativa ou judicial, ou
    de determinado tratamento tributário em qualquer jurisdição.</p></div>
  </div>
  <div>
    <p class="legal">As obrigações assumidas pela AUVP são <strong>de meio</strong>, e não
    <strong>de resultado</strong>. Toda análise reflete a legislação, a regulamentação e o
    entendimento das autoridades vigentes na data de sua emissão, sujeitos a alteração
    normativa, mudança de interpretação, divergência entre entes federativos e revisão de
    posicionamento fiscalizatório.</p>
    <p class="legal">A AUVP não responde por resultados tributários, financeiros ou
    patrimoniais decorrentes de decisões tomadas pelo cliente, da execução de recomendações por
    terceiros, da implementação parcial ou modificada das diretrizes indicadas, de informações
    incompletas, inexatas ou não reveladas, tampouco por autuações, glosas ou exigências
    fundadas em fatos anteriores à contratação ou alheios ao escopo contratado.</p>
  </div>
</div></div>"""))

    return S
