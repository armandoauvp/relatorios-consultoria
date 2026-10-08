# Dicionário de variáveis

Todo campo preenchível aparece nos modelos como `{{nome_da_variavel}}`, destacado em dourado. Substitua o token inteiro, chaves incluídas.

Os nomes são estáveis entre documentos: `{{patrimonio_total}}` significa a mesma coisa no relatório mensal e na versão em apresentação, o que permite preencher vários modelos com a mesma fonte de dados.

Arquivo gerado por `npm run vars`; não edite à mão.

## Convenções

| Padrão | Significado | Exemplo |
| --- | --- | --- |
| `nome_do_campo` | valor único | `{{nome_cliente}}` |
| `bloco_N_campo` | linha `N` de uma lista ou tabela | `{{mov_3_ativo}}` |
| `prefixo_chave_metrica` | célula de uma tabela de referência fixa | `{{alvo_rf_pos}}` |
| `texto_*`, `analise_*`, `comentario_*` | texto corrido escrito pelo responsável | `{{texto_desvio_alocacao}}` |

Linhas sobrando numa tabela (por exemplo, só houve 3 movimentações e o modelo traz 6 linhas) devem ser apagadas do HTML, não deixadas com o token à mostra.

## Campos institucionais e recorrentes

Estes se repetem na maior parte dos modelos. Vale manter um arquivo único com eles e aplicar em lote antes de partir para o conteúdo específico de cada documento.

| Variável | O que é | Em quantos modelos |
| --- | --- | --- |
| `razao_social` | Razão social da empresa emissora | 24 de 39 |
| `cnpj` | CNPJ da empresa emissora | 24 de 39 |
| `registro_cvm_empresa` | Registro da empresa na CVM | 4 de 39 |
| `canal_ouvidoria` | Telefone ou e-mail da ouvidoria | 24 de 39 |
| `disclaimer_regulatorio` | Texto legal aprovado pelo compliance, específico do segmento | 24 de 39 |
| `nome_cliente` | Nome do cliente destinatário | 30 de 39 |
| `nome_responsavel` | Consultor, assessor ou banker responsável | 30 de 39 |
| `registro_cvm_ou_ancord` | Registro do responsável (CVM 19 / Ancord) | 12 de 39 |
| `email_contato` | E-mail de contato exibido no documento | 29 de 39 |
| `whatsapp_contato` | WhatsApp direto do responsável | 13 de 39 |
| `canal_atendimento` | Canal e horário de atendimento | 12 de 39 |
| `link_agendamento` | URL de agendamento (a mesma do QR code) | 8 de 39 |
| `mes_referencia` | Mês de referência, ex.: Agosto de 2026 | 12 de 39 |
| `data_posicao` | Data da posição consolidada | 8 de 39 |
| `perfil_investidor` | Perfil de suitability do cliente | 12 de 39 |
| `patrimonio_total` | Patrimônio total sob acompanhamento | 8 de 39 |

## Apresentação do consultor — Me Diz o Que Fazer

Arquivos: `modelos/apresentacao-consultor-me-diz-o-que-fazer.html`, `modelos/apresentacao-consultor-simples-alta-renda.html`, `modelos/apresentacao-consultor-simples-assessoria.html`, `modelos/apresentacao-consultor-simples-consultoria.html`, `modelos/apresentacao-consultor-simples-private.html`

Variantes: me-diz-o-que-fazer, simples-alta-renda, simples-assessoria, simples-consultoria, simples-private &middot; 39 variáveis

<details><summary>Ver as 39 variáveis específicas deste documento</summary>

```
nome_consultor                    papel_consultor                   frase_consultor
formacao_1                        formacao_2                        formacao_3
formacao_4                        formacao_5                        especializacao_1
especializacao_2                  especializacao_3                  especializacao_4
especializacao_5                  certificacao_1                    certificacao_2
certificacao_3                    certificacao_4                    certificacao_5
proposito_1                       proposito_2                       proposito_3
proposito_4                       qualificacoes_1                   qualificacoes_2
trajetoria_1                      trajetoria_2                      trajetoria_3
marco_1_quando                    marco_1_texto                     marco_2_quando
marco_2_texto                     marco_3_quando                    marco_3_texto
fora_do_escritorio_1              fora_do_escritorio_2              fora_do_escritorio_3
whatsapp_consultor                email_consultor                   data_apresentacao
```
</details>

Campos exclusivos da variante **simples-alta-renda** (1):

```
instagram_consultor
```

Campos exclusivos da variante **simples-assessoria** (1):

```
instagram_consultor
```

Campos exclusivos da variante **simples-consultoria** (1):

```
instagram_consultor
```

Campos exclusivos da variante **simples-private** (1):

```
instagram_consultor
```

## Apresentação geral

Arquivos: `modelos/apresentacao-geral-alta-renda.html`, `modelos/apresentacao-geral-assessoria.html`, `modelos/apresentacao-geral-consultoria.html`, `modelos/apresentacao-geral-private.html`

Variantes: alta-renda, assessoria, consultoria, private &middot; 36 variáveis

<details><summary>Ver as 26 variáveis específicas deste documento</summary>

```
subtitulo_apresentacao            data_apresentacao                 prazo_implantacao
reuniao_1_data                    reuniao_2_data                    reuniao_3_data
reuniao_4_data                    reuniao_5_data                    reuniao_6_data
entregas_detalhe                  pessoa_1_nome                     pessoa_1_cargo
pessoa_1_bio                      pessoa_2_nome                     pessoa_2_cargo
pessoa_2_bio                      pessoa_3_nome                     pessoa_3_cargo
pessoa_3_bio                      passo_1_detalhe                   passo_2_detalhe
passo_3_detalhe                   passo_4_detalhe                   chamada_final
site                              endereco_escritorio
```
</details>

Campos exclusivos da variante **consultoria** (34):

```
nota_taxas                        plano_1_base_calculo              plano_1_item_1
plano_1_item_2                    plano_1_item_3                    plano_1_item_4
plano_1_item_5                    plano_1_item_6                    plano_1_nome
plano_1_para_quem                 plano_1_tag                       plano_1_taxa
plano_2_base_calculo              plano_2_item_1                    plano_2_item_2
plano_2_item_3                    plano_2_item_4                    plano_2_item_5
plano_2_item_6                    plano_2_nome                      plano_2_para_quem
plano_2_tag                       plano_2_taxa                      plano_3_base_calculo
plano_3_item_1                    plano_3_item_2                    plano_3_item_3
plano_3_item_4                    plano_3_item_5                    plano_3_item_6
plano_3_nome                      plano_3_para_quem                 plano_3_tag
plano_3_taxa
```

## undefined

Arquivos: `modelos/apresentacao-livre-alta-renda.html`

Variantes: — &middot; 10 variáveis

<details><summary>Ver as 2 variáveis específicas deste documento</summary>

```
capa_linha_livre                  data_documento
```
</details>

## undefined

Arquivos: `modelos/apresentacao-livre-assessoria.html`

Variantes: — &middot; 10 variáveis

<details><summary>Ver as 2 variáveis específicas deste documento</summary>

```
capa_linha_livre                  data_documento
```
</details>

## undefined

Arquivos: `modelos/apresentacao-livre-consultoria.html`

Variantes: — &middot; 10 variáveis

<details><summary>Ver as 2 variáveis específicas deste documento</summary>

```
capa_linha_livre                  data_documento
```
</details>

## undefined

Arquivos: `modelos/apresentacao-livre-private.html`

Variantes: — &middot; 10 variáveis

<details><summary>Ver as 2 variáveis específicas deste documento</summary>

```
capa_linha_livre                  data_documento
```
</details>

## undefined

Arquivos: `modelos/carta-apresentacao-alta-renda.html`

Variantes: — &middot; 12 variáveis

<details><summary>Ver as 7 variáveis específicas deste documento</summary>

```
subtitulo_carta                   data_carta                        data_primeira_reuniao
momento_do_cliente                objetivo_principal                frase_de_abertura
taxa_anual
```
</details>

## undefined

Arquivos: `modelos/carta-apresentacao-assessoria.html`

Variantes: — &middot; 12 variáveis

<details><summary>Ver as 7 variáveis específicas deste documento</summary>

```
subtitulo_carta                   data_carta                        data_primeira_reuniao
momento_do_cliente                objetivo_principal                frase_de_abertura
nota_remuneracao
```
</details>

## undefined

Arquivos: `modelos/carta-apresentacao-consultoria.html`

Variantes: — &middot; 12 variáveis

<details><summary>Ver as 7 variáveis específicas deste documento</summary>

```
subtitulo_carta                   data_carta                        data_primeira_reuniao
momento_do_cliente                objetivo_principal                frase_de_abertura
taxa_anual
```
</details>

## undefined

Arquivos: `modelos/carta-apresentacao-private.html`

Variantes: — &middot; 12 variáveis

<details><summary>Ver as 7 variáveis específicas deste documento</summary>

```
subtitulo_carta                   data_carta                        data_primeira_reuniao
momento_do_cliente                objetivo_principal                frase_de_abertura
taxa_anual
```
</details>

## Diagnóstico de carteira

Arquivos: `modelos/diagnostico-carteira-alta-renda.html`, `modelos/diagnostico-carteira-assessoria.html`, `modelos/diagnostico-carteira-consultoria.html`, `modelos/diagnostico-carteira-private.html`

Variantes: alta-renda, assessoria, consultoria, private &middot; 115 variáveis

<details><summary>Ver as 112 variáveis específicas deste documento</summary>

```
contexto_cliente                  contexto_trabalho                 contexto_consideracoes
objetivo_mestre_texto             objetivos_secundarios_texto       pat_financeiro_valor
pat_financeiro_dist               pat_imobilizado_valor             pat_imobilizado_dist
pat_liquidez_valor                pat_liquidez_dist                 cenario_carteira
comentario_carteira               comparacao_1_classe               comparacao_1_atual
comparacao_1_meta                 comparacao_2_classe               comparacao_2_atual
comparacao_2_meta                 comparacao_redirecionamento       comparacao_mantidas
valor_renda_passiva               valor_patrimonio_necessario       valor_patrimonio_inicial
valor_aporte_mensal               qtd_meses_objetivo                valor_reserva_emergencia
protecao_gatilho_texto            protecao_seguro_texto             pgbl_situacao
valor_renda_mensal                protecao_recomendacao             rf_pre_taxa
rf_pre_valor_atual                rf_pre_perc                       rf_ipca_taxa
rf_ipca_valor_atual               rf_ipca_perc                      rf_pcdi_taxa
rf_pcdi_valor_atual               rf_pcdi_perc                      rf_cdimais_taxa
rf_cdimais_valor_atual            rf_cdimais_perc                   rf_selic_taxa
rf_selic_valor_atual              rf_selic_perc                     comentario_rf
comentario_acoes                  comentario_fii                    comentario_intl
fundos_perc_taxa_adm              fundos_custo_anual                perf_1_benchmark
perf_1_taxa                       perf_1_valor                      perf_1_perc
comentario_fundos                 entrada_percentual                entrada_aportes
entrada_frequencia                entrada_veiculo                   rf_pre_valor
rf_ipca_valor                     rf_pos_valor                      rf_liquidez_valor
rf_total                          fii_1_ativo                       fii_1_valor
fii_1_qtd                         fii_2_ativo                       fii_2_valor
fii_2_qtd                         fii_3_ativo                       fii_3_valor
fii_3_qtd                         fii_total                         acao_1_ativo
acao_1_valor                      acao_1_qtd                        acao_2_ativo
acao_2_valor                      acao_2_qtd                        acao_3_ativo
acao_3_valor                      acao_3_qtd                        acao_4_ativo
acao_4_valor                      acao_4_qtd                        acao_5_ativo
acao_5_valor                      acao_5_qtd                        acao_total
intl_1_ativo                      intl_1_valor                      intl_1_qtd
intl_2_ativo                      intl_2_valor                      intl_2_qtd
intl_3_ativo                      intl_3_valor                      intl_3_qtd
intl_4_ativo                      intl_4_valor                      intl_4_qtd
intl_5_ativo                      intl_5_valor                      intl_5_qtd
intl_total                        transferencia_etapas_texto        dados_bancarios_texto
certificacao_responsavel
```
</details>

## undefined

Arquivos: `modelos/documento-livre-alta-renda.html`

Variantes: — &middot; 11 variáveis

<details><summary>Ver as 2 variáveis específicas deste documento</summary>

```
capa_linha_livre                  data_documento
```
</details>

## undefined

Arquivos: `modelos/documento-livre-assessoria.html`

Variantes: — &middot; 11 variáveis

<details><summary>Ver as 2 variáveis específicas deste documento</summary>

```
capa_linha_livre                  data_documento
```
</details>

## undefined

Arquivos: `modelos/documento-livre-consultoria.html`

Variantes: — &middot; 11 variáveis

<details><summary>Ver as 2 variáveis específicas deste documento</summary>

```
capa_linha_livre                  data_documento
```
</details>

## undefined

Arquivos: `modelos/documento-livre-private.html`

Variantes: — &middot; 11 variáveis

<details><summary>Ver as 2 variáveis específicas deste documento</summary>

```
capa_linha_livre                  data_documento
```
</details>

## Relatório macroeconômico

Arquivos: `modelos/relatorio-macroeconomico-alta-renda.html`, `modelos/relatorio-macroeconomico-assessoria.html`, `modelos/relatorio-macroeconomico-consultoria.html`, `modelos/relatorio-macroeconomico-private.html`

Variantes: alta-renda, assessoria, consultoria, private &middot; 181 variáveis

<details><summary>Ver as 175 variáveis específicas deste documento</summary>

```
registro_analista                 titulo_do_mes                     resumo_executivo
mes_fechamento                    painel_1_valor                    painel_1_nota
painel_2_valor                    painel_2_nota                     painel_3_valor
painel_3_nota                     painel_4_valor                    painel_4_nota
painel_5_valor                    painel_5_nota                     painel_6_valor
painel_6_nota                     painel_7_valor                    painel_7_nota
painel_8_valor                    painel_8_nota                     fonte_painel
destaque_1_titulo                 destaque_1_texto                  destaque_2_titulo
destaque_2_texto                  destaque_3_titulo                 destaque_3_texto
destaque_4_titulo                 destaque_4_texto                  destaque_5_titulo
destaque_5_texto                  analise_brasil_titulo             analise_brasil_1_subtitulo
analise_brasil_1_texto            analise_brasil_2_subtitulo        analise_brasil_2_texto
analise_tema1_titulo              analise_tema1_lead                analise_tema1_1_subtitulo
analise_tema1_1_texto             analise_tema1_fonte               analise_tema1_col_1
analise_tema1_col_2               analise_tema1_col_3               analise_tema1_col_4
analise_tema1_1_1                 analise_tema1_1_2                 analise_tema1_1_3
analise_tema1_1_4                 analise_tema1_2_1                 analise_tema1_2_2
analise_tema1_2_3                 analise_tema1_2_4                 analise_tema1_3_1
analise_tema1_3_2                 analise_tema1_3_3                 analise_tema1_3_4
analise_tema1_4_1                 analise_tema1_4_2                 analise_tema1_4_3
analise_tema1_4_4                 analise_tema1_5_1                 analise_tema1_5_2
analise_tema1_5_3                 analise_tema1_5_4                 analise_tema2_titulo
analise_tema2_lead                analise_tema2_1_subtitulo         analise_tema2_1_texto
analise_tema2_2_subtitulo         analise_tema2_2_texto             global_1_subtitulo
global_1_texto                    global_2_subtitulo                global_2_texto
global_3_subtitulo                global_3_texto                    analise_tema3_titulo
analise_tema3_lead                analise_tema3_texto_1             analise_tema3_texto_2
carteira_lead                     pos_1_posicao                     pos_1_racional
pos_2_posicao                     pos_2_racional                    pos_3_posicao
pos_3_racional                    pos_4_posicao                     pos_4_racional
classe_rf_1_rotulo                classe_rf_1_texto                 classe_rf_2_rotulo
classe_rf_2_texto                 classe_rf_3_rotulo                classe_rf_3_texto
classe_rf_4_rotulo                classe_rf_4_texto                 classe_rv_1_rotulo
classe_rv_1_texto                 classe_rv_2_rotulo                classe_rv_2_texto
classe_rv_3_rotulo                classe_rv_3_texto                 classe_fii_1_rotulo
classe_fii_1_texto                classe_fii_2_rotulo               classe_fii_2_texto
classe_intl_1_rotulo              classe_intl_1_texto               classe_intl_2_rotulo
classe_intl_2_texto               classe_intl_3_rotulo              classe_intl_3_texto
classe_cripto_1_rotulo            classe_cripto_1_texto             fech_cdi_mes
fech_cdi_ano                      fech_ibov_mes                     fech_ibov_ano
fech_imab_mes                     fech_imab_ano                     fech_ifix_mes
fech_ifix_ano                     fech_dolar_mes                    fech_dolar_ano
fech_ipca_mes                     fech_ipca_ano                     fechamento_nota
riscos_lead                       risco_1_titulo                    risco_1_texto
risco_1_acao                      risco_2_titulo                    risco_2_texto
risco_2_acao                      risco_3_titulo                    risco_3_texto
risco_3_acao                      risco_4_titulo                    risco_4_texto
risco_4_acao                      risco_5_titulo                    risco_5_texto
risco_5_acao                      oportunidade_1_titulo             oportunidade_1_texto
oportunidade_1_acao               oportunidade_2_titulo             oportunidade_2_texto
oportunidade_2_acao               oportunidade_3_titulo             oportunidade_3_texto
oportunidade_3_acao               ag_1_data                         ag_1_evento
ag_1_motivo                       ag_2_data                         ag_2_evento
ag_2_motivo                       ag_3_data                         ag_3_evento
ag_3_motivo                       ag_4_data                         ag_4_evento
ag_4_motivo                       ag_5_data                         ag_5_evento
ag_5_motivo                       perspectivas_texto                sintese_1
sintese_2                         sintese_3                         fonte_indicadores
fonte_cenarios
```
</details>

## Relatório mensal

Arquivos: `modelos/relatorio-mensal-alta-renda.html`, `modelos/relatorio-mensal-assessoria.html`, `modelos/relatorio-mensal-consultoria.html`, `modelos/relatorio-mensal-private.html`

Variantes: alta-renda, assessoria, consultoria, private &middot; 381 variáveis

<details><summary>Ver as 368 variáveis específicas deste documento</summary>

```
carta_paragrafo_1                 carta_paragrafo_2                 carta_paragrafo_3
telefone_contato                  rent_mes                          rent_ano
rent_12m                          rent_inicio                       ganho_mes_reais
ganho_ano_reais                   aplicacoes_mes                    resgates_mes
aporte_liquido_mes                total_proventos                   rent_24m
ipca5_mes                         ipca5_ano                         ipca5_12m
ipca5_24m                         ipca5_inicio                      ibov_mes
ibov_ano                          ibov_12m                          ibov_24m
ibov_inicio                       cls_rf_valor                      cls_rf_perc
cls_rf_variacao                   cls_rf_resultado                  cls_rfi_valor
cls_rfi_perc                      cls_rfi_variacao                  cls_rfi_resultado
cls_acoes_valor                   cls_acoes_perc                    cls_acoes_variacao
cls_acoes_resultado               cls_fii_valor                     cls_fii_perc
cls_fii_variacao                  cls_fii_resultado                 cls_rvi_valor
cls_rvi_perc                      cls_rvi_variacao                  cls_rvi_resultado
cls_cripto_valor                  cls_cripto_perc                   cls_cripto_variacao
cls_cripto_resultado              cls_caixa_valor                   cls_caixa_perc
cls_caixa_variacao                cls_caixa_resultado               variacao_total
resultado_total                   cust_1_nome                       cust_1_valor
cust_1_perc                       cust_1_classes                    cust_2_nome
cust_2_valor                      cust_2_perc                       cust_2_classes
cust_3_nome                       cust_3_valor                      cust_3_perc
cust_3_classes                    cust_4_nome                       cust_4_valor
cust_4_perc                       cust_4_classes                    alvo_rf_pos
atual_rf_pos                      desvio_rf_pos                     valor_rf_pos
status_rf_pos                     alvo_rf_pre                       atual_rf_pre
desvio_rf_pre                     valor_rf_pre                      status_rf_pre
alvo_rf_ipca                      atual_rf_ipca                     desvio_rf_ipca
valor_rf_ipca                     status_rf_ipca                    alvo_multi
atual_multi                       desvio_multi                      valor_multi
status_multi                      alvo_rv_br                        atual_rv_br
desvio_rv_br                      valor_rv_br                       status_rv_br
alvo_intl                         atual_intl                        desvio_intl
valor_intl                        status_intl                       alvo_fii
atual_fii                         desvio_fii                        valor_fii
status_fii                        alvo_alt                          atual_alt
desvio_alt                        valor_alt                         status_alt
alvo_caixa                        atual_caixa                       desvio_caixa
valor_caixa                       status_caixa                      data_inicio_periodo
data_fim_periodo                  mov_1_data                        mov_1_tipo
mov_1_ativo                       mov_1_classe                      mov_1_qtd
mov_1_valor                       mov_1_motivo                      mov_2_data
mov_2_tipo                        mov_2_ativo                       mov_2_classe
mov_2_qtd                         mov_2_valor                       mov_2_motivo
mov_3_data                        mov_3_tipo                        mov_3_ativo
mov_3_classe                      mov_3_qtd                         mov_3_valor
mov_3_motivo                      mov_4_data                        mov_4_tipo
mov_4_ativo                       mov_4_classe                      mov_4_qtd
mov_4_valor                       mov_4_motivo                      mov_5_data
mov_5_tipo                        mov_5_ativo                       mov_5_classe
mov_5_qtd                         mov_5_valor                       mov_5_motivo
mov_6_data                        mov_6_tipo                        mov_6_ativo
mov_6_classe                      mov_6_qtd                         mov_6_valor
mov_6_motivo                      prov_1_data                       prov_1_origem
prov_1_tipo                       prov_1_bruto                      prov_1_ir
prov_1_liquido                    prov_2_data                       prov_2_origem
prov_2_tipo                       prov_2_bruto                      prov_2_ir
prov_2_liquido                    prov_3_data                       prov_3_origem
prov_3_tipo                       prov_3_bruto                      prov_3_ir
prov_3_liquido                    prov_4_data                       prov_4_origem
prov_4_tipo                       prov_4_bruto                      prov_4_ir
prov_4_liquido                    prov_total_bruto                  prov_total_ir
liq_d0_valor                      liq_d0_perc_rf                    liq_d0_perc_pat
liq_d0_acum                       liq_d0_obs                        liq_d30_valor
liq_d30_perc_rf                   liq_d30_perc_pat                  liq_d30_acum
liq_d30_obs                       liq_d60_valor                     liq_d60_perc_rf
liq_d60_perc_pat                  liq_d60_acum                      liq_d60_obs
liq_d90_valor                     liq_d90_perc_rf                   liq_d90_perc_pat
liq_d90_acum                      liq_d90_obs                       liq_d180_valor
liq_d180_perc_rf                  liq_d180_perc_pat                 liq_d180_acum
liq_d180_obs                      liq_a1_valor                      liq_a1_perc_rf
liq_a1_perc_pat                   liq_a1_acum                       liq_a1_obs
liq_a2_valor                      liq_a2_perc_rf                    liq_a2_perc_pat
liq_a2_acum                       liq_a2_obs                        liq_a3_valor
liq_a3_perc_rf                    liq_a3_perc_pat                   liq_a3_acum
liq_a3_obs                        liq_a4_valor                      liq_a4_perc_rf
liq_a4_perc_pat                   liq_a4_acum                       liq_a4_obs
liq_a5_valor                      liq_a5_perc_rf                    liq_a5_perc_pat
liq_a5_acum                       liq_a5_obs                        liq_a5mais_valor
liq_a5mais_perc_rf                liq_a5mais_perc_pat               liq_a5mais_acum
liq_a5mais_obs                    banco_1_nome                      banco_1_valor
banco_1_perc_rf                   banco_1_perc_pat                  banco_1_rating
banco_1_fgc                       banco_1_margem                    banco_2_nome
banco_2_valor                     banco_2_perc_rf                   banco_2_perc_pat
banco_2_rating                    banco_2_fgc                       banco_2_margem
banco_3_nome                      banco_3_valor                     banco_3_perc_rf
banco_3_perc_pat                  banco_3_rating                    banco_3_fgc
banco_3_margem                    banco_4_nome                      banco_4_valor
banco_4_perc_rf                   banco_4_perc_pat                  banco_4_rating
banco_4_fgc                       banco_4_margem                    banco_5_nome
banco_5_valor                     banco_5_perc_rf                   banco_5_perc_pat
banco_5_rating                    banco_5_fgc                       banco_5_margem
banco_total_valor                 banco_total_perc_rf               banco_total_perc_pat
banco_total_fgc                   privado_1_nome                    privado_1_valor
privado_1_perc_rf                 privado_1_perc_pat                privado_1_rating
privado_1_setor                   privado_1_vencimento              privado_2_nome
privado_2_valor                   privado_2_perc_rf                 privado_2_perc_pat
privado_2_rating                  privado_2_setor                   privado_2_vencimento
privado_3_nome                    privado_3_valor                   privado_3_perc_rf
privado_3_perc_pat                privado_3_rating                  privado_3_setor
privado_3_vencimento              privado_4_nome                    privado_4_valor
privado_4_perc_rf                 privado_4_perc_pat                privado_4_rating
privado_4_setor                   privado_4_vencimento              privado_5_nome
privado_5_valor                   privado_5_perc_rf                 privado_5_perc_pat
privado_5_rating                  privado_5_setor                   privado_5_vencimento
privado_total_valor               privado_total_perc_rf             privado_total_perc_pat
texto_limite_emissor              bolsa_1_recorte                   bolsa_1_valor
bolsa_1_perc_bolsa                bolsa_1_perc_carteira             bolsa_1_resultado
bolsa_2_recorte                   bolsa_2_valor                     bolsa_2_perc_bolsa
bolsa_2_perc_carteira             bolsa_2_resultado                 bolsa_3_recorte
bolsa_3_valor                     bolsa_3_perc_bolsa                bolsa_3_perc_carteira
bolsa_3_resultado                 bolsa_4_recorte                   bolsa_4_valor
bolsa_4_perc_bolsa                bolsa_4_perc_carteira             bolsa_4_resultado
bolsa_5_recorte                   bolsa_5_valor                     bolsa_5_perc_bolsa
bolsa_5_perc_carteira             bolsa_5_resultado                 bolsa_total_valor
bolsa_total_perc_carteira         bolsa_total_resultado             data_ptax
intl_total_usd                    intl_total_brl                    intl_perc_patrimonio
ptax_utilizada                    intl_rf_usd                       intl_rf_brl
intl_rf_perc_ext                  intl_rf_perc_cart                 intl_acoes_usd
intl_acoes_brl                    intl_acoes_perc_ext               intl_acoes_perc_cart
intl_reits_usd                    intl_reits_brl                    intl_reits_perc_ext
intl_reits_perc_cart              intl_caixa_usd                    intl_caixa_brl
intl_caixa_perc_ext               intl_caixa_perc_cart
```
</details>

Campos exclusivos da variante **assessoria** (35):

```
remun_1_classe                    remun_1_forma                     remun_1_perc
remun_1_posicao                   remun_1_produto                   remun_1_valor
remun_2_classe                    remun_2_forma                     remun_2_perc
remun_2_posicao                   remun_2_produto                   remun_2_valor
remun_3_classe                    remun_3_forma                     remun_3_perc
remun_3_posicao                   remun_3_produto                   remun_3_valor
remun_4_classe                    remun_4_forma                     remun_4_perc
remun_4_posicao                   remun_4_produto                   remun_4_valor
remun_5_classe                    remun_5_forma                     remun_5_perc
remun_5_posicao                   remun_5_produto                   remun_5_valor
remun_equivalente_ano             remun_total                       remun_total_perc
texto_como_ler_remuneracao        texto_conflito_interesse
```

## Relatório mensal em formato de apresentação

Arquivos: `modelos/relatorio-mensal-apresentacao-alta-renda.html`, `modelos/relatorio-mensal-apresentacao-assessoria.html`, `modelos/relatorio-mensal-apresentacao-consultoria.html`, `modelos/relatorio-mensal-apresentacao-private.html`

Variantes: alta-renda, assessoria, consultoria, private &middot; 154 variáveis

<details><summary>Ver as 141 variáveis específicas deste documento</summary>

```
duracao_reuniao                   rent_mes                          rent_ano
rent_12m                          rent_24m                          aporte_liquido_mes
resgates_mes                      resumo_do_mes                     ponto_de_atencao_mes
ipca5_mes                         ipca5_ano                         ipca5_12m
ipca5_24m                         ibov_mes                          ibov_ano
ibov_12m                          ibov_24m                          alvo_rf_pos
atual_rf_pos                      desvio_rf_pos                     alvo_rf_ipca
atual_rf_ipca                     desvio_rf_ipca                    alvo_rf_pre
atual_rf_pre                      desvio_rf_pre                     alvo_multi
atual_multi                       desvio_multi                      alvo_rv_br
atual_rv_br                       desvio_rv_br                      alvo_intl
atual_intl                        desvio_intl                       alvo_fii
atual_fii                         desvio_fii                        alvo_alt
atual_alt                         desvio_alt                        alvo_caixa
atual_caixa                       desvio_caixa                      texto_rebalanceamento
mov_1_data                        mov_1_tipo                        mov_1_ativo
mov_1_classe                      mov_1_valor                       mov_1_motivo
mov_2_data                        mov_2_tipo                        mov_2_ativo
mov_2_classe                      mov_2_valor                       mov_2_motivo
mov_3_data                        mov_3_tipo                        mov_3_ativo
mov_3_classe                      mov_3_valor                       mov_3_motivo
mov_4_data                        mov_4_tipo                        mov_4_ativo
mov_4_classe                      mov_4_valor                       mov_4_motivo
mov_5_data                        mov_5_tipo                        mov_5_ativo
mov_5_classe                      mov_5_valor                       mov_5_motivo
total_aportes                     total_resgates                    total_proventos
total_custos                      custo_perc_patrimonio             seg_1_item
seg_1_detalhe                     seg_1_valor                       seg_1_perc
seg_1_obs                         seg_2_item                        seg_2_detalhe
seg_2_valor                       seg_2_perc                        seg_2_obs
seg_3_item                        seg_3_detalhe                     seg_3_valor
seg_3_perc                        seg_3_obs                         seg_4_item
seg_4_detalhe                     seg_4_valor                       seg_4_perc
seg_4_obs                         seg_5_item                        seg_5_detalhe
seg_5_valor                       seg_5_perc                        seg_5_obs
cenario_brasil                    cenario_internacional             pos_rfpos_visao
pos_rfpos_mov                     pos_rfpos_racional                pos_rfipca_visao
pos_rfipca_mov                    pos_rfipca_racional               pos_rvbr_visao
pos_rvbr_mov                      pos_rvbr_racional                 pos_intl_visao
pos_intl_mov                      pos_intl_racional                 pos_alt_visao
pos_alt_mov                       pos_alt_racional                  acao_1_prioridade
acao_1_descricao                  acao_1_prazo                      acao_2_prioridade
acao_2_descricao                  acao_2_prazo                      acao_3_prioridade
acao_3_descricao                  acao_3_prazo                      acao_4_prioridade
acao_4_descricao                  acao_4_prazo                      pendencia_1_titulo
pendencia_1_detalhe               pendencia_2_titulo                pendencia_2_detalhe
data_proxima_reuniao              formato_reuniao                   mensagem_encerramento
```
</details>

## undefined

Arquivos: `modelos/wealth-proposta-private.html`

Variantes: — &middot; 7 variáveis

<details><summary>Ver as 3 variáveis específicas deste documento</summary>

```
data_proposta                     valor_epwp                        valor_roadmap
```
</details>

## undefined

Arquivos: `modelos/wealth-snapshot-private.html`

Variantes: — &middot; 89 variáveis

<details><summary>Ver as 87 variáveis específicas deste documento</summary>

```
data_snapshot                     perfil_1                          perfil_2
perfil_3                          perfil_4                          perfil_5
perfil_6                          perfil_7                          perfil_8
ind_1_valor                       ind_2_valor                       ind_3_valor
ind_4_valor                       ind_5_valor                       ind_6_valor
ind_7_valor                       ind_8_valor                       conclusao_1_titulo
conclusao_1_texto                 conclusao_2_titulo                conclusao_2_texto
conclusao_3_titulo                conclusao_3_texto                 conclusao_4_titulo
conclusao_4_texto                 nucleo_pf_texto                   nucleo_imob_texto
nucleo_geracao_texto              nucleo_empresas_texto             consumo_dado_1
consumo_dado_2                    consumo_dado_3                    consumo_dado_4
consumo_dado_5                    consumo_dado_6                    consumo_leitura
consumo_criterio_6                ir_contexto_1                     ir_contexto_2
ir_contexto_3                     ir_contexto_4                     ir_contexto_5
sucessao_elemento_1               sucessao_elemento_2               sucessao_elemento_3
sucessao_elemento_4               sucessao_elemento_5               sucessao_elemento_6
sucessao_elemento_7               sucessao_questao_1                sucessao_questao_2
sucessao_questao_3                sucessao_questao_4                sucessao_questao_5
sucessao_questao_6                sucessao_questao_7                governanca_contexto_1
governanca_contexto_2             governanca_contexto_3             governanca_contexto_4
governanca_contexto_5             eficiencia_contexto_1             eficiencia_contexto_2
eficiencia_contexto_3             eficiencia_contexto_4             fr_1_prioridade
fr_1_frente                       fr_1_conteudo                     fr_2_prioridade
fr_2_frente                       fr_2_conteudo                     fr_3_prioridade
fr_3_frente                       fr_3_conteudo                     fr_4_prioridade
fr_4_frente                       fr_4_conteudo                     fr_5_prioridade
fr_5_frente                       fr_5_conteudo                     fr_6_prioridade
fr_6_frente                       fr_6_conteudo                     roadmap_1_texto
roadmap_2_texto                   roadmap_3_texto                   roadmap_4_texto
```
</details>

