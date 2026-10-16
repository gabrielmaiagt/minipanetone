# Funil na Cakto

## Produto principal: 80 Receitas de Mini Panetones e Chocotones

| Oferta | Preço | Vai em |
|---|---|---|
| Pacote Básico | R$ 12,90 | `checkoutLinks.basico` |
| Pacote Completo (receitas + 5 bônus) | R$ 19,90 | `checkoutLinks.completo` |

## Order bumps

| Bump | Preço | Básico | Completo |
|---|---|---|---|
| Cesta de Natal com Mini Panetone: 7 montagens prontas, lista de itens, onde comprar e quanto cobrar | R$ 12,90 | sim | sim |
| Embalagem de R$ 1 que parece de loja: material barato de papelaria, passo a passo e onde comprar | R$ 7,90 | sim | não (o Completo já tem o bônus de embalagens) |

## Upsell (one-click, depois da compra)

Linha Gourmet: 12 sabores que vendem pelo dobro (Pistache, Ferrero, Kinder, Red Velvet, Ninho com Nutella). Mesma massa, mesmo trabalho, preço maior. R$ 27,00.

## Pendências

* Entregáveis dos bumps e do upsell ainda não existem.
* Bumps cadastrados na Cakto. Falta conferir a apresentação visual no checkout e concluir o upsell com página publicada e botão one-click.

## Configuração em 16/10/2026

Os três produtos adicionais foram criados como ativos na Cakto:

| Produto | Oferta | Checkout |
|---|---|---|
| Cesta de Natal | `9yoqh8p` | https://pay.cakto.com.br/9yoqh8p |
| Embalagem | `wsattxf` | https://pay.cakto.com.br/wsattxf |
| Linha Gourmet | `jbgtdgj` | https://pay.cakto.com.br/jbgtdgj |

IDs completos em `cakto-config.json`. Não contém credenciais.

A página `upsell/index.html` apresenta a Linha Gourmet por R$ 27,00. Seu botão atual abre uma nova compra no checkout. Ainda não é one-click.

Para ativar one-click, no painel Cakto: selecionar a oferta `jbgtdgj` no Gerador de Upsell, copiar o código completo gerado e inserir em `#cakto-one-click`. Configurar aceite e recusa para a URL pública de `/app/`. Depois remover o checkout alternativo e sua mensagem. No produto principal, habilitar a página personalizada de upsell e informar a URL pública de `/upsell/`. Testar os dois caminhos no fluxo real antes de considerar concluído.

Produtos principais criados como ativos e links conectados em `script.js`: Básico https://pay.cakto.com.br/sx8qygn e Completo https://pay.cakto.com.br/63bx672.

Bumps aplicados: `6wkH5G6` (Cesta no Básico), `3Ws7Pku` (Embalagem no Básico) e `4ZeuxLa` (Cesta no Completo).

Pendências atuais: configurar a entrega dos produtos, publicar a página e configurar o redirecionamento e o código one-click no painel. Os produtos adicionais ativos ainda não têm entrega de conteúdo configurada.

A página atual e a área pública liberam os cinco bônus também para o Básico. Isso se sobrepõe ao bump de embalagem e precisa ser considerado na oferta.
