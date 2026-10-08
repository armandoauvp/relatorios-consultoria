# -*- coding: utf-8 -*-
"""Diagnóstico de carteira.

É o relatório de proposta que a consultoria já usava
(Relatorio_de_Proposta_AUVP_Capital_v2) no desenho novo. A sequência, os
tópicos, os gráficos e todos os textos são os dele, palavra por palavra: foram
escritos pelos analistas e pelos líderes, e não se mexe neles aqui. O que muda é
só a forma.

O relatório antigo trazia em vermelho as instruções ao consultor, para apagar
antes de enviar. Aqui elas viram a dica do campo em que o consultor escreve, e
nunca chegam ao papel. Os colchetes do texto (`[NOME DO CLIENTE]`, `[x%]`) viram
campos no próprio parágrafo.

Onde o antigo pedia para manter um texto entre vários (o do perfil, o do
cenário da carteira), o modelo traz todos, marcados com a escolha a que
pertencem, e a ferramenta deixa só o do que foi escolhido.
"""
from layout import *
from common import _b64

PAPEL = {"consultoria": "Consultor", "alta-renda": "Consultor",
         "private": "Banker", "assessoria": "Assessor"}

CLASSES_ROSCA = ["Renda fixa", "Ações", "Fundos imobiliários", "Internacional",
                 "Fundos de investimento", "Criptoativos"]


def T(s, **kw):
    """Preenche `@nome@` no texto. O texto do relatório tem `%` a cada linha, e
    a formatação com `%` obrigaria a dobrar todos eles."""
    for k, v in kw.items():
        s = s.replace("@%s@" % k, v)
    return s


def _risco_retorno():
    """O gráfico de risco e retorno do relatório: uma reta que sobe e, em
    quatro pontos dela, a distribuição dos retornos se abrindo à medida que o
    risco aumenta."""
    curvas = []
    for x, h, w in [(70, 16, 12), (150, 30, 20), (235, 46, 28), (320, 70, 38)]:
        y = 150 - (x - 30) * 0.28
        pts = []
        for k in range(-20, 21):
            ww = w * 2.718 ** (-(k / 9.0) ** 2)
            pts.append("%.1f,%.1f" % (x - ww, y + k * h / 20.0))
        curvas.append('<polyline points="%s"/><line x1="%d" y1="%.1f" x2="%d" y2="%.1f"/>'
                      % (" ".join(pts), x, y - h, x, y + h))
    return """<svg class="rr" viewBox="0 0 380 200" role="img" aria-label="Risk x Return">
  <line class="ax" x1="30" y1="185" x2="370" y2="185"/><line class="ax" x1="30" y1="185" x2="30" y2="10"/>
  <line class="rt" x1="30" y1="150" x2="365" y2="56"/>
  <g class="dist">%s</g>
  <text x="365" y="198" text-anchor="end">Risk</text>
  <text x="18" y="16" text-anchor="end" transform="rotate(-90 18 16)">Return</text>
</svg>""" % "".join(curvas)


def _seta(x, y1, y2):
    """Seta dupla vertical, de y1 a y2."""
    return ('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f"/>'
            '<polyline points="%.1f,%.1f %.1f,%.1f %.1f,%.1f"/>'
            '<polyline points="%.1f,%.1f %.1f,%.1f %.1f,%.1f"/>') % (
        x, y1 + 1, x, y2 - 1, x - 3, y1 + 5, x, y1 + 1, x + 3, y1 + 5,
        x - 3, y2 - 5, x, y2 - 1, x + 3, y2 - 5)


def _risco_ativos():
    """O risco total da carteira contra o número de ativos, como no relatório:
    o risco não sistemático cai com a diversificação e o sistemático fica."""
    def px(n):
        return 42 + (n - 1) * 10.2

    def py(n):      # cai até perto da linha do risco sistemático, sem tocá-la
        return 114 - 58 / (n ** 0.9)

    pts = " ".join("%.1f,%.1f" % (px(n / 4.0), py(n / 4.0)) for n in range(4, 101))
    yc = py((54 - 42) / 10.2 + 1)
    return """<svg class="rr ra" viewBox="0 0 380 205" role="img" aria-label="O risco total da carteira pelo total de ativos">
  <line class="ax" x1="40" y1="172" x2="300" y2="172"/><line class="ax" x1="40" y1="172" x2="40" y2="12"/>
  <polyline class="ax" points="37,18 40,12 43,18"/>
  <line class="ax" x1="40" y1="138" x2="300" y2="138"/>
  <polyline class="rt" points="%(pts)s"/>
  <g class="seta">%(s1)s%(s2)s</g>
  <text x="48" y="20">O Risco total da</text><text x="48" y="30">carteira</text>
  <text x="62" y="131">O risco não-sistemático</text>
  <text x="62" y="158">O risco sistemático</text>
  <text x="%(x1).1f" y="186" text-anchor="middle">1</text>
  <text x="%(x5).1f" y="186" text-anchor="middle">5</text>
  <text x="%(x15).1f" y="186" text-anchor="middle">15</text>
  <text x="306" y="176">Total de ativos na</text><text x="306" y="186">carteira</text>
</svg>""" % dict(pts=pts, s1=_seta(54, yc, 138), s2=_seta(54, 141, 172),
                 x1=px(1), x5=px(5), x15=px(15))


def _figura(arquivo, alt):
    """Gráfico que é o mesmo para todo cliente: a imagem do relatório antigo,
    fixa no modelo."""
    return '<figure class="fig-fixa"><img src="data:image/png;base64,%s" alt="%s"></figure>' % (
        _b64("assets/diagnostico/" + arquivo), alt)


def _donut(titulo, desc, altura="62mm"):
    """Rosca com o título que, no relatório, vinha dentro da imagem."""
    return '<div class="graf-bloco"><p class="tit-graf">%s</p>%s</div>' % (
        titulo, chart(titulo, desc, "donut", "min-height:%s" % altura))


def _par(a, b):
    return '<div class="cols2 par-graf">%s%s</div>' % (a, b)


def _texto(nome, dica):
    """O parágrafo que o consultor escreve no lugar da instrução em vermelho."""
    return '<p>%s</p>' % ph(nome, dica)


def build(t, seg):
    P = []
    papel = PAPEL[seg]

    def pagina(sec, corpo, attrs=""):
        P.append(page_a4(t, sec, len(P) + 1, corpo, data=False, attrs=attrs))

    P.append(cover_a4(t, "Diagnóstico", "de Carteira", "Relatório de", "Proposta",
                      ["Cliente - " + ph("nome_cliente"),
                       "Perfil de investidor - " + ph("perfil_investidor"),
                       papel + " - " + ph("nome_responsavel")], grafismo=2))

    # ------------------------------------------------------------ abertura
    pagina("Apresentação", """<p>A partir da realização do processo de suitability - Análise do Perfil do
Investidor, que consistiu em uma reunião de coleta de informações e de um período de análise destes
dados, apresentamos por meio deste documento uma proposta de atuação para atender a(s) demanda(s)
apresentada(s) a nós da AUVP Consultoria.</p>
<p>Para isso, partiremos de quatro pontos centrais para justificar a nossa linha de atuação durante o
processo de consultoria:</p>
<ol class="pontos">
  <li>Avaliação do contexto do cliente e definição de perfil de risco;</li>
  <li>Estrutura meta da carteira e camadas de proteção do patrimônio;</li>
  <li>Análise da carteira atual e proposta para cada classe de ativo;</li>
  <li>Fluxo de aplicações e adequação metodológica;</li>
</ol>
<p>Em sequência, apresentaremos um modelo estrutural que, após a anuência do cliente, servirá como
uma estrutura inicial na condução do processo. Observo que ao longo do acompanhamento, alterações de
cenário eventualmente trarão a necessidade de alterações pontuais nas sugestões que serão dadas nos
próximos meses.</p>
<p>Por fim, objetivamos apresentar soluções pautadas na realidade e na segurança do patrimônio
contemplado, aqui, pois compreendemos que os patrimônios construídos ao longo da vida devem ser
preservados tem caráter perpétuo - nunca diluídos.</p>
<div class="disclaimer">
  <p class="dt">Disclaimer</p>
  <p>a) As informações contidas neste relatório constituem uma recomendação exclusiva de
  investimentos, a partir de um suitability próprio, realizada por um profissional habilitado para
  esta finalidade, designado pela AUVP Consultoria Financeira e de Investimentos, possui caráter
  confidencial. Portanto, não devendo tais informações serem divulgadas para fins de recomendações
  públicas de investimentos e/ou não se destina à publicação ou distribuição a terceiros.</p>
  <p>b) Rentabilidades passadas não são garantias de rentabilidades futuras. As informações,
  opiniões, estimativas e projeções contidas neste documento estão sujeitas a mudanças, não
  implicando necessariamente na obrigação de quaisquer comunicações no sentido de atualização ou
  revisão, a respeito de tais mudanças, fora do escopo temporal da consultoria contratada.</p>
</div>""")

    # ---------------------------------------------------------- 1. Contexto
    # Os itens a), b) e c) eram inteiros em vermelho: são o que o consultor
    # escreve, e a instrução vai na dica.
    pagina("1. Contexto", T("""<h1 class="t">1. Contexto</h1>
<p>Posto que:</p>
<ol class="alfa">
  <li>@a@</li>
  <li>@b@</li>
  <li>@c@</li>
  <li>Por meio da consultoria, procura:
    <ol class="romano">
      <li>@mestre@</li>
      <li>@sec@</li>
    </ol>
  </li>
  <li>Divisão do patrimônio:</li>
</ol>
@tab@
<p class="apos-tab">Em virtude dos fatores descritos acima e das predileções durante o processo de
suitability, avaliamos o perfil de investimentos como @perf@.</p>
@perfis@""",
        a=ph("contexto_cliente", "Cliente tem N anos, solteiro/casado sob o regime X, com "
             "dependentes/filhos, e reside em Cidade - UF. Se a gestão do patrimônio for feita em "
             "conjunto, incluir o nome completo do cônjuge;"),
        b=ph("contexto_trabalho", "Atua como X, sob vínculo de trabalho do tipo CLT / PJ / "
             "estatutário-servidor público / empresário-sócio / autônomo / comissionado, com renda "
             "mensal de R$ X, gastos de R$ X e capacidade de aportar R$ X. Se o cliente não vai "
             "aportar e vai trabalhar apenas com a liquidez que já tem, deixar isso explícito;"),
        c=ph("contexto_consideracoes", "Demais considerações relevantes sobre o cliente: viés com "
             "determinados setores, nível de conhecimento em cada classe de ativo, necessidade de "
             "caixa para um objetivo próximo, existência e alocação atual da reserva de emergência;"),
        mestre=ph("objetivo_mestre_texto", "Objetivo Mestre (em geral, liberdade financeira ou renda "
                  "passiva a partir de determinado prazo)"),
        sec=ph("objetivos_secundarios_texto", "Objetivos Secundários (troca de carro, entrada de "
               "imóvel, viagem, curso) — ser detalhista, é o que prova que o relatório não é "
               "padronizado"),
        tab=table(["Patrimônio", "Valor (R$)", "Distribuição (%)"],
                  [[n, ph("pat_%s_valor" % k), ph("pat_%s_dist" % k)]
                   for n, k in [("Financeiro", "financeiro"), ("Imobilizado", "imobilizado"),
                                ("Liquidez", "liquidez")]],
                  nums=[1, 2], sm=True, widths=[40, 30, 30]),
        perf=ph("perfil_investidor", "Conservador, Moderado ou Arrojado. Dentre os textos abaixo, "
                "apenas aquele que se refere ao perfil do cliente é mantido."),
        perfis="\n".join(
            '<p data-se-campo="perfil_investidor" data-se-valor="%s"><strong>%s:</strong> %s</p>' % (n, n, x)
            for n, x in [
                ("Conservador", "Este perfil possui baixa tolerância ao risco, portanto, existe uma "
                 "necessidade de exposição a investimentos que oferecem maior estabilidade, mesmo que "
                 "isso signifique uma rentabilidade menor no longo prazo."),
                ("Moderado", "Este perfil modera entre uma rentabilidade significativamente superior "
                 "às taxas básicas do país de origem e compreende como natural um pouco de oscilação "
                 "no patrimônio ao longo dos ciclos econômicos, possuindo também um horizonte de "
                 "investimentos relativamente pré-definido."),
                ("Arrojado", "Este perfil aceita correr um risco maior para obter melhores retornos "
                 "e compreende como natural a oscilação no patrimônio ao longo dos ciclos econômicos, "
                 "com um horizonte de investimentos voltado para o longo prazo.")])))

    pagina("1. Contexto", T("""<p>Em suma, as classificações de perfis existem para atrelar as necessidades e
objetivos do investidor, o contexto de vida, além do apetite ao risco, aos diferentes produtos
financeiros disponíveis no mercado, com os seus diferentes graus de risco. É importante destacar que
um risco maior não necessariamente implica um retorno maior, mas sim possibilidades mais amplas de
retorno.</p>
<div class="rr-box">@rr@</div>
<p>O risco aumenta a incerteza em relação ao comportamento dos ativos, ou seja, produtos mais
arriscados, como ações de empresas emergentes ou criptomoedas, oferecem o potencial de retornos
expressivos em períodos curtos, mas também podem sofrer volatilidade significativa. Por outro lado,
investimentos de menor risco, como títulos públicos, tendem a oferecer retornos mais estáveis e
previsíveis, embora menores.</p>""", rr=_risco_retorno()))

    # ------------------------------------------ 2. Estrutura meta e proteção
    SEC2 = "2. Estrutura meta"
    pagina(SEC2, T("""<h1 class="t">2. Estrutura Meta da Carteira e Camadas de Proteção</h1>
<p>A partir das premissas básicas de classes de ativos para a carteira, seguimos para a montagem de
uma estrutura meta de carteira. Por “estrutura meta”, compreenda uma proporção de alocação que serve
como um norteador para os aportes, para o balanceamento ao longo do tempo e uma prevenção contra
heurísticas comportamentais, que são vieses que atrapalham o investidor no seu dia-a-dia</p>
<h2>2.1. Diagnóstico da Carteira Atual e Estrutura Meta</h2>
<p>Antes de detalhar cada classe de ativo, apresentamos lado a lado o retrato da carteira que existe
hoje e a alocação-alvo que propomos. A intenção é que a leitura da proposta comece por um único
olhar: de onde a carteira sai e para onde ela vai.</p>
<p class="tit-graf">Estrutura Meta</p>
<div class="cols2 par-graf meta-lado">
  <div><div class="cab">Carteira atual</div>@atual@</div>
  <div><div class="cab">Estrutura meta</div>@meta@</div>
</div>
<p class="so-campo">@cen@</p>""",
        atual=chart("Carteira atual", "Gráfico de alocação atual.", "donut", "min-height:70mm",
                    series=CLASSES_ROSCA),
        meta=chart("Estrutura meta", "Gráfico de rosca da estrutura meta, da planilha Estrutura Meta.",
                   "donut", "min-height:70mm", series=CLASSES_ROSCA),
        # O cenário não se imprime: é a escolha que decide qual dos quatro
        # textos a seguir fica no relatório.
        cen=ph("cenario_carteira", "Os textos a seguir são a base do diagnóstico macro da carteira. "
               "Todo cliente se enquadra em um dos quatro cenários — pulverizada, concentrada, "
               "equilibrada ou em liquidez. Fica apenas o texto do cenário escolhido aqui. Este "
               "tópico é só o retrato macro: a análise classe por classe vem na seção 3.")))

    # Os quatro cenários. Cada página leva a marca do seu, e fica a do
    # cenário escolhido em `cenario_carteira`.
    def cenario(valor, *paginas):
        for corpo in paginas:
            pagina(SEC2, corpo, 'data-se-campo="cenario_carteira" data-se-valor="%s"' % valor)

    cenario("Pulverizada", """<h3 class="cenario">CARTEIRA PULVERIZADA</h3>
<p>No portfólio atual, identificamos uma pulverização excessiva do patrimônio investido, visto que a
quantidade de ativos excede os limites eficientes de diversificação do risco não sistemático. Para
entender melhor essa distinção, o risco sistemático, também conhecido como risco de mercado, está
relacionado a fatores macroeconômicos que afetam todos os ativos, como taxas de juros, inflação,
riscos políticos e recessões. Esse tipo de risco não pode ser eliminado por diversificação dentro de
um único país.</p>
<p>Já o risco não sistemático é específico de um ativo ou setor. Ele pode estar relacionado a fatores
como má gestão, mudanças regulatórias e concorrência. Esse tipo de risco pode ser reduzido ao
diversificar os investimentos em ativos de setores diferentes e descorrelacionados, conforme
preconizado pela Teoria Moderna do Portfólio, desenvolvida por Markowitz. No entanto, a pulverização
excessiva pode gerar os seguintes efeitos negativos:</p>
<ul class="lista">
  <li><strong>Diluição de retornos:</strong> O excesso de ativos faz com que os ganhos expressivos de alguns ativos sejam compensados por desempenhos fracos de outros, limitando a capacidade de obter retornos significativos.</li>
  <li><strong>Falta de concentração em oportunidades:</strong> A carteira fica dispersa, dificultando a alocação de recursos em ativos com maior potencial de valorização.</li>
  <li><strong>Gestão mais complexa:</strong> Um número elevado de ativos exige mais tempo e recursos para monitoramento e ajustes constantes.</li>
  <li><strong>Margem reduzida para otimização:</strong> Acima de um certo número de ativos, os benefícios adicionais de diversificação são marginais, conforme a teoria de Markowitz.</li>
</ul>
<p class="apos-lista">A relação entre esses riscos pode ser visualizada no gráfico abaixo:</p>
<div class="rr-box">%s</div>
<p>Segundo Ray Dalio, a diversificação eficiente envolve a escolha entre 15 e 20 ativos
descorrelacionados, o que maximiza os retornos enquanto reduz o risco. Além desse número, os
benefícios da diversificação tornam-se marginais, pois mais ativos não oferecem proteção adicional
relevante e podem diluir os ganhos potenciais.</p>""" % _risco_ativos())

    cenario("Concentrada", """<h3 class="cenario">CARTEIRA CONCENTRADA</h3>
<p>No portfólio atual, identificamos uma concentração excessiva do patrimônio investido, o que expõe o
investidor a um risco elevado, uma vez que a diversificação é limitada. A concentração em poucos
ativos pode amplificar o impacto de riscos não sistemáticos, que são específicos de um ativo ou setor.
Esses riscos podem incluir problemas de gestão, mudanças regulatórias ou oscilações na demanda de
mercado.</p>
<p>Diferentemente do risco sistemático, que afeta todos os ativos em um mercado e não pode ser
mitigado por diversificação, o risco não sistemático pode ser reduzido ao aumentar o número de ativos
diversificados no portfólio. Posto isso, a concentração resulta nos seguintes efeitos negativos:</p>
<ul class="lista">
  <li><strong>Maior exposição ao risco não sistemático:</strong> O portfólio fica vulnerável a eventos adversos que impactem um setor ou ativo específico.</li>
  <li><strong>Volatilidade acentuada:</strong> Com poucos ativos, a volatilidade dos retornos tende a ser maior, pois quedas ou oscilações significativas em um ativo impactam diretamente o desempenho geral da carteira.</li>
  <li><strong>Dependência de menos oportunidades:</strong> A concentração em poucos ativos limita o número de oportunidades de ganho, colocando o portfólio à mercê do sucesso de poucos investimentos.</li>
  <li><strong>Menor margem de segurança:</strong> Sem diversificação suficiente, a capacidade de mitigar perdas em períodos de crise é reduzida, pois não há ativos descorrelacionados para compensar possíveis quedas.</li>
</ul>
<p class="apos-lista">A relação entre o risco e o número de ativos pode ser visualizada no gráfico abaixo.</p>
<div class="rr-box">%s</div>
<p>Segundo a Teoria Moderna do Portfólio, de Markowitz, a diversificação inteligente envolve manter
uma quantidade adequada de ativos descorrelacionados, geralmente entre 15 e 20, conforme recomendado
também por Ray Dalio. Concentrar-se em poucos ativos pode resultar em maior risco sem o retorno
compensatório, contrariando os princípios da diversificação eficiente.</p>""" % _risco_ativos())

    cenario("Equilibrada", """<h3 class="cenario">CARTEIRA EQUILIBRADA</h3>
<p>No portfólio atual, identificamos uma alocação equilibrada e coerente com os princípios de
diversificação eficiente, o que representa uma base sólida para os próximos passos do planejamento. A
quantidade e a distribuição dos ativos entre as diferentes classes evidenciam um cuidado prévio na
construção da carteira, reduzindo a exposição a riscos não sistemáticos sem incorrer na diluição de
retornos típica da pulverização excessiva. Essa estrutura já equilibrada traz benefícios
importantes:</p>
<ul class="lista">
  <li><strong>Mitigação eficiente do risco não sistemático:</strong> a diversificação entre ativos e setores distintos reduz o impacto de eventos específicos de uma empresa ou segmento sobre o resultado global da carteira.</li>
  <li><strong>Preservação do potencial de retorno:</strong> ao evitar tanto a concentração excessiva quanto a pulverização, a carteira mantém espaço para que os ativos de melhor desempenho contribuam de forma relevante para o resultado.</li>
  <li><strong>Gestão mais previsível:</strong> um número adequado de posições facilita o acompanhamento e o rebalanceamento periódico, sem a complexidade operacional de carteiras excessivamente pulverizadas.</li>
</ul>
<p class="apos-lista">Vale destacar que uma carteira bem estruturada não é sinônimo de carteira estática. Mesmo em
portfólios equilibrados, costumam existir oportunidades pontuais de otimização como em eficiência
tributária, custos, aderência ao ciclo econômico atual ou exposição a classes ainda pouco
representadas no seu portfólio. Essas oportunidades específicas são detalhadas na seção 3, junto à
estruturação da meta de carteira.</p>""")

    cenario("Em liquidez", """<h3 class="cenario">CARTEIRA EM LIQUIDEZ</h3>
<p>O portfólio atual está integralmente posicionado em ativos de liquidez, sem uma estrutura de
investimentos definida. Esta é uma oportunidade de construir a carteira desde o início, alinhada aos
objetivos e ao perfil de risco levantados no processo de suitability. Antes de avançar, vale
reconhecer que manter recursos em liquidez tem um papel legítimo, especialmente para a reserva de
emergência e objetivos de curtíssimo prazo. No entanto, quando a totalidade do patrimônio permanece
nessa condição por período prolongado, alguns pontos merecem atenção:</p>
<ul class="lista">
  <li><strong>Custo de oportunidade:</strong> recursos represados em liquidez deixam de capturar o potencial de valorização de outras classes de ativos ao longo do tempo, especialmente em horizontes de médio e longo prazo.</li>
  <li><strong>Ausência de direcionamento por objetivo:</strong> sem uma estrutura de carteira, é mais difícil conectar os recursos disponíveis aos objetivos específicos do cliente (aposentadoria, renda, sucessão etc.), que são a base do planejamento apresentado na seção 3.</li>
</ul>
<p class="apos-lista">Um ponto positivo deste cenário: por não existir uma carteira legada a ser desmontada, a
estruturação pode ser feita integralmente dentro da nossa metodologia, com aportes graduais, sem os
custos ou eventos de tributação normalmente associados à migração de uma carteira já posicionada,
conforme detalhado na seção 4.</p>""")

    # Os colchetes do parágrafo de comparação são campos. Os opcionais
    # ("[e pelo redirecionamento...]", "[ou: com venda parcial...]") também: em
    # branco, saem sem deixar a vírgula para trás.
    pagina(SEC2, T("""@coment@
<p>Comparando a carteira atual com a estrutura meta, @nome@ está hoje com @c1@ em @a1@ contra os @m1@
propostos, e com @c2@ em @a2@ contra @m2@. A correção dessas diferenças será feita principalmente pelos
novos aportes, direcionados às classes que estão abaixo do alvo @redir@, @venda@. As posições em
@mant@ já estão aderentes à estratégia e serão mantidas. A reserva de emergência e a liquidez de
curto prazo ficam fora dessa comparação: elas protegem a alocação e não competem com ela.</p>
<h2>2.2. Alinhamento de Expectativas de Rentabilidade</h2>
<p>A referência que utilizamos é o retorno nominal histórico dos títulos públicos brasileiros.
Avaliando a Selic e os títulos indexados à inflação, a média entregue desde 2003 equivale a
aproximadamente a variação do IPCA acrescida de 5% ao ano. Por isso trabalhamos a expectativa de
rentabilidade da carteira como IPCA + 5% ao ano, ou seja, um retorno nominal composto pela inflação
do período mais cerca de 5% de ganho real acima dela.</p>
@hist@
<p class="fonte">Fonte: Clube dos Poupadores</p>
<p>Essa abordagem conservadora permite alinhar a estrutura da carteira a uma estratégia sólida e
factível, mitigando o risco de excesso de exposição a qualquer classe de ativos e garantindo uma base
sustentável para o crescimento patrimonial ao longo do tempo.</p>
<p>Reforçamos que essa é uma premissa de projeção, e não uma promessa de retorno. Ela serve para
mitigar o risco de excesso de exposição a qualquer classe de ativos, não para prever
rentabilidade.</p>""",
        coment=_texto("comentario_carteira", "Inserir comentários gerais sobre a carteira, como "
                      "aderência ao perfil de risco e aos objetivos informados no suitability. Valide "
                      "também o que já está bem feito: se o cliente tem bons ativos na carteira, elogie "
                      "explicitamente antes de entrar nos pontos de ajuste."),
        nome=ph("nome_cliente"),
        c1=ph("comparacao_1_classe", "[classe]"), a1=ph("comparacao_1_atual", "[x%]"),
        m1=ph("comparacao_1_meta", "[y%]"),
        c2=ph("comparacao_2_classe", "[classe]"), a2=ph("comparacao_2_atual", "[x%]"),
        m2=ph("comparacao_2_meta", "[y%]"),
        redir=ph("comparacao_redirecionamento", "Opcional: e pelo redirecionamento dos vencimentos de "
                 "renda fixa a partir de [data]"),
        venda=ph("comparacao_venda", "Ou: com venda parcial e gradual apenas de [ativo], pelo motivo "
                 "descrito adiante", "sem necessidade de vender"),
        mant=ph("comparacao_mantidas", "[ativos/classes]"),
        hist=_figura("retorno-historico.png", "Juro real dos títulos públicos desde 2003")))

    pagina(SEC2, T("""<h2>2.3. Projeção Financeira</h2>
<p>Para garantir uma renda passiva desejada de @renda@ por mês, estimamos que será necessário
acumular um patrimônio de @alvo@, considerando a premissa de IPCA + 5% ao ano descrita acima.
Partindo de um patrimônio inicial de @ini@ com aportes mensais de @aporte@, será necessário um prazo
estimado de @prazo@ meses para atingir esse objetivo. O gráfico a seguir demonstra a evolução
esperada do patrimônio ao longo desse período.</p>
@proj@
<h2>2.4. Camada de Proteção (1) — Reserva de Emergência</h2>
<p>A reserva de emergência deve ser suficiente para cobrir 12 meses do custo de vida em um cenário
estressado. Para a sua carteira, recomendamos uma reserva de @res@.</p>
<p>Essa reserva é essencial para garantir segurança em momentos de imprevistos, como perda de renda
ou despesas emergenciais. O veículo escolhido precisa atender, ao mesmo tempo, a três critérios:
disponibilidade em D+0 ou D+1; ausência de risco de principal, de modo que o valor não esteja menor
justamente quando você precisar dele; e ausência de carência ou penalidade de saída. Entre as
alternativas que atendem a esses critérios estão os CDBs de liquidez diária emitidos por instituições
financeiras sólidas e com proteção do Fundo Garantidor de Créditos (FGC), o Tesouro Selic e o
AUPO11.</p>""",
        renda=ph("valor_renda_passiva"), alvo=ph("valor_patrimonio_necessario"),
        ini=ph("valor_patrimonio_inicial"), aporte=ph("valor_aporte_mensal"),
        prazo=ph("qtd_meses_objetivo", "N"),
        res=ph("valor_reserva_emergencia"),
        proj=chart("Projeção financeira", "Evolução esperada do patrimônio, em meses: valor aportado "
                   "e patrimônio.", "line", "min-height:62mm",
                   series=["Valor Aportado", "Patrimônio"], eixo="R$")))

    pagina(SEC2, T("""<h2>2.5. Camada de Proteção (2) — Proteção Patrimonial e Sucessória</h2>
<p>Além de estruturar o crescimento do patrimônio, um planejamento patrimonial completo precisa
considerar o que acontece com a família e com os objetivos traçados caso um evento inesperado (morte,
invalidez ou doença grave) interrompa a capacidade de geração de renda de @nome@. Consideramos, para
isso, dois instrumentos com funções complementares: o seguro de vida, que cobre o risco de perda de
renda no valor do capital segurado contratado, e a previdência privada (PGBL/VGBL), veículo de
acumulação com função sucessória e, no caso do PGBL, benefício fiscal.</p>
<p>No seu momento de vida atual @gat@, a proteção da renda familiar ganha relevância adicional.
@seg@, recomendamos avaliar se o capital segurado é suficiente para manter o padrão de vida da
família e quitar dívidas vinculadas à sua renda, como o financiamento do imóvel, por um período de
transição.</p>
<p>Do ponto de vista sucessório, tanto o seguro de vida quanto a previdência privada (PGBL/VGBL)
possuem uma característica estratégica: os valores pagos aos beneficiários indicados não integram o
inventário nem seguem as regras gerais de partilha de herança. No caso do seguro de vida, essa regra
está prevista no artigo 794 do Código Civil. No caso da previdência privada, o Supremo Tribunal
Federal (Tema 1.214, decisão de janeiro de 2025) e, mais recentemente, a Lei Complementar nº 227/2026
confirmaram que os valores recebidos por beneficiários de VGBL e PGBL não estão sujeitos ao ITCMD e
não entram no inventário. Na prática, isso tende a significar acesso mais rápido dos beneficiários aos
recursos, sem esperar o processo de inventário, que pode levar meses ou anos, e mais liberdade para
direcionar parte do patrimônio a pessoas específicas, dentro dos limites legais.</p>
<p>Como a regulamentação tributária e sucessória desses produtos tem sido alterada com frequência nos
últimos anos, recomendamos sempre confirmar a legislação vigente e o entendimento do estado de
domicílio no momento da operação, e orientamos @nome@ a formalizar a estratégia com um advogado
especializado em planejamento sucessório.</p>
<p>Sob a ótica fiscal, caso @nome@ contribua para o INSS ou regime próprio e opte pela declaração de
Imposto de Renda completa, os aportes em PGBL permitem deduzir da base de cálculo do IR até 12% da
renda bruta anual tributável, um benefício que hoje @pgbl@, considerando a renda mensal de
@rendam@.</p>
<p>Com base no seu perfil, contexto familiar e objetivos, nossa recomendação inicial é: @rec@. Essa
recomendação será detalhada e cotada em conjunto com nossos parceiros especializados em seguro.</p>
<p>A recomendação final de produto e a cotação são feitas em conjunto com os parceiros especializados
em seguros e previdência da AUVP.</p>""",
        nome=ph("nome_cliente"),
        gat=ph("protecao_gatilho_texto", "Inserir gatilho identificado no KYC, por exemplo: "
               "casamento previsto para, filho(a) de [idade], dependentes financeiros"),
        seg=ph("protecao_seguro_texto", "Se aplicável: hoje, na ausência de um seguro de vida vigente "
               "/ com o seguro de vida atual, no valor de capital segurado de R$ [valor]"),
        pgbl=ph("pgbl_situacao", "não está sendo utilizado / está sendo utilizado parcialmente"),
        rendam=ph("valor_renda_mensal"),
        rec=ph("protecao_recomendacao", "Preencher — priorizar seguro de vida temporário com capital "
               "segurado de R$ [x] / priorizar previdência PGBL como veículo de acumulação com "
               "benefício fiscal e função sucessória / combinar os dois instrumentos")))

    # --------------------------------------- 3. Análise por classe de ativo
    SEC3 = "3. Análise por classe"
    pagina(SEC3, T("""<h1 class="t">3. Análise da Carteira Atual e Proposta por Classe</h1>
<h2>3.1. Renda Fixa</h2>
<h3>Carteira atual</h3>
<p class="tit-graf">Indexadores</p>
@tab@
<div class="cols2 par-graf">
  <div class="graf-bloco"><p class="tit-graf">Liquidez</p>@liq@</div>
  <div class="graf-bloco"><p class="tit-graf">Emissores</p>@emis@</div>
</div>""",
        tab=table(["Indexador", "Taxa Média", "Valor", "Percentual"],
                  [[n, ph("rf_%s_taxa" % k), ph("rf_%s_valor_atual" % k), ph("rf_%s_perc" % k)]
                   for n, k in [("Prefixado", "pre"), ("IPCA", "ipca"), ("% CDI", "pcdi"),
                                ("CDI+", "cdimais"), ("Selic", "selic")]],
                  nums=[2, 3], sm=True),
        liq=chart("Liquidez", "Valor que vence em cada data.", "bars", "min-height:70mm", eixo="R$"),
        emis=chart("Emissores", "Valor aplicado em cada emissor.", "bars", "min-height:70mm", eixo="R$")))

    pagina(SEC3, T("""@coment@
<h3>Estrutura meta proposta</h3>
<p>Nossa abordagem para a alocação em Renda Fixa é baseada na estratégia <strong>Barbell</strong>,
que combina a <strong>proteção</strong> de ativos de <strong>curto prazo</strong> com a busca por
<strong>maiores retornos</strong> em ativos de <strong>longo prazo</strong>. Utilizamos, nesse
contexto, ativos indexados à inflação para maximizar os retornos ao longo do tempo, enquanto nos
protegemos no curto prazo com títulos prefixados e pós-fixados.</p>
<p>Essa estratégia é caracterizada por evitar ativos de médio prazo, concentrando-se apenas em
<strong>títulos de curto e longo prazo</strong>. Os primeiros proporcionam <strong>estabilidade e
proteção</strong>, enquanto os segundos oferecem potencial de <strong>rentabilidade mais elevado e
maior flexibilidade para movimentos de marcação a mercado</strong>.</p>
<p>Com base no cenário atual e nas condições de mercado, estruturamos a carteira conforme a tabela a
seguir, que apresenta, por <strong>indexador</strong>, os <strong>prazos</strong> para carregamento até
o vencimento e os prazos mínimos para estratégias de marcação a mercado. <strong>Esses parâmetros
servem como referência e poderão ser ajustados pontualmente conforme oportunidades
táticas:</strong></p>
@prazos@
<p class="apos-tab">Para maximizar a segurança e aproveitar os limites de proteção do Fundo Garantidor
de Créditos (FGC), trabalhamos com exposição a títulos bancários (CDBs, LCIs e LCAs) de até R$200 mil
por emissor. Essa é a margem de segurança prática para não estourar o teto legal de R$250 mil por
instituição, já que a rentabilidade acumulada entra nesse cálculo e pode levar o valor total acima do
limite se a alocação inicial já estiver no teto. Para ativos de crédito privado sem garantia do FGC
(debêntures, CRIs e CRAs), a alocação é feita em emissores com rating elevado e limitada a 5% do
patrimônio por emissor — e o retorno oferecido precisa superar o de um título bancário equivalente,
para compensar o risco assumido sem garantia.</p>""",
        coment=_texto("comentario_rf", "Inserir comentários sobre a carteira de renda fixa do cliente: "
                      "taxas por indexador, concentração em emissores, liquidez da carteira e o que será "
                      "trabalhado na consultoria. Pontos de atenção a levantar: risco de crédito do "
                      "emissor, teto do FGC (R$250 mil) e vencimentos pré-fixados muito longos. "
                      "Complemente com o cenário doméstico atual e o que pode impactar a curva de juros "
                      "futura. Não misture aqui fundos de liquidez nem ETFs de renda fixa (ex.: AUPO11, "
                      "LFTB11) — eles têm espaço próprio na seção de fundos. Se o cliente não tem "
                      "exposição a algum indexador, remova a linha da tabela em vez de deixá-la zerada."),
        prazos=table(["Indexador", "Prazo para Carrego", "Prazo para Marcação"],
                     [["Inflação", "A partir de 4 anos", "A partir de 10 anos"],
                      ["Prefixado", "Até 3 anos", "A partir de 5 anos"],
                      ["CDI | Selic", "Até 2 anos", "-"]], sm=True)))

    pagina(SEC3, T("""<p>Essas decisões estruturais dialogam diretamente com o cenário atual da economia
brasileira. A seguir, apresentamos a curva de juros atual, que embasa as escolhas de prazos e
indexadores na estratégia de Renda Fixa:</p>
@curva@
<p class="fonte">Fonte: Dados da Anbima, elaborado por AUVP Consultoria</p>
<p>Apesar da curva de juros indicar uma expectativa de queda da Selic ao longo do próximo ano, os
<strong>juros nominais</strong> ainda estão em patamares historicamente <strong>elevados</strong>, o
que justifica travar parte da carteira em <strong>títulos prefixados com taxas atrativas</strong>.</p>
<p>Ao mesmo tempo, é importante manter uma <strong>exposição estratégica em ativos atrelados ao
CDI</strong>, que oferecem <strong>liquidez</strong> e <strong>flexibilidade</strong> para aproveitar
<strong>oportunidades táticas</strong> que possam surgir com eventuais movimentações na curva de juros
ou mudanças no cenário macroeconômico. Essa combinação permite capturar o prêmio atual do juro alto,
sem abrir mão da capacidade de reposicionamento.</p>
<p>No entanto, para o <strong>longo prazo</strong>, o risco inflacionário torna-se mais relevante.
Nesse contexto, <strong>priorizam-se alocações em títulos atrelados ao IPCA</strong>, que oferecem
proteção contra a inflação e um <strong>prêmio real competitivo</strong>. Essa abordagem complementa
a estratégia Barbell, equilibrando retornos e proteção ao longo do tempo.</p>""",
        curva=_figura("curva-de-juros.png", "Curvas de juros: IPCA, pré-fixados e inflação implícita")))

    pagina(SEC3, T("""<h2>3.2. Ações Nacionais</h2>
<h3>Carteira atual</h3>
@graf@
@coment@""",
        graf=_par(_donut("Concentração por Ativos", "Peso de cada ação na carteira atual."),
                  _donut("Concentração por Setor", "Peso de cada setor na carteira atual.")),
        coment=_texto("comentario_acoes", "Inserir comentários sobre a carteira de ações: concentração "
                      "em ativos e setores e o que será trabalhado na consultoria. Deixe claro, para "
                      "cada ativo, qual dos três destinos ele segue, mantido, aportes congelados ou "
                      "avaliado para venda, com o racional correspondente, inclusive para os congelados. "
                      "Os três únicos casos que justificam venda, a checagem prévia com o time de análise "
                      "e a avaliação tributária obrigatória estão no playbook da R3 (§4.7). Registre no "
                      "relatório que o custo tributário foi considerado.")))

    pagina(SEC3, T("""<h3 class="topo">Estrutura meta proposta</h3>
<p>De forma sucinta, nossa metodologia busca investir em empresas com lucros recorrentes,
<strong>endividamento controlado, vantagens competitivas e posicionadas em setores perenes</strong>.
Na estruturação da carteira, também realizamos uma diversificação setorial, evitando sobreposição de
riscos e priorizando os setores mais resilientes da economia.</p>
<p><strong>Cada ativo recebe uma nota</strong> definida internamente, com base em <strong>critérios
de avaliação específicos para seu setor e no <em>valuation</em> do ativo</strong>. Caso o ativo esteja
mais descontado, sua nota aumenta, o que impacta diretamente o tamanho do aporte. Dessa forma,
<strong>quanto maior a nota de um ativo, maior será sua participação na carteira</strong>, garantindo
uma alocação eficiente e baseada em fundamentos sólidos.</p>
<p>Trabalhamos com a filosofia de Buy &amp; Hold: evitamos girar a carteira sem necessidade, e as
vendas eventualmente recomendadas são sempre graduais, nunca de uma só vez.</p>
@graf@""",
        graf=_par(_donut("Distribuição Setorial", "A carteira de ações deve ser estruturada conforme o "
                         "Manual Renda Variável - AUVP Consultoria. Gráfico de distribuição setorial."),
                  _donut("Exposição por Ativo", "A carteira de ações deve ser estruturada conforme o "
                         "Manual Renda Variável - AUVP Consultoria. Gráfico de exposição por ativo."))))

    pagina(SEC3, T("""<h2>3.3. Fundos Imobiliários</h2>
<h3>Carteira atual</h3>
@graf@
@coment@""",
        graf=_par(_donut("Concentração por Ativos", "Peso de cada fundo na carteira atual."),
                  _donut("Concentração por Segmento", "Peso de cada segmento na carteira atual.")),
        coment=_texto("comentario_fii", "Inserir comentários sobre a carteira de FIIs: concentração por "
                      "ativo e segmento e o que será trabalhado na consultoria. Mesma lógica das ações — "
                      "destino explícito de cada ativo, racional individual por venda e checagem prévia "
                      "com o time de análise (playbook da R3, §4.8). Atenção: o limite mensal de isenção "
                      "de IR para vendas não se aplica a FIIs.")))

    pagina(SEC3, T("""<h3 class="topo">Estrutura meta proposta</h3>
<p>Nos fundos, nossa metodologia consiste em selecionar FIIs com <strong>vários imóveis e
inquilinos</strong>, além de um segmento de atuação sólido e propriedades modernas, portanto,
escolhemos a maior parte dos setores mais perenes nessa classe de ativos.</p>
<p>Acreditamos que os setores de <strong>logística e shoppings</strong> têm maior previsibilidade em
seus resultados, pois trabalham com um público mais B2B, conseguindo assim monetizar mais do que o
setor de Renda Urbana e Lajes Corporativas, que também está voltado para o público B2B, mas é mais
volátil devido às mudanças na economia doméstica.</p>
<p>Shoppings dependem do consumo das famílias e do crescimento do varejo. No entanto,
historicamente, vemos que o brasileiro tem o costume de visitar shoppings como lazer e, por conta
disso, acaba fazendo compras e impulsionando o consumo. Além disso, esse setor tem gerado mais valor do
que as empresas de shopping, como a Aliansce Sonae (ALOS3) e Iguatemi (IGTI11).</p>
<p>Nossa alocação tem foco exclusivo em fundos de tijolo, ou seja, que detêm imóveis físicos. Fundos
de papel, lastreados em dívida, não são utilizados: como a carteira já é bastante ativa em Renda Fixa,
um fundo de papel aumentaria a correlação com a taxa de juros e a volatilidade sem necessidade.</p>
@graf@""",
        graf=_par(_donut("Alocação por Segmento", "A carteira de fundos imobiliários deve ser "
                         "estruturada conforme o Manual Renda Variável - AUVP Consultoria. Gráfico de "
                         "pizza da alocação por segmento.", "56mm"),
                  _donut("Concentração por Ativo", "A carteira de fundos imobiliários deve ser "
                         "estruturada conforme o Manual Renda Variável - AUVP Consultoria. Gráfico de "
                         "concentração por ativo.", "56mm"))))

    pagina(SEC3, T("""<h2>3.4. Internacional</h2>
<h3>Carteira atual</h3>
@graf@
@coment@""",
        graf=_par(_donut("Concentração por Ativos", "Peso de cada ativo na carteira internacional."),
                  _donut("Concentração por Setores", "Peso de cada setor na carteira internacional.")),
        coment=_texto("comentario_intl", "Inserir comentários sobre a carteira internacional: "
                      "concentração por ativo e segmento e o que será trabalhado na consultoria. No "
                      "exterior é comum encontrar sobreposição que parece diversificação e não é (ex.: "
                      "IVV, SPY e VOO, que seguem o mesmo S&P 500) — quando ocorrer, comente por escrito "
                      "e demonstre visualmente. Não venda um ETF que o cliente já tem só para comprar o "
                      "equivalente oficial da casa: a lista de equivalentes validados e o critério de "
                      "quando adotar o modelo UCITS estão no Manual da Carteira Internacional. Apoio: ETF "
                      "Research Center — Fund Overlap.")))

    pagina(SEC3, """<h3 class="topo">Estrutura meta proposta — Renda Fixa Internacional</h3>
<p>A estratégia proposta para a parcela de renda fixa internacional da carteira tem como objetivo
principal gerar liquidez e, ao mesmo tempo, capturar oportunidades em um ambiente de juros ainda
elevados nos Estados Unidos. Atualmente, as taxas de juros americanas permanecem em patamares
consideravelmente acima da média histórica, o que abre espaço para estruturar posições que conciliam
segurança, previsibilidade e flexibilidade na gestão dos recursos.</p>
<p>Para alcançar esse equilíbrio, adotaremos um mix de instrumentos:</p>
<ul class="lista">
  <li>Veículos de alta liquidez (com liquidez próxima a D+1, equivalente a quase liquidez diária), garantindo que parte relevante do portfólio possa ser movimentada rapidamente sempre que necessário.</li>
  <li>Bonds internacionais de alta qualidade (high-grade), selecionados de forma criteriosa. Ressaltamos que não haverá exposição a títulos high-yield, de maior risco, já que o foco é preservar a qualidade do portfólio e buscar uma relação risco-retorno positiva.</li>
</ul>
<p class="apos-lista">A seleção dos bonds seguirá uma análise aprofundada com base nos 4 C’s do crédito
(Capacidade, Garantia, Covenants e Caráter), metodologia amplamente reconhecida e reforçada por
instituições como o CFA Institute. Esse processo reforça o compromisso em manter uma alocação
disciplinada e com fundamentos sólidos.</p>
<p>É importante destacar ainda que, no momento, os spreads de crédito encontram-se bastante
comprimidos, reduzindo a atratividade relativa entre títulos high-grade e high-yield. Nesse contexto,
não faz sentido alongar excessivamente o duration da carteira, uma vez que a simetria de risco para
prazos mais longos não se mostra favorável no cenário atual. Dessa forma, manteremos uma abordagem de
<em>duration</em> moderada, preservando flexibilidade para eventuais ajustes futuros, conforme as
condições de mercado evoluírem.</p>
<p>Em resumo, esta estratégia busca equilibrar liquidez, qualidade de crédito e prudência na gestão
de risco, aproveitando o atual patamar elevado de juros nos EUA para gerar valor ao portfólio do
cliente sem comprometer a segurança patrimonial.</p>""")

    pagina(SEC3, """<p>Atualmente, como opção de Money Market, estamos utilizando o Franklin U.S. Dollar
Short-Term Money Market Fund A (acc) USD, fundo de liquidez internacional gerido pela Franklin
Templeton, uma das maiores gestoras globais independentes. O fundo aplica em ativos de curtíssimo prazo
denominados em dólar, priorizando emissores de alta qualidade de crédito. Sua carteira é composta
principalmente por títulos de dívida corporativa de curto prazo, acordos de recompra – operações
compromissadas, certificados de depósito bancário, além de títulos de agências governamentais e
Treasuries americanos (1%). O portfólio apresenta classificação média de crédito AA, prazo médio
ponderado de vencimento de 24 dias e vida média de 67 dias, assegurando elevada liquidez, preservação
de capital e gestão eficiente dos riscos</p>
<p>Sua estrutura regulatória em Luxemburgo, sob as normas UCITS, assegura elevados padrões de
governança, transparência e controles rigorosos de risco. Dessa forma, a estratégia proporciona alta
liquidez em dólares, ao mesmo tempo em que oferece estabilidade patrimonial, preservando capital e
mantendo flexibilidade para ajustes dinâmicos dentro da carteira global.</p>
<p>A escolha por utilizar Money Market Funds e Bonds internacionais como parte da estratégia de renda
fixa decorre não apenas da busca por liquidez e previsibilidade, mas também por um aspecto estrutural
relevante para investidores globais: ambos os instrumentos não são classificados como US Situs Assets.
Isso significa que eles não estão sujeitos ao Estate Tax norte-americano — o imposto de sucessão
aplicado sobre ativos custodiados nos Estados Unidos.</p>
<p>Enquanto ativos de equity (como Stocks, ETFs e REITs listados nos EUA) são enquadrados como US Situs
Assets e, portanto, passam a estar sujeitos ao imposto sucessório para NRA (Non-Resident Alien -
pessoa física não residente) a partir de um limite de apenas USD 60 mil (com alíquotas progressivas que
podem variar de 18% a 40% sobre o excedente), os Money Markets e Bonds utilizados nesta estratégia
ficam fora desse escopo. Isso garante uma proteção patrimonial adicional, permitindo que o investidor
não precise se preocupar com essa exposição fiscal.</p>
<p>Na prática, essa característica se deve à estrutura de custódia e regulamentação. Os Money Markets
são estabelecidos e regulados em jurisdições como Luxemburgo, fora do ambiente americano. Já os Bonds
contam com a Portfolio Interest Exception, uma regra que concede isenção para investidores não
residentes nos EUA. Assim, além de oferecerem liquidez, solidez de crédito e estabilidade, esses
instrumentos também entregam uma camada extra de eficiência sucessória, tornando-se particularmente
estratégicos em uma carteira global equilibrada.</p>""")

    pagina(SEC3, """<h3 class="topo">Estrutura meta proposta — Internacional Equity</h3>
<p>Na alocação de Equity internacional, optamos por utilizar UCITs de gestão passiva, domiciliados na
Irlanda e em Luxemburgo, em substituição aos ETFs americanos tradicionalmente utilizados nesse
segmento.</p>
<p>A razão central dessa escolha está na questão do Estate Tax americano. Todo investidor não
residente nos Estados Unidos classificado como <strong>NRA</strong> que detenha ativos considerados US
Situs Assets, o que inclui qualquer ação ou ETF listado em bolsa americana, está sujeito ao imposto
sobre herança dos EUA em caso de falecimento, conforme as alíquotas mencionadas acima. Na prática,
para um brasileiro com patrimônio alocado em ETFs, Stocks e REITs americanos acima de <strong>USD 60
mil</strong>, o risco é real, imediato e potencialmente devastador para a transmissão
patrimonial.</p>
<p>Os UCITs domiciliados na Irlanda e em Luxemburgo eliminam integralmente essa exposição. Como são
fundos constituídos em jurisdições europeias e listados nas respectivas bolsas, eles não constituem US
Situs Assets para fins do <strong>IRC §2104</strong>. O falecimento do investidor brasileiro que detém
UCITs irlandeses ou luxemburgueses não acarreta em nenhuma obrigação tributária perante o IRS,
independentemente do valor alocado.</p>
<p>Além da questão sucessória, a estrutura UCITS em formato de acumulação agrega eficiência tributária
relevante. Nos ETFs americanos, os dividendos são distribuídos ao investidor e sofrem retenção na
fonte de <strong>30%</strong> pelo IRS. No formato UCITS, dois mecanismos atuam a favor do investidor:
primeiro, o tratado de dupla tributação entre Irlanda e Estados Unidos reduz a retenção sobre
dividendos de ações americanas dentro do fundo de <strong>30%</strong> para <strong>15%</strong> (no
caso dos UCITs irlandeses); segundo, como o UCIT é de acumulação, esses dividendos são reinvestidos
automaticamente dentro do fundo, sem gerar evento tributável para o investidor brasileiro. O ganho só
será tributado no momento da venda das cotas, permitindo que o efeito de compounding opere de forma
integral ao longo dos anos.</p>
<p>Esses dois elementos combinados, eliminação do Estate Tax e postergação tributária via acumulação,
fazem com que a alocação via UCITs não represente apenas uma troca de veículo. Ela configura uma
melhoria estrutural na arquitetura patrimonial da carteira, especialmente relevante para clientes com
horizonte de longo prazo e preocupação com transmissão de patrimônio.</p>""")

    pagina(SEC3, T("""<h3 class="topo">Estratégia Core-Satellite</h3>
<p>Para organizar a exposição em Equity, aplicamos a estratégia Core-Satellite. O Core (Núcleo) é
composto por UCITs amplos e estáveis, que formam a base sólida da carteira com diversificação global e
previsibilidade. Os Satélites representam uma fatia menor e mais tática, direcionada a setores
específicos, permitindo capturar oportunidades sem comprometer a estabilidade geral do portfólio.</p>
<h3>Contexto de Mercado e Posicionamento</h3>
<p>No cenário atual, optamos por reduzir a concentração em Equity norte-americano, sobretudo na
parcela core da carteira, em função do nível historicamente elevado dos indicadores de valuation.
Métricas amplamente acompanhadas, como o Price-to-Earnings (P/L), o Price-to-Book (P/VP) e o
EV/EBITDA, apontam para múltiplos significativamente acima de suas médias históricas, refletindo um
mercado que negocia em patamares de preço bastante esticados. O P/VP do S&amp;P 500 atingiu 5,3x em
2025, superando inclusive os níveis observados durante a bolha da internet no início dos anos 2000.
Esse descolamento dos fundamentos não implica, necessariamente, em correção imediata, mas aumenta a
probabilidade de retornos abaixo da média nos próximos anos e reduz a margem de segurança para novos
aportes, tornando a simetria de risco claramente menos favorável.</p>
<p>Diante dessa conjuntura, a decisão estratégica é adotar um rebalanceamento tático da exposição
global, com menor peso estrutural nos Estados Unidos e maior diversificação em outras geografias.
Mercados como a Europa apresentam múltiplos mais alinhados às suas médias históricas, configurando um
ambiente de risco-retorno mais equilibrado. A inserção em mercados emergentes e a manutenção de
exposições setoriais seletivas nos EUA complementam a estrutura, capturando oportunidades sem
comprometer a resiliência do portfólio.</p>
@graf@""",
        graf=_par(_donut("Concentração por Ativos", "A carteira de equity deve ser estruturada "
                         "conforme o Manual Proposta Internacional Equity UCITs. Se o cliente quiser "
                         "saber mais sobre os ativos, envie o Entregável UCITs.", "50mm"),
                  _donut("Concentração por Segmentos", "A carteira de equity deve ser estruturada "
                         "conforme o Manual Proposta Internacional Equity UCITs.", "50mm"))))

    pagina(SEC3, T("""<h2>3.5. Fundos de Investimento</h2>
<h3>Carteira atual</h3>
@graf@
<p class="apos-tab">A atual posição em fundos de investimentos gera um ônus significativo para a carteira.
Com a composição acima, o custo total de taxas administrativas totaliza uma média <strong>@taxa@
a.a., equivalente a @reais@ por ano.</strong></p>
<p>Além dos custos administrativos, também há incidência das taxas de performance conforme tabela
abaixo:</p>
@perf@
<p class="apos-tab">Para fundos de renda fixa e multimercados, há ainda o efeito do come-cotas a
antecipação semestral do Imposto de Renda, cobrada no último dia útil de maio e de novembro. O impacto
não é apenas de caixa: o imposto recolhido antes do resgate reduz o capital que continuaria rendendo,
prejudicando a formação de juros compostos e entregando, no acumulado, menos rendimento do que um ativo
tributado somente no resgate.</p>
<p>Trabalhando com uma exposição direta nas classes subjacentes, conseguimos eliminar esses custos
desnecessários e ganhar eficiência nas alocações.</p>
@coment@""",
        graf=_par(_donut("Concentração por Fundos", "Peso de cada fundo na carteira atual.", "52mm"),
                  _donut("Tipos de Fundos", "Renda fixa, multimercado, ações.", "52mm")),
        taxa=ph("fundos_perc_taxa_adm", "N%"), reais=ph("fundos_custo_anual"),
        perf=table(["Benchmark", "Taxa", "Valor", "Percentual (sobre o total)"],
                   [[ph("perf_1_benchmark", "Ex.: 100% do CDI"), ph("perf_1_taxa"), ph("perf_1_valor"),
                     ph("perf_1_perc")]], nums=[1, 2, 3], sm=True),
        coment=_texto("comentario_fundos", "Compare cada fundo com o seu benchmark (CDI, Ibovespa, "
                      "IMA-B, conforme o tipo) e escreva a recomendação: resgate com exposição direta "
                      "nos ativos subjacentes ou portabilidade para fundo de taxas mais baixas, no caso "
                      "de previdência privada. Os dois únicos casos em que recomendamos previdência "
                      "estão no playbook da R2 (§5).")))

    pagina(SEC3, """<h2>3.6. Criptoativos</h2>
<p>Diferente dos ativos tradicionais, criptomoedas como Bitcoin e Ethereum oferecem uma alternativa
descentralizada e independente dos mercados financeiros convencionais. Essa característica as torna
uma opção interessante para proteção contra inflação e desvalorização cambial, especialmente em
cenários de instabilidade econômica. Além disso, a tecnologia blockchain subjacente garante
transparência, imutabilidade e segurança nas transações, reduzindo riscos de fraude e aumentando a
confiança dos investidores.</p>
<p>O mercado de criptoativos tem demonstrado um crescimento expressivo, com adoção crescente por
grandes instituições financeiras e desenvolvimento contínuo de novas aplicações para a tecnologia
blockchain. Dessa forma, alocar uma parcela do portfólio em criptoativos pode não apenas gerar retornos
potencialmente elevados no longo prazo, mas também proporcionar maior diversificação e resiliência em
períodos de volatilidade nos mercados tradicionais.</p>
<p><strong>Bitcoin (BTC)</strong> – Criado em 2009, o Bitcoin é a primeira e mais consolidada
criptomoeda do mercado. Ele opera por meio de uma rede descentralizada, utilizando a tecnologia
<strong>blockchain</strong> para registrar transações de forma transparente e imutável. Sua escassez
programada, com um limite de <strong>21 milhões de unidades</strong>, é um dos principais fatores que
sustentam seu valor ao longo do tempo, tornando-o frequentemente comparado ao ouro digital. Além disso,
sua resistência à censura e independência de bancos centrais fazem do Bitcoin uma opção para
<strong>proteção contra inflação e desvalorização cambial</strong>, sendo cada vez mais adotado por
instituições e grandes investidores como reserva de valor.</p>
<p><strong>Ethereum (ETH)</strong> – Lançado em 2015, o Ethereum expandiu o conceito de blockchain ao
permitir a criação de <strong>contratos inteligentes (smart contracts)</strong> e <strong>aplicativos
descentralizados (DApps)</strong>. Diferente do Bitcoin, que se concentra em ser um meio de troca e
reserva de valor, o Ethereum é uma <strong>plataforma programável</strong>, possibilitando soluções
financeiras descentralizadas (<strong>DeFi</strong>), <strong>tokens não fungíveis (NFTs)</strong> e
muitas outras aplicações. A recente transição para o mecanismo de consenso <strong>Proof of Stake
(PoS)</strong> melhorou sua eficiência energética e abriu novas oportunidades, como o
<strong>staking</strong>, permitindo que os detentores do ativo participem da validação da rede e
obtenham rendimentos passivos.</p>""")

    pagina(SEC3, """<p><strong>Solana (SOL) –</strong> A Solana é uma blockchain altamente escalável, projetada
para suportar milhares de transações por segundo (TPS) com <strong>custos extremamente
baixos</strong>. Utilizando um modelo híbrido de consenso que combina <strong>Proof of History (PoH) e
Proof of Stake (PoS)</strong>, a rede reduz significativamente os tempos de confirmação das
transações, tornando-se uma das principais <strong>concorrentes do Ethereum</strong>. Sua velocidade e
escalabilidade a tornam ideal para aplicações de DeFi, NFTs e games baseados em blockchain, atraindo
desenvolvedores e usuários para o ecossistema.</p>
<p><strong>Chainlink (LINK) –</strong> A Chainlink é uma solução crucial para a
<strong>interoperabilidade entre blockchains e o mundo real</strong>. Sua principal função é operar
como um oráculo descentralizado, permitindo que <strong>contratos inteligentes acessem dados
externos</strong>, como cotações de ativos, condições climáticas, taxas de câmbio e muito mais. Essa
conectividade possibilita a automação segura e confiável de diversas aplicações financeiras e
empresariais, eliminando a necessidade de intermediários centralizados. Com parcerias estratégicas e
adoção crescente, a Chainlink se tornou <strong>essencial para o desenvolvimento do ecossistema
blockchain</strong>, garantindo integridade e precisão das informações usadas em contratos
inteligentes.</p>
<p>Esses criptoativos foram selecionados estrategicamente para compor uma exposição equilibrada ao
mercado digital, combinando ativos consolidados como Bitcoin e Ethereum com soluções inovadoras como
Solana e Chainlink, garantindo diversificação, proteção contra volatilidade e participação no
crescimento da tecnologia blockchain.</p>
<p>Não fazemos trade: também nesta classe a filosofia é buy and hold. A alocação é pequena, buscando
assimetria positiva, sem girar o patrimônio.</p>""")

    # ------------------------------------------------- 4. Fluxo de aplicações
    SEC4 = "4. Fluxo de aplicações"
    pagina(SEC4, """<h1 class="t">4. Fluxo de Aplicações</h1>
<h2>4.1. Metodologia Contrafluxo</h2>
<p>Adotamos uma abordagem gradual e passiva na compra de ativos de renda variável para suavizar os
impactos da volatilidade do mercado, diluindo o risco ao longo do tempo e evitando compras
concentradas em um único cenário. Nossa metodologia, que chamamos de Contrafluxo, é estruturada para
priorizar ativos subvalorizados em relação à alocação meta, o que permite manter um balanceamento
eficiente e focado em controle de risco.</p>
<p>Para um rebalanceamento eficiente, seguimos os seguintes pontos-chave:</p>
<ol class="numerada">
  <li><strong>Concentração Setorial:</strong> Monitoramos a exposição a cada setor para evitar concentrações excessivas, mantendo uma diversificação estratégica entre diferentes setores.</li>
  <li><strong>Concentração em Ativos Específicos:</strong> Controlamos a exposição a cada ativo individual, evitando sobrepesos que podem aumentar o risco da carteira.</li>
  <li><strong>Aportes Graduais:</strong> Realizamos aquisições em volumes menores, sem grandes compras de uma só vez, o que favorece uma alocação mais constante e evita quedas bruscas em caso de volatilidade.</li>
</ol>
<p>Nosso rebalanceamento ocorre principalmente por meio de novos aportes, sem necessidade de vender
ativos, o que permite seguir o movimento natural dos ativos ao longo do tempo, confiando que retornem
às suas médias de volatilidade (altas e baixas). Essa abordagem evita o “abraço” da volatilidade e
mantém o foco na estrutura inicial da carteira, não apenas no preço do ativo.</p>
<p>Em suma, a estratégia é baseada na proporção alvo para cada classe de ativos e na nota de cada
ativo, definida por critérios setoriais específicos. O peso de cada ativo dentro de sua classe é
calculado como a nota do ativo dividida pela soma das notas de todos os ativos naquela classe. Nos
aportes, compramos ativos que estão abaixo do percentual-alvo e evitamos os que estão acima,
privilegiando assim os mais subvalorizados.</p>
<p><strong>Exemplo:</strong> Se a alocação-alvo para um setor é de 10% e ele atinge 13%, o mais
eficiente em termos de risco x retorno é investir em ativos mais descontados dentro da carteira, ao
invés de aumentar a exposição ao setor. Essa metodologia nos permite uma postura contrária ao fluxo de
valorização do mercado, reforçando ativos mais baratos e mantendo o foco na estrutura
preestabelecida.</p>""")

    # As tabelas de compra inicial: o tipo ou o ativo e o valor, e nos ativos
    # também a quantidade. A ferramenta acrescenta quantas linhas o cliente
    # tiver.
    MONTE = "Monte estas tabelas a partir do diagrama do cerrado (Jamel Street)."

    def _ativos(prefixo, n):
        return table(["Ativo", "Valor (Aprox.)", "Quantidade (Aprox.)"],
                     [[ph("%s_%d_ativo" % (prefixo, i), MONTE), ph("%s_%d_valor" % (prefixo, i)),
                       ph("%s_%d_qtd" % (prefixo, i))] for i in range(1, n + 1)],
                     foot=["<strong>Total (Aprox.):</strong>", ph("%s_total" % prefixo), ""],
                     nums=[1, 2], sm=True, widths=[40, 30, 30])

    pagina(SEC4, T("""<h2>4.2. Dinâmica de Entrada</h2>
<p>O valor disponível para investimento representa aproximadamente @pct@ do seu patrimônio investido.
Por isso, em vez de uma única compra, propomos dividir a entrada em @n@ aportes @freq@, mantendo o
recurso ainda não investido em @veic@. Essa dinâmica reduz o risco de concentrar toda a entrada em um
único momento de mercado e mantém o patrimônio com oscilação compatível com o seu perfil ao longo da
montagem.</p>
<h2>4.3. Ativos Recomendados para Compra Inicial</h2>
<p>Após a transferência de custódia, recomendamos que as primeiras compras se concentrem nos ativos de
maior potencial de valorização dentro do seu perfil de investimento e da estratégia Contrafluxo que
utilizamos. Sugerimos começar pelos seguintes ativos:</p>
<p class="item-tab">a) Renda fixa</p>
@rf@
<p class="item-tab">b) Fundos imobiliários</p>
@fii@""",
        pct=ph("entrada_percentual", "Balizador, não trava: a decisão final é do consultor, conforme "
               "perfil, objetivos e momento de mercado, desde que o racional seja explicado e "
               "registrado no relatório. Os exemplos de cálculo, os ajustes finos e o tratamento de "
               "cliente sem aporte recorrente estão no playbook da R3 (§5.3). [x%]"),
        n=ph("entrada_aportes", "[nº]"),
        freq=ph("entrada_frequencia", "[quinzenais/mensais]"),
        veic=ph("entrada_veiculo", "[veículo de liquidez]"),
        rf=table(["Tipo de renda fixa", "Valor (Aprox.)"],
                 [[n, ph("rf_%s_valor" % k, MONTE)] for n, k in
                  [("Pré-fixado", "pre"), ("Inflação (IPCA)", "ipca"), ("Pós-fixado", "pos"),
                   ("Liquidez", "liquidez")]],
                 foot=["<strong>Total (Aprox.):</strong>", ph("rf_total")],
                 nums=[1], sm=True, widths=[60, 40]),
        fii=_ativos("fii", 3)))

    pagina(SEC4, T("""<p class="item-tab topo">c) Ações nacionais</p>
@acoes@
<p class="item-tab">d) Internacional</p>
@intl@""", acoes=_ativos("acao", 5), intl=_ativos("intl", 5)))

    # ------------------------------------------------------ 5. Próximos passos
    pagina("5. Próximos passos", T("""<h1 class="t">5. Próximos Passos</h1>
<h2>5.1. Transferência de Custódia</h2>
<p>Para otimizar a gestão e consolidar o portfólio, o próximo passo será a transferência de custódia
para o BTG Pactual. Esse processo permite centralizar os ativos em uma única plataforma, garantindo
maior controle e eficiência na administração das aplicações.</p>
<h3>Passo a Passo da Transferência de Custódia</h3>
<p>Abaixo, detalhamos as etapas de transferência para cada corretora atualmente utilizada. Se precisar
de suporte durante o processo, entre em contato conosco para orientações personalizadas.</p>
@passos@
<h2>5.2. Dados Bancários</h2>
<p>Abaixo estão os dados da conta na estrutura AUVP Capital / BTG Pactual para onde os recursos devem
ser enviados.</p>
@conta@
<div class="assina">
  @foto@
  <div class="assina-id">
    <div class="nm">@nome@, @cert@</div>
    @logo@
  </div>
</div>""",
        passos=_texto("transferencia_etapas_texto", "Consultar no link: Passo a passo de "
                      "transferências de custódias."),
        conta=_texto("dados_bancarios_texto", "Inserir os dados da conta (investimento ou banking) "
                     "para onde o cliente deve enviar o recurso."),
        foto='<div class="imgbox assina-foto" data-img="%d"><div class="cl">Foto</div></div>' % proximo_img(),
        nome=ph("nome_responsavel"), cert=ph("certificacao_responsavel", "CEA, CFP ou CNPI"),
        logo=logo_svg(t, 7.0, ink=True)))

    return P
