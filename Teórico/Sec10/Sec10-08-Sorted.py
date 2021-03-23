"""
Sorted
OBS: Não confunda com a função sort() que já estudamos em listas. O Sort() só funciona em listas

podemos utilizar o sorted() com qualquer iteravel
Como o próprio nome diz, sorted() só serve para ordenar elemnentos

OBS: o Sorted retorna SEMPRE UMA LISTA com os elementos do Iteravel Ordenado
====================================================================================================================
lista = [4,7,3,8,1,4,2]
lista.sort()
lista

tupla = (4,7,3,8,1,4,2)
====================================================================================================================
OBS: o Sorted retorna SEMPRE UMA LISTA com os elementos do Iteravel Ordenado
numeros = ( 6 ,3, 8, 1 ,2 )
dois = sorted(numeros)
tres = tuple(sorted(numeros))

print(type(dois))
print(type(tres))

print(numeros)
print(sorted(numeros))
print(numeros)
print(dois)
print(tres)
====================================================================================================================
#Adicionando parametros ao Sorted
numeros = [ 6 ,3, 8, 1 ,2 ]
# Ordena do > para o <
print(sorted(numeros, reverse=True))
====================================================================================================================
usuarios = [
    {"username": "samuel", "tweets": ["Aodoro bolos", "adoro pitiças"]},
    {"username": "carla", "tweets": ["Aodoro My Cétis", "adoro pitiças"]},
    {"username": "jheff", "tweets": []},
    {"username": "bobi123", "tweets": [], "cor" : "amarelo"},
    {"username": "doggo", "tweets": ["Aodoro bocetas ", "adoro xanas", "Siabo capeta chupa teta"]},
    {"username": "gall", "tweets": [], "cor":"preto", "musica" : "róque"}
]


# Ordernar pelo tamanho do dicionário
print(usuarios)

# Ordenando pelo Username , alfabeticamente
print(sorted(usuarios, key= lambda usuario : usuario["username"]))
#idem, só que reverso
print(sorted(usuarios, key= lambda usuario : usuario["username"] , reverse=True))
# Pelo numero de Tweets
print(sorted(usuarios, key= lambda usuario : len(usuario["tweets"]) ))
====================================================================================================================

"""
musicas = [
    {"titulo" : "Thunderstruck" , "tocou": 3 },
    {"titulo" : "Smack My Bich Up" , "tocou": 99 },
    {"titulo" : "Sandstorm" , "tocou": 32 },
    {"titulo": "Galinero do Ramirez", "tocou": 17},
]

# Da - tocada pra + tocada
print(sorted(musicas, key=lambda musica : musica["tocou"]))
print(sorted(musicas, key=lambda musica : musica["tocou"], reverse=True))