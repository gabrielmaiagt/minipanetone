# Validação da área em /app/

Data: 16 de outubro de 2026.

## Conteúdo e arquivos

* 80 receitas principais com IDs únicos, ingredientes, rendimento estimado, etapas, alergênicos e notas.
* 12 biscoitos e 10 sobremesas no copinho.
* 11 vídeos públicos com URL e autoria conferidos no oEmbed oficial do YouTube. A incorporação está implementada; há link para assistir no canal caso o player seja indisponível. Não há garantia de disponibilidade futura dos vídeos externos.
* Sete PDFs reais respondendo HTTP 200 e com assinatura PDF válida.
* Ícones, manifest e service worker instaláveis.

## Testes funcionais aprovados

* Busca por ingrediente, categoria e preservação da busca ao favoritar.
* Escala de ingredientes ao alterar o rendimento.
* Soma de itens iguais na lista de compras.
* Persistência de anotações, checklists e receitas preparadas após recarregar.
* Modo preparo e controles do temporizador.
* Abertura e fechamento do player com crédito ao autor, e registro de aula assistida.
* Calculadora com verificação de uma margem conhecida e bloqueio de margem + taxas acima do limite.
* Impressão de 12 tags personalizadas em nova janela.
* Cadastro de encomenda, alteração do pagamento e exportação CSV.
* Catálogo e notas acessíveis após desligar a rede.
* Nenhuma exceção de JavaScript durante os fluxos testados.

## Responsividade

Nove telas avaliadas nas larguras 280, 320, 390, 540, 768, 1024 e 1440 px, totalizando 63 combinações. Sem rolagem lateral ou estouro de texto nos elementos avaliados.

## Limite culinário

As formulações foram escritas e estruturadas, mas não executadas em uma cozinha nesta produção. A área e os PDFs identificam as receitas como adaptações e orientam um primeiro preparo. Não há validação de rendimento, resultado sensorial ou validade comercial. Fontes técnicas e os créditos estão no guia Cuidados e conservação.

## Executar novamente

`node verificacao/app-e2e.cjs`

O teste usa o navegador Chrome deste ambiente e Playwright disponível no caminho de QA local. A aplicação em produção é estática e não depende desse ambiente de teste.
