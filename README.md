# Mini Panetones Faça e Venda

Página estática em HTML, CSS e JavaScript. Não precisa instalar dependências.

## Abrir localmente

Na pasta do projeto:

```sh
python3 -m http.server 8010 --bind ::
```

Abra http://127.0.0.1:8010.

## Conectar o pagamento

Preencha `checkoutLinks.basico` e `checkoutLinks.completo` em `script.js` com os links reais. Enquanto estiverem vazios, os botões abrem uma janela de prévia, sem cobrar nem coletar dados.

## Antes de vender

Esta é uma proposta de página, não um produto final cadastrado. Confirmar a existência das 80 receitas distintas, a composição dos bônus, o canal de atendimento, os termos de acesso e o processo de reembolso. Cadastrar os dados reais do responsável pela venda. Os preços sugeridos são R$ 12,90 e R$ 19,90.

As imagens ativas da página foram geradas com a ferramenta integrada imagegen. O mockup é um PNG com transparência; as três cenas mostram mini panetones com referência de escala. Os originais em PNG e versões JPEG otimizadas ficam em `assets/`. Os prompts estão em `assets/prompts-imagens.json`. As fotos antigas de pesquisa permanecem na pasta e suas origens estão em `assets/fontes.json`, mas não são usadas na página atual.

As imagens e o mockup são ilustrativos, identificados na página. O livro e o tablet representam uma coleção digital, não itens físicos entregues nem fotos do conteúdo já produzido.

A oferta está em desenvolvimento. A proposta atual especifica receitas em PDF para formas de 100 g, ingredientes em gramas, rendimento, massas, recheios e finalização. O pacote de R$ 19,90 propõe 5 bônus: biscoitos de Natal, sobremesas no copinho, decorações para minis, embalagens e tags, e guia de vendas. Essas especificações precisam fazer parte do material entregue antes da abertura das vendas. As 80 formulações e os conteúdos dos bônus agora estão implementados em `app/`, com PDFs. São adaptações culinárias e ainda não passaram por teste prático de cozinha.

A página não usa depoimentos, faturamento, contagem de compradores ou escassez inventados. A copy não contém hífens nem travessões. Os botões de checkout continuam em modo de prévia até os links reais serem configurados.

## Arquivos

* `index.html`: conteúdo e estrutura da página
* `styles.css`: visual e adaptação para celular
* `script.js`: seleção de plano e conexão de checkout
* `assets/`: imagens locais e registro das fontes

## Ângulos da oferta

A promessa principal atende a três motivações: fazer por hobby e saborear em casa, presentear amigos e família, e vender. Não tratar hobby como uma etapa obrigatória para começar a vender. O Pacote Básico atende aos três usos; o Completo adiciona receitas complementares, decorações, embalagens e um guia opcional para vendas. Manter essa abrangência na headline, galeria, público, chamadas e FAQ.

## Preços e bônus atuais

Básico: R$ 12,90. Completo: R$ 19,90. Diferença: R$ 7,00. Os dois incluem as 80 receitas principais. O Completo adiciona cinco bônus com imagens geradas próprias. Os conteúdos desses bônus são parte da proposta da oferta e precisam existir antes da venda. Os prompts das cinco imagens estão em `assets/prompts-bonus.json`.

## Área completa em /app/

Os dois planos liberam o mesmo endereço público, sem login, conforme solicitado. A área contém 80 versões de mini panetones, 12 biscoitos, 10 sobremesas, 11 aulas públicas do YouTube verificadas e todos os guias e ferramentas. Existem PDFs reais para download. Ver `app/README.md` para funcionamento e limites de validação culinária. As receitas são adaptações sem teste prático de cozinha, informadas assim no conteúdo. Os links de pagamento ainda precisam ser configurados; o endereço de entrega pode ser usado como redirecionamento após a compra.
