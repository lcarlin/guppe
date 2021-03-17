"""
Modulo collections : Counter
Collections -> High-Performance container datatypes
Counter -> recebe um interável como parametro e cria um objecto do tipo collectionsCounter, analogo à um dicionário
contendo como chave o elemento da lista passado como parametro e como valor a qyantidade de ocorrencias desse elemento

====================================================================================================================
# Utilizando o Couner
# primento tem que importar a parada
from collections import Counter
# é uma listra, mas poderia ser uma tupla, dicionario e essas coisas , qualquer interável
lista = [1, 1, 1, 2, 2, 3, 3, 3, 3, 1, 1, 2, 2, 4, 4, 4, 4, 5, 5, 5, 5, 5, 2, 3, 45, 45, 66, 43, 34, 66, 88]
res = Counter(lista)
# fica parecido com um dicionário, porem a chave é o item e o valoe é a qtd de ocorrencias do item
print (type(res))
print(res)
# Counter({1: 5, 2: 5, 3: 5, 5: 5, 4: 4, 45: 2, 66: 2, 43: 1, 34: 1, 88: 1})
====================================================================================================================
# primento tem que importar a parada
from collections import Counter
print (Counter('Geek University'))
====================================================================================================================

"""
# Utilizando o Couner
# primento tem que importar a parada
# https://docs.python.org/3/library/collections.html#collections.Counter
from collections import Counter
textoGrande = """Sua obra consiste em onze livros autobiográficos nos quais relata experiências decorrentes de sua associação com o bruxo conhecido por Don Juan Matus, índio da tribo Yaquis, do deserto de Sonora, no México. Como relata em entrevista para Sam Keen, pensando em ir para o curso de antropologia, buscava a publicação de um artigo científico para dar início à carreira acadêmica. Castaneda havia lido o livro de Aldous Huxley As Portas da Percepção, que havia celebrizado, no mundo ocidental, os efeitos psicotrópicos da mescalina, alcaloide alucinógeno presente em grandes quantidades no botão do cacto de peiote, que era usado de forma ritual por vários povos indígenas americanos. Castaneda havia escrito um pequeno ensaio sobre o livro. Castaneda, então, pesquisou o tema das plantas medicinais em livros como o de Weston La Barre, O ritual do peiote, e partiu para o trabalho de campo no sudoeste da Califórnia.
Foi então para o estado de Arizona, onde conheceu o índio bruxo conhecido como Don Juan Del Peiote. Este viria a ser seu guia, e é personagem central nos livros autobiográficos que escreveu. O encontro com o índio foi um episódio marcante, que é recontado várias vezes na sua obra. Numa estação rodoviária, indicado por um colega da faculdade, Castaneda aproximou-se e apresentou-se como especialista em peiote, convidando o índio a lhe conceder uma entrevista. Como não sabia virtualmente nada a respeito do cacto, segundo relata, Don Juan teria captado sua mentira e devolvido-a com um olhar. Este olhar foi bastante significativo, pois Castaneda, normalmente um homem falante e extrovertido, ficou sem ação e tímido ao ser perscrutado. Nas explanações posteriores, diz que Don Juan o havia capturado com o olhar mostrando-lhe o nagualismo, pois havia percebido que Castaneda poderia ser o homem que ele procurava para lhe passar seu conhecimento. Depois de mais alguns encontros, Don Juan lhe anuncia sua decisão e decide levá-lo a experimentar as plantas medicinais que Castaneda tanto pedia.
Aos poucos, o jovem latino e acadêmico foi sendo posto ao encontro de experiências cognitivas que desafiavam o poder de explicação de sua razão, sendo forçado finalmente a mudar toda a sua concepção de mundo em prol das novas explicações que o mestre lhe fornecia e que ia compreendendo, gradualmente. A Erva do Diabo, seu primeiro livro, também tese de mestrado, tornou-se um best-seller entre os jovens do movimento hippie e da contracultura, que, rapidamente, elegeram Castaneda um guru da nova era, formando legiões de admiradores que queriam, por conta própria, reviver as experiências descritas no livro. O livro também era bastante prezado no meio acadêmico, sobretudo porque, em seu princípio, era considerada uma obra de cunho científico. Foi muito criticada por, supostamente, atrair os jovens para o mundo das drogas e do crime.
Uma controvérsia formou-se em torno de sua figura tanto por parte de admiradores, que queriam encontrar Don Juan pessoalmente e, de alguma forma, fazer parte do processo de aprendizado, quanto de céticos, que queriam encontrar motivos para desacreditá-lo academicamente, argumentando que o testemunho fornecido em seus escritos era ficcional e apontando a escassez de fontes documentais sobre sua pesquisa de campo [junto ao] com o mestre indígena. Castaneda foi procurado pela polícia brasileira durante a ditadura militar brasileira e seus livros foram banidos de entrar no Brasil pelo Governo Federal, por se acreditar que o livro incentivava os jovens do movimento hippie ao uso de drogas (no caso, o cacto peiote descrito no livro "A Erva do Diabo").
Em 1973, no auge de sua fama, a conhecida revista norte-americana Time publicou uma extensa matéria de capa sobre o autor. Esta só foi conseguida depois de muita insistência [junto aos] com os agentes literários do autor, que, inclusive, imploraram para Castaneda posar para fotos em ângulos parciais, o que sempre evitava a todo custo. A abrangente matéria notabilizou-se por publicar o resultado de uma suposta investigação envolvendo a biografia de Castaneda antes da fama, a qual tinha, entre seus objetivos implícitos e explícitos, o propósito de retratá-lo como um mentiroso. A reportagem alega que Castaneda era peruano, nascido na andina cidade de Cajamarca. A reportagem cita amigos da terra natal e mesmo uma irmã de Castaneda, falando sobre traços da personalidade de Castaneda, como sendo alguém dono de imaginação fértil e entregue ao vício do jogo e das drogas. Segundo ela, Castaneda seria filho de um relojoeiro e teria nascido no ano de 1925. Aos 24 anos, em 1951, teria decidido imigrar para os Estados Unidos após a traumática morte da mãe, assassinada por seu pai, o que teria sido testemunhado por Castaneda em seus seis anos de vida. No livro de entrevistas "Conversando com Carlos Castaneda", da jornalista Carmina Fort, Castaneda, décadas depois, lamenta a decisão da TIME de publicar estes dados, que teriam sido inseridos porque ela "precisava de uma história". O autor ironiza o esforço da matéria em situar sua ascendência [junto a] de índios sul-americanos.
Em 1973, revê os conceitos apresentados na primeira obra em uma versão de sua tese de doutorado em filosofia intitulada Journey to Ixtlan - Lessons of Don Juan (Viagem a Ixtlan). Como explica no sexto livro, O Presente da Águia, o sistema de interpretações e crenças que se dispôs a estudar terminou por engalfinhá-lo, ao se revelar tão ou mais complexo que o sistema "ocidental" de interpretações do mundo.
Um 13° livro chamado Magical Passes (Passes Mágicos) foi lançado, destoando aparentemente do conjunto da obra, pois parece se aproximar mais de um manual prático de aplicação de exercícios corporais de educação física, embora não o seja. """

palavras = textoGrande.split()
# print(palavras)
resultado = Counter(palavras)
print(resultado)
# apresente as 5 palavras que mais se repetem
print(resultado.most_common(5))
