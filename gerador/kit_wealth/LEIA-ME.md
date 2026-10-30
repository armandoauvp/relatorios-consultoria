# Kit AUVP Wealth

Os modelos e o guia de marca para produzir os documentos da AUVP Wealth com o Claude
Code. Com o kit, todo documento sai no mesmo padrão: mesma capa, mesma tipografia,
mesmas cores e o mesmo disclaimer, seja quem for que o produza.

## Instalar (uma vez)

Precisa do [Node.js](https://nodejs.org) 18 ou mais novo e do Claude Code.

1. Descompacte o zip numa pasta de trabalho.
2. Abra um terminal nessa pasta e rode:

   ```bash
   npm install
   ```

   O script de PDF usa o Chrome ou o Edge já instalados. Se não houver nenhum dos dois,
   rode também `npx playwright install chromium`.

## Usar

Abra o Claude Code nessa pasta e peça o documento, mandando junto o material do cliente.
Por exemplo:

> Monte a proposta de Wealth Planning para Maria e João Silva, identidade verde. Valor do
> EPWP R$ 18.600, Roadmap R$ 20.400, responsável Ana Souza. Segue o material da reunião.

> Faça o snapshot patrimonial da família Andrade no Private, a partir desta planilha.

> Preciso de uma apresentação da devolutiva do estudo da família Costa, identidade
> Private, com o conteúdo deste Word.

O Claude Code lê as regras do kit sozinho (`CLAUDE.md`), copia o modelo certo para
`documentos/<cliente>/`, preenche, confere e gera o PDF ao lado do HTML.

Para exportar de novo depois de uma correção feita à mão:

```bash
node ferramentas/pdf.mjs documentos/<cliente>/<documento>.html
```

## As duas identidades

- **Private:** família atendida pelo AUVP Private Banking.
- **Verde:** cliente da consultoria AUVP Capital, ou cliente de fora da casa.

## O que tem aqui

- `MARCA.md`: o guia de marca (cores, tipografia, componentes, texto).
- `modelos/`: os modelos nas duas identidades. Não edite; o Claude Code copia.
- `referencia/`: o PDF de cada modelo, para ver como fica.
- `marca/`: logos, grafismos e fontes, para uso fora dos documentos.
- `documentos/`: os documentos dos clientes.

Quando a AUVP mandar uma versão nova do kit, substitua tudo **menos** a pasta
`documentos/`.

## Dúvidas e pedidos

Se um documento precisar de algo que os modelos e os componentes não têm (um tipo de
página novo, um gráfico diferente), fale com o time de Produtos da AUVP antes de
improvisar. O modelo novo entra na versão seguinte do kit para todos.
