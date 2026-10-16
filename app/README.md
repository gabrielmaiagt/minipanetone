# Minha Cozinha

Área completa e pública em `/app/`, sem login. O mesmo endereço serve aos dois planos.

## Conteúdo

* 80 versões de mini panetones e chocotones, com ingredientes, rendimento estimado, etapas, cuidados e fontes.
* 12 receitas de biscoitos e 10 sobremesas no copinho.
* 11 vídeos públicos conferidos pelo oEmbed oficial do YouTube, com autoria, incorporação e link de alternativa. São aulas de apoio por técnica, não 80 aulas exatas nem conteúdo exclusivo.
* Guias de decoração, embalagens, vendas e cuidados.
* PDFs para download e tags para imprimir.

As fórmulas são adaptações culinárias. Não houve teste prático de cozinha nesta produção. Isso está informado na coleção, nas fichas, nos PDFs e no guia de cuidados. Antes de vender o conteúdo como validado, é necessária revisão e execução culinária. Não há prazo comercial de validade validado para os alimentos.

## Recursos

Busca por nome ou ingrediente, categorias, favoritos, receitas preparadas, aulas assistidas, ajuste proporcional de ingredientes, checklist de preparo, modo de uma etapa por vez, temporizador, notas, lista de compras acumulada e CSV, tags personalizadas, cálculo de preço com margem e taxas, registro de pedidos e exportação de dados.

Todos os dados pessoais ficam em `localStorage` deste navegador. Não existe sincronização entre dispositivos. A área não tem proteção de acesso, conforme solicitado. O service worker guarda a interface, receitas e imagens para uso offline após o primeiro acesso. Os vídeos precisam de internet; PDFs ficam offline depois de acessados.

## Arquivos

* `index.html`, `app.css`, `app.js`: interface buildless.
* `content.json` e `content.js`: conteúdo completo.
* `videos-verificados.json`: metadados públicos dos vídeos consultados.
* `tools/build-content.py`: catálogo e composições culinárias.
* `tools/build-downloads.py`: documentos para exportação em PDF.
* `downloads/`: PDFs e versões HTML para impressão.
* `manifest.webmanifest` e `sw.js`: instalação e cache local.

## Atualizações

Execute os dois scripts Python para regenerar conteúdo e documentos. Depois exporte os documentos HTML em PDF com um navegador. Ao alterar recursos de cache, incremente o nome do cache em `sw.js`.

## Preview

A partir da raiz do projeto:

```sh
python3 -m http.server 8010 --bind ::
```

Abra `http://127.0.0.1:8010/app/`.
