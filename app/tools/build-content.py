from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]
def ing(name,g):return {'name':name,'amount':g,'unit':'g'}
def items(*rows):return [ing(n,g) for n,g in rows]
BASE=items(('Farinha de trigo',450),('Leite integral',180),('Ovo sem casca',100),('Água',20),('Manteiga sem sal',60),('Açúcar',80),('Fermento biológico seco',9),('Sal',4),('Essência de panetone',5))
DOUGH_STEPS=[
('Organize a bancada','Pese os ingredientes. Separe 12 formas de papel próprias para mini panetone de 100 g e uma assadeira. O ovo é pesado sem a casca; bata com um garfo antes de pesar.'),
('Comece a massa','Misture a farinha com o fermento. Acrescente açúcar, leite levemente morno, ovo, essência e água. Misture até não sobrar farinha seca. O líquido deve estar apenas morno, nunca quente.'),
('Desenvolva a massa','Adicione sal e sove até formar uma massa unida. Incorpore a manteiga em três adições e continue sovando até a massa ganhar elasticidade. Isso pode levar de 15 a 25 minutos, com pequenas pausas. Evite acrescentar farinha para corrigir a pegajosidade; a absorção varia conforme a marca.'),
('Primeira fermentação','Cubra a tigela e deixe em local protegido até aumentar bastante de volume, próximo do dobro. Comece observando após 60 minutos; o crescimento pode levar mais tempo em dias frios. O volume é mais importante que o relógio.'),
('Junte o sabor da massa','Incorpore os ingredientes do grupo Sabor da massa, quando houver, em movimentos suaves. Não use recheio cremoso na massa crua. Seque bem as frutas já cortadas e use as gotas de chocolate frias.'),
('Pese e modele','Divida toda a massa em 12 porções iguais, pesando cada uma. Conforme os ingredientes adicionados, espere cerca de 75 a 90 g de massa crua por unidade. Boleie e coloque nas formas; não comprima a massa nem encha até a borda.'),
('Segunda fermentação','Cubra sem apertar e deixe crescer até a massa se aproximar da borda da forma, ainda com espaço para o forno. Observe após 45 minutos; pode levar 90 minutos ou mais. Preaqueça o forno a 170 °C durante os últimos 20 minutos.'),
('Asse e esfrie','Asse na grade central por aproximadamente 20 a 30 minutos. Ajuste ao seu forno: a superfície deve dourar e o centro não pode apresentar massa crua. Se dourar cedo, proteja a superfície com papel alumínio sem apertar. Deixe esfriar completamente sobre uma grade antes de rechear ou embalar.')]
FILLINGS={
 'brigadeiro':{'label':'Brigadeiro cremoso','ingredients':items(('Leite condensado',300),('Creme de leite',150),('Chocolate em pó 50% cacau',25),('Manteiga sem sal',8)),'method':'Misture os ingredientes em uma panela de fundo grosso. Cozinhe em fogo baixo, mexendo sem parar, até engrossar e cair da espátula em porções cremosas, antes do ponto de enrolar. Transfira para um recipiente limpo, cubra em contato com filme próprio para alimentos e resfrie. Use o creme frio.'},
 'leite':{'label':'Creme de leite em pó','ingredients':items(('Leite condensado',300),('Creme de leite',150),('Leite em pó integral',40),('Manteiga sem sal',8)),'method':'Dissolva o leite em pó no creme de leite e misture ao leite condensado e à manteiga. Cozinhe em fogo baixo, mexendo até ficar cremoso e encorpado. Transfira para um recipiente limpo, cubra em contato e resfrie antes de usar.'},
 'ganache':{'label':'Ganache de chocolate','ingredients':items(('Chocolate meio amargo',300),('Creme de leite',150)),'method':'Pique o chocolate em pedaços pequenos. Aqueça o creme de leite até ficar bem quente, sem fervura prolongada. Despeje sobre o chocolate, espere um minuto e misture do centro para as bordas até emulsionar. Se necessário, aqueça por poucos segundos. Resfrie até ficar cremoso e estável para aplicar.'},
 'branca':{'label':'Ganache branca','ingredients':items(('Chocolate branco',300),('Creme de leite',100)),'method':'Derreta o chocolate branco em pulsos curtos, misturando entre eles. Junte o creme de leite levemente aquecido e mexa até ficar homogêneo. Deixe resfriar até encorpar. A textura depende da marca do chocolate; não use a mistura quente para rechear.'},
 'doce':{'label':'Doce de leite cremoso','ingredients':items(('Doce de leite pastoso industrializado',400),('Creme de leite',80)),'method':'Misture o doce de leite pastoso ao creme de leite até obter um creme uniforme. Mantenha refrigerado enquanto prepara os minis. Use doce de leite pronto, de boa procedência; não cozinhe latas fechadas nesta preparação.'},
 'coco':{'label':'Creme de coco','ingredients':items(('Leite condensado',300),('Creme de leite',150),('Coco ralado seco sem açúcar',45),('Manteiga sem sal',8)),'method':'Misture todos os ingredientes na panela. Cozinhe em fogo baixo, mexendo, até obter um creme de colher mais firme. Transfira para um recipiente limpo, cubra em contato e resfrie antes de rechear.'}
}
# Cada linha representa uma combinação culinária própria, não um resultado de teste de cozinha.
CATALOG=[
('Clássicos','Frutas cristalizadas e passas',[('Frutas cristalizadas',80),('Uvas passas',40)],None,[]),
('Clássicos','Laranja e passas',[('Laranja cristalizada picada',60),('Uvas passas',60)],None,[]),
('Clássicos','Damasco e nozes',[('Damasco seco picado',80),('Nozes picadas',40)],None,[]),
('Clássicos','Cranberry e laranja',[('Cranberry seca',80),('Laranja cristalizada picada',40)],None,[]),
('Clássicos','Figo e castanha',[('Figo seco picado',80),('Castanha de caju picada',40)],None,[]),
('Clássicos','Maçã seca e canela',[('Maçã desidratada picada',80),('Uvas passas',40),('Canela em pó',2)],None,[]),
('Clássicos','Banana seca e chocolate',[('Banana passa picada',60),('Gotas de chocolate',60)],None,[]),
('Clássicos','Coco e frutas',[('Frutas cristalizadas',80),('Coco ralado seco sem açúcar',40)],None,[]),
('Clássicos','Mix de castanhas',[('Nozes picadas',40),('Castanha de caju picada',40),('Amêndoas picadas',40)],None,[]),
('Clássicos','Passas e especiarias',[('Uvas passas',120),('Canela em pó',2),('Noz moscada em pó',0.5)],None,[]),
('Chocotones','Gotas ao leite',[('Gotas de chocolate ao leite',120)],None,[]),
('Chocotones','Gotas meio amargas',[('Gotas de chocolate meio amargo',120)],None,[]),
('Chocotones','Chocolate branco',[('Gotas de chocolate branco',120)],None,[]),
('Chocotones','Dois chocolates',[('Gotas de chocolate ao leite',60),('Gotas de chocolate branco',60)],None,[]),
('Chocotones','Três chocolates',[('Gotas de chocolate ao leite',40),('Gotas de chocolate branco',40),('Gotas de chocolate meio amargo',40)],None,[]),
('Chocotones','Chocolate e nozes',[('Gotas de chocolate',80),('Nozes picadas',40)],None,[]),
('Chocotones','Chocolate e café',[('Gotas de chocolate',120),('Café solúvel',3)],None,[]),
('Chocotones','Chocolate branco e cranberry',[('Gotas de chocolate branco',70),('Cranberry seca',50)],None,[]),
('Chocotones','Chocolate e laranja',[('Gotas de chocolate',80),('Laranja cristalizada picada',40)],None,[]),
('Chocotones','Chocolate e amendoim',[('Gotas de chocolate',80),('Amendoim torrado sem sal',40)],None,[]),
('Brigadeiros','Brigadeiro clássico',[], 'brigadeiro',[]),
('Brigadeiros','Brigadeiro com paçoca',[], 'brigadeiro',[('Paçoca esfarelada',45)]),
('Brigadeiros','Brigadeiro de café',[], 'brigadeiro',[('Café solúvel',3)]),
('Brigadeiros','Brigadeiro de canela',[], 'brigadeiro',[('Canela em pó',2)]),
('Brigadeiros','Brigadeiro com nozes',[], 'brigadeiro',[('Nozes picadas',40)]),
('Brigadeiros','Brigadeiro com coco',[], 'brigadeiro',[('Coco ralado seco sem açúcar',35)]),
('Brigadeiros','Brigadeiro com avelã',[], 'brigadeiro',[('Creme de avelã pronto',60)]),
('Brigadeiros','Brigadeiro crocante',[], 'brigadeiro',[('Biscoito de chocolate triturado',45)]),
('Brigadeiros','Brigadeiro de laranja',[], 'brigadeiro',[('Laranja cristalizada picada',35)]),
('Brigadeiros','Brigadeiro com castanha',[], 'brigadeiro',[('Castanha de caju picada',40)]),
('Leite em pó','Leite em pó clássico',[], 'leite',[]),
('Leite em pó','Leite em pó com avelã',[], 'leite',[('Creme de avelã pronto',70)]),
('Leite em pó','Leite em pó e morango',[], 'leite',[('Geleia de morango pronta',80)]),
('Leite em pó','Leite em pó e coco',[], 'leite',[('Coco ralado seco sem açúcar',30)]),
('Leite em pó','Leite em pó e biscoito',[], 'leite',[('Biscoito de chocolate triturado',45)]),
('Leite em pó','Leite em pó e doce de leite',[], 'leite',[('Doce de leite pastoso industrializado',80)]),
('Leite em pó','Leite em pó e damasco',[], 'leite',[('Damasco seco picado',40)]),
('Leite em pó','Leite em pó e amêndoas',[], 'leite',[('Amêndoas picadas',35)]),
('Leite em pó','Leite em pó e paçoca',[], 'leite',[('Paçoca esfarelada',40)]),
('Leite em pó','Leite em pó e frutas vermelhas',[], 'leite',[('Geleia de frutas vermelhas pronta',80)]),
('Trufados','Trufa de chocolate',[], 'ganache',[]),
('Trufados','Trufa branca',[], 'branca',[]),
('Trufados','Trufa de café',[], 'ganache',[('Café solúvel',3)]),
('Trufados','Trufa de coco',[], 'branca',[('Coco ralado seco sem açúcar',30)]),
('Trufados','Trufa de amêndoas',[], 'ganache',[('Amêndoas picadas',35)]),
('Trufados','Trufa de pistache',[], 'branca',[('Pasta de pistache pura',40)]),
('Trufados','Trufa de limão',[], 'branca',[('Raspas de limão higienizado',3)]),
('Trufados','Trufa de laranja',[], 'ganache',[('Laranja cristalizada picada',40)]),
('Trufados','Trufa de avelãs',[], 'ganache',[('Avelãs torradas picadas',40)]),
('Trufados','Trufa de maracujá',[], 'branca',[('Geleia de maracujá pronta',70)]),
('Doce de leite','Doce de leite clássico',[], 'doce',[]),
('Doce de leite','Doce de leite e nozes',[], 'doce',[('Nozes picadas',40)]),
('Doce de leite','Doce de leite e coco',[], 'doce',[('Coco ralado seco sem açúcar',30)]),
('Doce de leite','Doce de leite e paçoca',[], 'doce',[('Paçoca esfarelada',40)]),
('Doce de leite','Doce de leite e chocolate',[], 'doce',[('Chocolate meio amargo picado',45)]),
('Doce de leite','Doce de leite e canela',[], 'doce',[('Canela em pó',2)]),
('Doce de leite','Doce de leite e amêndoas',[], 'doce',[('Amêndoas picadas',35)]),
('Doce de leite','Doce de leite e damasco',[], 'doce',[('Damasco seco picado',45)]),
('Doce de leite','Doce de leite e café',[], 'doce',[('Café solúvel',3)]),
('Doce de leite','Doce de leite e castanha',[], 'doce',[('Castanha de caju picada',40)]),
('Coco e frutas','Coco cremoso',[], 'coco',[]),
('Coco e frutas','Coco com chocolate',[], 'coco',[('Chocolate meio amargo picado',40)]),
('Coco e frutas','Coco com damasco',[], 'coco',[('Damasco seco picado',40)]),
('Coco e frutas','Coco com doce de leite',[], 'coco',[('Doce de leite pastoso industrializado',70)]),
('Coco e frutas','Coco com amêndoas',[], 'coco',[('Amêndoas picadas',35)]),
('Coco e frutas','Coco com morango',[], 'coco',[('Geleia de morango pronta',80)]),
('Coco e frutas','Coco com frutas vermelhas',[], 'coco',[('Geleia de frutas vermelhas pronta',80)]),
('Coco e frutas','Coco com maracujá',[], 'coco',[('Geleia de maracujá pronta',70)]),
('Coco e frutas','Coco com laranja',[], 'coco',[('Laranja cristalizada picada',35)]),
('Coco e frutas','Coco com cranberry',[], 'coco',[('Cranberry seca picada',40)]),
('Especiais','Pistache e chocolate branco',[('Gotas de chocolate branco',80),('Pistache sem sal picado',40)],'branca',[('Pasta de pistache pura',35)]),
('Especiais','Avelã com chocolate crocante',[('Gotas de chocolate',80)],'ganache',[('Creme de avelã pronto',50),('Avelãs torradas picadas',35)]),
('Especiais','Chocolate branco e nozes',[('Gotas de chocolate branco',80)],'branca',[('Nozes picadas',35)]),
('Especiais','Café com leite em pó',[('Gotas de chocolate',80),('Café solúvel',2)],'leite',[('Café solúvel',2)]),
('Especiais','Dois cremes de chocolate',[('Gotas de chocolate',80)],'branca',[('Chocolate meio amargo picado',50)]),
('Especiais','Caramelo com amendoim',[('Gotas de chocolate',80)],'doce',[('Amendoim torrado sem sal',40)]),
('Especiais','Damasco com trufa branca',[('Damasco seco picado',70)],'branca',[('Damasco seco picado',35)]),
('Especiais','Chocolate e especiarias',[('Gotas de chocolate meio amargo',80),('Canela em pó',1)],'ganache',[('Canela em pó',1),('Noz moscada em pó',0.3)]),
('Especiais','Frutas natalinas com trufa',[('Frutas cristalizadas',60),('Uvas passas',40)],'branca',[('Laranja cristalizada picada',30)]),
('Especiais','Castanhas com doce de leite',[('Nozes picadas',30),('Castanha de caju picada',30)],'doce',[('Amêndoas picadas',30)])]
assert len(CATALOG)==80
recipes=[]
for idx,(cat,name,mix,fill,extras) in enumerate(CATALOG,1):
 groups=[{'title':'Massa base','items':BASE}]
 if not mix and fill:mix=[('Gotas de chocolate',80)]
 if mix:groups.append({'title':'Sabor da massa','items':items(*mix)})
 steps=[{'title':t,'text':v} for t,v in DOUGH_STEPS]
 video='D_3fJWA00C0'
 if fill:
  f=FILLINGS[fill];groups.append({'title':f['label'],'items':f['ingredients']})
  if extras:groups.append({'title':'Complemento do recheio','items':items(*extras)})
  steps.append({'title':'Prepare o recheio','text':f['method']})
  if extras:
   names=', '.join(n.lower() for n,g in extras)
   text='Com o recheio frio, incorpore '+names+'.'
   if any('Geleia' in n or 'Creme de avelã' in n or 'Doce de leite' in n for n,g in extras):text='Separe o complemento indicado e distribua em uma camada dentro de cada mini, junto do creme frio. Assim você preserva as duas texturas.'
   if any('Café solúvel' in n for n,g in extras):text='Dissolva o café solúvel do recheio no próprio creme de leite da fórmula antes de preparar o creme. Não adicione água extra.'
   steps.append({'title':'Acrescente o complemento','text':text})
  steps.extend([{'title':'Recheie os minis','text':'Com os pães totalmente frios, corte uma tampa pequena e retire parte do miolo sem furar o fundo. Aplique cerca de 25 g de recheio por unidade e recoloque a tampa. Reserve creme para finalizar; se o rendimento variar, distribua por peso entre as 12 unidades.'},{'title':'Finalize','text':'Espalhe cerca de 10 g do mesmo creme sobre cada mini. Se preferir manter a cobertura firme, mantenha os minis refrigerados até o momento de servir. Guarde eventual sobra de creme separadamente e identificada.'}])
  video='aIgkUqJtUJs' if fill in ['leite','coco'] else '50sZqnRJ3qI' if fill in ['ganache','branca'] else 'aIgkUqJtUJs'
 if any('Café solúvel' in n for n,g in mix):steps[1]['text']+=' Dissolva o café da massa no leite antes de misturar.'
 names=' '.join(i['name'].lower() for g in groups for i in g['items'])
 allergens=['Trigo e glúten','Ovos','Leite']
 for token,label in [('amendoim','Amendoim'),('nozes','Nozes'),('amêndoas','Amêndoas'),('castanha','Castanhas'),('pistache','Pistache'),('avelã','Avelãs')]:
  if token in names:allergens.append(label)
 recipes.append({'id':f'r{idx:03}','name':name,'category':cat,'yield':12,'kind':'panetone','minutes':240 if fill else 210,'time':'4 a 5 h' if fill else '3 a 4 h','difficulty':'Intermediário','image':'../assets/mini-sabores.jpg' if cat=='Clássicos' else '../assets/mini-mao.jpg' if cat in ['Chocotones','Brigadeiros'] else '../assets/bonus-decoracoes.jpg' if cat in ['Leite em pó','Coco e frutas'] else '../assets/mini-presentes.jpg','description':('Massa aromática com '+', '.join(n.lower() for n,g in mix)+'.') if not fill else FILLINGS[fill]['label']+' em um mini feito em forma de 100 g'+(' com '+', '.join(n.lower() for n,g in extras) if extras else '')+'.','groups':groups,'steps':steps,'allergens':allergens,'video':video,'filled':bool(fill),'notes':['Rendimento estimado de 12 unidades. A forma de 100 g indica o tamanho do molde, não o peso final com recheio.','Esta é uma formulação adaptada. Faça um primeiro preparo para ajustar sua farinha, seu forno e o rendimento. Não houve teste prático de cozinha nesta produção.','Para assar, considere ponto e estrutura; tempos e fermentação são estimativas.','Recheios com laticínios exigem refrigeração. Mantenha a 4 °C ou menos, embale com o alimento frio e não atribua uma validade comercial sem validação. Consulte Cuidados e conservação.'],'sources':['tecnica-massa','higiene']})
# Biscoitos: uma massa amanteigada de domínio culinário comum com variações próprias.
cookie_variants=[('Amanteigado de baunilha',[]),('Estrelinhas de canela',[('Canela em pó',3)]),('Gengibre de Natal',[('Gengibre em pó',3),('Canela em pó',2)]),('Chocolate e baunilha',[('Cacau em pó',20)]),('Raspas de laranja',[('Raspas de laranja higienizada',4)]),('Limão e baunilha',[('Raspas de limão higienizado',3)]),('Coco amanteigado',[('Coco ralado seco sem açúcar',30)]),('Amêndoas natalinas',[('Amêndoas picadas finamente',30)]),('Castanha de caju',[('Castanha de caju picada',30)]),('Gotas de chocolate',[('Gotas de chocolate',50)]),('Biscoito com goiabada',[('Goiabada firme em cubos',60)]),('Nozes e canela',[('Nozes picadas',30),('Canela em pó',2)])]
cookies=[]
for idx,(name,extra) in enumerate(cookie_variants,1):
 flour=230 if any(n=='Cacau em pó' for n,g in extra) else 250
 groups=[{'title':'Massa do biscoito','items':items(('Farinha de trigo',flour),('Manteiga sem sal',125),('Açúcar',85),('Ovo sem casca',50),('Extrato de baunilha',3),('Sal',1))}]
 if extra:groups.append({'title':'Sabor e acabamento','items':items(*extra)})
 steps=[{'title':'Misture','text':'Misture a manteiga em ponto de pomada com o açúcar, sem incorporar muito ar. Junte ovo e baunilha e misture até ficar uniforme.'},{'title':'Forme a massa','text':'Acrescente farinha e sal. Junte os ingredientes de sabor, exceto goiabada, quando houver. Misture apenas até unir. Não sove. No biscoito de chocolate, o cacau substitui parte da farinha já descontada na lista.'},{'title':'Resfrie','text':'Achate a massa entre duas folhas de papel manteiga e leve à geladeira por 30 minutos ou até ficar firme para cortar.'},{'title':'Corte','text':'Abra com aproximadamente 5 mm de espessura. Corte cerca de 30 biscoitos pequenos e distribua em assadeira com papel manteiga próprio para forno. Se usar goiabada, pressione um cubinho no centro de cada peça.'},{'title':'Asse','text':'Asse em forno preaquecido a 170 °C por cerca de 12 a 18 minutos, até as bordas firmarem e começarem a dourar. Espere esfriar na assadeira antes de transferir para uma grade.'},{'title':'Decore','text':'Somente depois de frios, use glacê pronto para alimentos ou chocolate conforme a embalagem do fabricante. Espere a decoração firmar antes de embalar. O glacê é opcional e não está incluído no peso da massa.'}]
 cookies.append({'id':f'b{idx:02}','name':name,'category':'Biscoitos de Natal','kind':'biscoito','yield':30,'minutes':75,'time':'1 h 15 min','difficulty':'Fácil','image':'../assets/bonus-biscoitos.jpg','description':'Biscoitos pequenos para o café e para lembrancinhas.','groups':groups,'steps':steps,'allergens':['Trigo e glúten','Ovos','Leite']+(['Oleaginosas ou amendoim: conferir ingredientes'] if any(w in name.lower() for w in ['amêndoa','castanha','nozes']) else []),'video':'_z09sAwbxjs','filled':False,'notes':['Rendimento estimado para 30 peças pequenas; varia com o cortador e a espessura.','Variações próprias, sem teste de cozinha nesta produção. Ajuste ao seu forno e faça um primeiro lote antes de presentear ou vender.','Conserve completamente frios em recipiente limpo e bem fechado. A validade depende da umidade e da decoração; não há prazo comercial validado.'],'sources':['tecnica-biscoitos']})
cup_defs=[('Brigadeiro no copinho','brigadeiro',[]),('Leite em pó no copinho','leite',[]),('Doce de leite com biscoito','doce',[('Biscoito maisena triturado',60)]),('Coco com chocolate','coco',[('Chocolate meio amargo picado',60)]),('Leite em pó com morango','leite',[('Morango fresco higienizado e seco',120)]),('Brigadeiro com paçoca','brigadeiro',[('Paçoca esfarelada',50)]),('Ganache com biscoito','ganache',[('Biscoito de chocolate triturado',60)]),('Doce de leite e nozes','doce',[('Nozes picadas',40)]),('Creme branco com frutas vermelhas','branca',[('Geleia de frutas vermelhas pronta',80)]),('Coco com maracujá','coco',[('Geleia de maracujá pronta',80)])]
cups=[]
for idx,(name,key,extras) in enumerate(cup_defs,1):
 f=FILLINGS[key];groups=[{'title':f['label'],'items':f['ingredients']}]
 if extras:groups.append({'title':'Camadas e finalização','items':items(*extras)})
 cups.append({'id':f'c{idx:02}','name':name,'category':'Sobremesas no copinho','kind':'copinho','yield':10,'minutes':150,'time':'30 min + 2 h de geladeira','difficulty':'Fácil','image':'../assets/bonus-copinhos.jpg','description':'Porções individuais em copinhos de 50 ml, sem encher até a borda.','groups':groups,'steps':[{'title':'Prepare o creme','text':f['method']},{'title':'Organize os complementos','text':'Separe os ingredientes das camadas. Triture biscoitos quando usados. Morangos precisam estar higienizados, bem secos e cortados pouco antes da montagem.'},{'title':'Monte os copinhos','text':'Use 10 copinhos limpos de 50 ml próprios para alimentos e frios. Distribua o creme resfriado, intercalando os complementos quando houver. Deixe espaço para a tampa e divida as quantidades igualmente.'},{'title':'Refrigere','text':'Tampe e leve à geladeira por pelo menos 2 horas para firmar a textura. Mantenha a 4 °C ou menos até servir e transporte refrigerado.'}],'allergens':['Leite']+(['Trigo e glúten'] if any('Biscoito' in n for n,g in extras) else [])+(['Oleaginosas ou amendoim: conferir ingredientes'] if any(w in name.lower() for w in ['paçoca','nozes']) else []),'video':'5Lt7rdZWBsg','filled':True,'notes':['Rendimento aproximado. Divida o creme por peso e respeite o volume real de cada copinho.','Adaptação culinária sem teste de cozinha nesta produção. Não é a reprodução exata da receita do vídeo de apoio.','Com frutas frescas, prepare próximo de servir e mantenha refrigerado. Não há validade comercial validada.'],'sources':['tecnica-ganache','higiene']})
video_meta=json.loads((ROOT/'videos-verificados.json').read_text())
lesson_meta=[
('D_3fJWA00C0','Massa de mini panetone','Comece aqui','Veja mistura, porcionamento e fermentação em formas pequenas.','../assets/mini-sabores.jpg'),
('SxkZqvdoEcM','Outro preparo de mini panetones','Comece aqui','Compare a manipulação da massa e a montagem das forminhas.','../assets/mini-mao.jpg'),
('fUCn0tej3ZE','Entenda a massa de panetone','Massas','Acompanhe o desenvolvimento da massa e a fermentação.','../assets/mini-sabores.jpg'),
('aIgkUqJtUJs','Recheios de leite em pó e coco','Recheios','Aprenda a abrir, rechear e finalizar o panetone.','../assets/bonus-decoracoes.jpg'),
('50sZqnRJ3qI','Ganache e trufa de chocolate','Recheios','Observe a emulsão e a textura de uma ganache.','../assets/mini-mao.jpg'),
('l4sc0SrZZS8','Ganache para recheio e cobertura','Decoração','Conheça uma técnica adicional de cobertura.','../assets/bonus-decoracoes.jpg'),
('_z09sAwbxjs','Biscoitos de Natal','Biscoitos','Massa, corte e apresentação de biscoitos para presentes.','../assets/bonus-biscoitos.jpg'),
('5Lt7rdZWBsg','Sobremesa no copinho de chocolate','Copinhos','Veja uma montagem de porção individual com chocolate.','../assets/bonus-copinhos.jpg'),
('Xp5kfFXK_E0','Porta mini panetone','Embalagens','Uma ideia artesanal para apresentar seus minis.','../assets/bonus-embalagens.jpg'),
('F8Vzgdi7L80','Caixa para panetone em cartonagem','Embalagens','Aprenda uma montagem de embalagem e adapte às medidas do seu mini.','../assets/bonus-embalagens.jpg'),
('l4zraPJbcPw','Como definir o preço de venda','Vendas','Entenda custos e margem com o Sebrae PR.','../assets/bonus-vendas.jpg')]
lessons=[]
for vid,title,cat,desc,img in lesson_meta:
 meta=next(v for v in video_meta if v['id']==vid)
 lessons.append({'id':vid,'title':title,'category':cat,'description':desc,'image':img,'originalTitle':meta['title'],'author':meta['author'],'url':'https://www.youtube.com/watch?v='+vid})
guides={
 'decoracoes':{'title':'Decorações para os minis','subtitle':'Seis acabamentos para dar sua cara a cada receita.','image':'../assets/bonus-decoracoes.jpg','videos':['l4sc0SrZZS8','aIgkUqJtUJs'],'sections':[
 {'title':'1. Ganache espalhada','text':'Prepare uma ganache de sua preferência e espere chegar à consistência cremosa. Coloque uma colher pequena sobre o mini frio e espalhe com espátula. Não deixe a cobertura escorrer para dentro da embalagem.','list':['Espátula pequena','Ganache já fria','Mini completamente frio']},
 {'title':'2. Fios de chocolate','text':'Use chocolate temperado ou cobertura fracionada conforme as instruções do fabricante. Faça um pequeno corte na ponta do saco de confeitar e movimente sobre o topo. Não acrescente água ao chocolate.'},
 {'title':'3. Roseta de creme','text':'Use creme firme, frio e próprio para bico. Coloque o saco na vertical, pressione e solte antes de levantar. Faça um teste em um prato. Coberturas com laticínios pedem conservação refrigerada.'},
 {'title':'4. Coco ou leite em pó','text':'Polvilhe uma camada fina sobre o creme já aplicado. Para uma cobertura uniforme, use peneira pequena para leite em pó. Confira se os confeitos e pós são próprios para consumo.'},
 {'title':'5. Um brigadeiro no topo','text':'Reserve brigadeiro preparado no ponto de enrolar, resfrie e modele bolinhas pequenas. Passe no granulado e acomode sobre a cobertura. Não use palitos escondidos dentro do alimento.'},
 {'title':'6. Castanhas e frutas secas','text':'Corte em pedaços pequenos e coloque sobre a cobertura ainda cremosa. Indique os ingredientes alergênicos a quem vai receber. Frutas secas e castanhas precisam estar próprias para consumo e sem sinais de umidade.'},
 {'title':'Antes de embalar','text':'Espere a cobertura estabilizar, use embalagem própria para alimentos e não deixe a decoração encostar na tampa. Registre data de preparo e ingredientes. Veja o guia de cuidados para conservação.'}]},
 'embalagens':{'title':'Embalagens e tags de Natal','subtitle':'Quatro montagens práticas e tags para imprimir.','image':'../assets/bonus-embalagens.jpg','videos':['Xp5kfFXK_E0','F8Vzgdi7L80'],'sections':[
 {'title':'Saquinho com laço','text':'Coloque o mini frio em saco transparente próprio para alimentos. Deixe folga para a cobertura. Feche com fita acima do topo e prenda uma tag por fora. A fita não deve encostar no alimento.','list':['Saco próprio para alimentos','Fita de cetim','Tag impressa','Tesoura']},
 {'title':'Caixinha individual','text':'Meça a largura e a altura do mini já decorado. Escolha uma caixa com folga e berço estável. Use barreira própria para contato com alimentos; papel decorativo e cola ficam na parte externa.'},
 {'title':'Kit com duas unidades','text':'Escolha uma base com espaço para dois minis sem se encostarem. Embale cada um individualmente e estabilize com berço ou divisória. Identifique os sabores para quem receber.'},
 {'title':'Cesta para presentear','text':'Combine minis embalados individualmente com um pacote de biscoitos e um cartão. Use base firme e não misture itens que exigem refrigeração com produtos que ficarão fora da geladeira por longo período.'},
 {'title':'Personalize as tags','text':'Use o gerador de tags da área de ferramentas. Informe o nome de quem vai receber e uma mensagem. Imprima em tamanho real, corte e fixe por fora. A tag decorativa não substitui as informações sobre ingredientes e conservação.'}]},
 'vendas':{'title':'Guia para vender seus minis','subtitle':'Preço, cardápio, atendimento e organização do primeiro pedido.','image':'../assets/bonus-vendas.jpg','videos':['l4zraPJbcPw'],'sections':[
 {'title':'1. Comece com um lote de teste','text':'Escolha dois ou três sabores. Prepare, pese o rendimento real, observe o trabalho e fotografe sua própria produção. Não use as imagens ilustrativas da coleção como se fossem fotos dos seus produtos.'},
 {'title':'2. Some os custos do lote','text':'Inclua ingredientes, embalagens, energia, perdas e o valor do seu tempo. Divida o total pelo número de unidades vendáveis. A calculadora desta área faz a conta usando os valores que você informar.'},
 {'title':'3. Diferencie margem de acréscimo','text':'Se o custo unitário é R$ 6 e a margem desejada é 40% do preço, o preço calculado é R$ 10, antes de taxas adicionais. Multiplicar o custo por 1,40 resulta em R$ 8,40 e não gera margem de 40%.'},
 {'title':'4. Monte um cardápio curto','text':'Mostre sabor, tamanho da forma, peso final real, ingredientes principais, valor e data limite para pedir. Diga se o produto precisa de refrigeração. Só anuncie o que você consegue produzir e entregar.'},
 {'title':'5. Abra as encomendas','text':'Publique uma foto própria e uma mensagem com os sabores e o período de entrega. Evite prometer validade sem testes. Confirme quantidade, sabor, preço total, pagamento e horário por escrito.'},
 {'title':'6. Registre os pedidos','text':'Use o controle de encomendas para anotar o combinado. Os dados ficam neste navegador; exporte uma cópia CSV. Como não há conta, outro aparelho não recebe esses dados automaticamente.'},
 {'title':'7. Separe pedidos e transporte','text':'Agrupe os pedidos por data e sabor. Identifique as embalagens e conserve cada produto na temperatura adequada. Confira o pedido com o cliente e informe como armazenar.'}],
 'messages':[
 {'title':'Abrir encomendas','text':'Oi! Preparei um cardápio de mini panetones e chocotones para este Natal. Tenho [sabores] e opções para presentear. As entregas serão em [datas]. Quer que eu envie as opções e os valores?'},
 {'title':'Enviar o cardápio','text':'Aqui estão as opções: [sabor e valor por unidade]. O kit com [quantidade] sai por [valor]. Pedidos até [data], com entrega ou retirada em [local e horário]. Qual opção você prefere?'},
 {'title':'Confirmar um pedido','text':'Confirmando seu pedido: [quantidade] mini panetones de [sabores]. Total: [valor]. Entrega ou retirada: [data, horário e local]. Pagamento: [forma e condição]. Está tudo certo?'},
 {'title':'Lembrar o prazo','text':'Oi! Passando para avisar que vou encerrar as encomendas deste lote em [data]. Se quiser reservar seus minis, me diga o sabor e a quantidade para eu verificar a disponibilidade.'},
 {'title':'Depois da entrega','text':'Oi! Espero que você tenha gostado dos minis. Obrigada por escolher meu trabalho. Se quiser contar como foi, vou adorar saber. As orientações de conservação estão junto do seu pedido.'}]},
 'cuidados':{'title':'Cuidados e conservação','subtitle':'Organize o preparo e trate cada recheio conforme seus ingredientes.','image':'../assets/mini-sabores.jpg','videos':[],'sections':[
 {'title':'Higiene antes do preparo','text':'Higienize mãos, bancada e utensílios. Use água potável e ingredientes dentro do prazo. Mantenha ovos crus separados de produtos prontos para consumo. Lave as mãos após manusear ovos.'},
 {'title':'Laticínios e frutas','text':'Minis recheados e sobremesas com creme de leite ou frutas exigem refrigeração. Mantenha a 4 °C ou menos e evite interromper a cadeia de frio. Não deixe os recheios resfriando por períodos longos na bancada.'},
 {'title':'Resfriamento e identificação','text':'Resfrie os cremes em recipientes limpos, rasos e protegidos, e leve à refrigeração. Identifique o produto e a data de preparo. A orientação geral da Anvisa limita o tempo na faixa de temperaturas que favorece multiplicação microbiana.'},
 {'title':'Validade não é um número universal','text':'A RDC 216 traz um limite geral de até 5 dias a 4 °C ou menos para alimento preparado em condições controladas. Isso não comprova a validade destas receitas. Recheio, higiene, embalagem e temperatura mudam o resultado; o prazo comercial precisa de validação específica.'},
 {'title':'Alergênicos','text':'As massas incluem trigo, ovos e leite. Algumas versões também incluem castanhas, amendoim ou avelãs. Chocolates e biscoitos podem conter soja e outros alergênicos. Leia todos os rótulos e informe os ingredientes a quem receber.'},
 {'title':'Sobre estas receitas e as aulas','text':'A coleção reúne formulações adaptadas e combinações de sabores. Elas não passaram por teste prático de cozinha nesta produção. Faça um primeiro preparo antes de produzir para terceiros. As aulas públicas são referências de técnica e podem usar fórmulas, tamanhos e rendimentos diferentes.'}]}
}
sources=[
{'id':'tecnica-massa','title':'Mini panetones • Jane Loures','url':'https://www.youtube.com/watch?v=D_3fJWA00C0','note':'Referência visual de técnica; a fórmula e as combinações da coleção são adaptações.'},
{'id':'tecnica-biscoitos','title':'Biscoito de Natal • Dika da Naka','url':'https://www.youtube.com/watch?v=_z09sAwbxjs','note':'Referência visual para preparo e corte; as variações da coleção têm formulação própria.'},
{'id':'tecnica-ganache','title':'Ganache: proporções e textura • Receitas Nestlé','url':'https://www.receitasnestle.com.br/receitas/ganache-coringa','note':'Referência geral de emulsão e consistência.'},
{'id':'higiene','title':'RDC 216: boas práticas • Anvisa','url':'https://anvisalegis.datalegis.net/action/ActionDatalegis.php?acao=abrirTextoAto&codTipo=&cod_menu=1696&cod_modulo=134&desItem=&desItemFim=&numeroAto=00000216&orgao=RDC%2FDC%2FANVISA%2FMS&pesquisa=true&seqAto=000&tipo=RDC&valorAno=2004','note':'Orientação geral de conservação, não estudo de validade dos produtos da coleção.'},
{'id':'precos','title':'Definição de preço de venda • Sebrae PR','url':'https://pr.agenciasebrae.com.br/videos/economia-e-politica/como-definir-preco-passo-a-passo-pra-precificar-seu-produto-ou-servico/','note':'Referência de custos, preço e margem.'}]
data={'version':1,'recipes':recipes,'cookies':cookies,'cups':cups,'lessons':lessons,'guides':guides,'sources':sources,'categories':list(dict.fromkeys(r['category'] for r in recipes))}
(ROOT/'content.json').write_text(json.dumps(data,ensure_ascii=False,indent=2))
(ROOT/'content.js').write_text('window.MINI_CONTENT = '+json.dumps(data,ensure_ascii=False,separators=(',',':'))+';\n')
print(f'{len(recipes)} receitas principais, {len(cookies)} biscoitos, {len(cups)} copinhos, {len(lessons)} aulas, {len(guides)} guias')
