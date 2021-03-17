"""
Filter
Filter () -> Serve para filtrar dados de uma determinada coleção

====================================================================================================================
valores = 1,2,3,4,5,6
media = (sum(valores) / len(valores))
print(media)
====================================================================================================================
# Biblioteca para se trabalhar com dados estatisticos
import statistics

# Dados coletados de um sensor
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# calculamndo a media dos dados utilizando a função mean()
media = statistics.mean(dados)
print(f'Media é de :-> {media}' )
# OBS: Assim como a funç~~ao MAP, a filter recebe 2 parametros: sendo o 1º uma função e o 2ª um iteravel

res = filter(lambda x: x > media, dados)
print (type(res))
print(list(res))
print(f'Novamente :-> {list(res)}')
# Assim como na funç~çao MAP, apos serem utilzados os dados de FILTEr, eles são excluidos da memoria
====================================================================================================================
# remover dados faltantes
paises = ['', 'AR', 'BR', 'CL', '', 'Colombia', '','equador', '','', 'Venezuela']
print(paises)
# 1ª forma =
res = filter(None, paises)
# 2ª form a
res = filter(lambda pais: len(pais.strip()) > 0, paises)
# 3ª forma
res = filter(lambda pais: pais != '' , paises)
print(list(res))
## Strip - Trim WhiteSpaces both sides - rtrim + ltrim
====================================================================================================================
A diferença entre MAP e filter :
    MAP :-> 2 parametros ( uma função e um iteravel) e retorna um Objeto mapeando a função para cada elemento do Iteravel
    Filter :->  2 parametros ( uma função e um iteravel) e retorna um Objeto filtrando apenas os elementos de acordo com a Função
    A função do Filter retorna Booleanos e baseado nisso, o valor é repassado ao onjecto MAo, fazendo com que o dado seja ou nao selecionado
    A função do MAP retorna o valor processado por uma função, cada um dos dados será retornado novamente
====================================================================================================================
usuarios = [
    {"username": "samuel", "tweets": ["Aodoro bolos", "adoro pitiças"]},
    {"username": "carla", "tweets": ["Aodoro My Cétis", "adoro pitiças"]},
    {"username": "jheff", "tweets": []},
    {"username": "bobi123", "tweets": []},
    {"username": "doggo", "tweets": ["Aodoro bocetas ", "adoro xanas"]},
    {"username": "Gall", "tweets": []},
]

#filtrar usuários inativos no TW
print(usuarios)
# forma 1
# inativos = list(filter(lambda usuario : len(usuario['tweets']) == 0, usuarios))
# forma 2
inativos = list(filter(lambda usuario: not usuario['tweets'], usuarios))
print(inativos)

# Em python , uma LISTA VAZIA tem um valor Booleano FALSO, já uma lista com elementos, possui booleano True
# logo, NOT FALSE -> TRUE
# lista = []
# bool(lista)
# False

# lista = [1]
# bool(lista)
# True
====================================================================================================================
"""
# combinar filter + map
# devemos criar uyma lista contendo 'Sua instrutora é " + nome da pessoa, desde que cada nome tenha menos de 5 caracteres
nomes = ['Ana Julia', 'Giselle', 'Misia', 'Ana', 'Vanessa', 'Kara']
lista = list(map(lambda nome: f'Sua instrutora é :-> {nome}', filter(lambda nome: len(nome.strip()) < 5, nomes)))
print(lista)
