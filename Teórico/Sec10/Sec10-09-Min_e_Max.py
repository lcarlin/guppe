"""
Min e Max
max() retorna o maior valor de um iterável OU o maior de 2 ou mais elementos
min() retorna o Menor valor de um iteravel ou o menor de 2 ou mais elementos
====================================================================================================================
lista = [1, 8, 4, 89, 99, 24, 34, 129]
print(max(lista))

tupla = (1, 8, 4, 89, 99, 24, 34, 129)
print(max(tupla))

conjunto = {1, 8, 4, 89, 99, 24, 34, 129}
print(max(conjunto))

dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 89, 'e': 99, 'f': 224, 'g': 34, 'h': 129}
print(max(dicionario))  # atencao , a ordenacao sempre será pela CHAVE
print(max((dicionario.values()))) ## aqui é que ordena pelo valor e nbao pela chave

====================================================================================================================
# Faça um programa que receba 2 valores do usuário e mostre o MAIOR ( crássico em programassão )
val1 = int(input('Informe  o 1º Valor :-> '))
val2 = int(input('Informe  o 2º Valor :-> '))
print(f'E o maior  é -> {max(val1, val2)} ')

====================================================================================================================
lista = [1, 8, 4, 89, 99, 24, 34, 129]
print(min(lista))

tupla = (1, 8, 4, 89, 99, 24, 34, 129)
print(min(tupla))

conjunto = {1, 8, 4, 89, 99, 24, 34, 129}
print(min(conjunto))

dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 89, 'e': 99, 'f': 224, 'g': 34, 'h': 129}
print(min(dicionario))  # atencao , a ordenacao sempre será pela CHAVE
print(min((dicionario.values()))) ## aqui é que ordena pelo valor e nbao pela chave
====================================================================================================================
val1 = int(input('Informe  o 1º Valor :-> '))
val2 = int(input('Informe  o 2º Valor :-> '))
print(f'E o maior  é -> {min(val1, val2)} ')
====================================================================================================================
# Outros Exemplos:
nome = ['Annya', 'SamSOm', 'Doralyce', 'Timas', 'Ollivander', 'Bek']

print(max(nome, key= lambda nome:len(nome)))
print(min(nome, key= lambda nome:len(nome)))
====================================================================================================================

"""

musicas = [
    {"titulo" : "Thunderstruck" , "tocou": 3 },
    {"titulo" : "Smack My Bich Up" , "tocou": 99 },
    {"titulo" : "Sandstorm" , "tocou": 32 },
    {"titulo": "Galinero do Ramirez", "tocou": 17},
]
print(max(musicas, key=lambda musica:musica['tocou']))
print(min(musicas, key=lambda musica:musica['tocou']))

print(max(musicas, key=lambda musica:musica['tocou']))
print(min(musicas, key=lambda musica:musica['tocou']))
print("**********************")
print(max(musicas, key=lambda musica:musica['tocou'])['titulo'])
print(min(musicas, key=lambda musica:musica['tocou'])['titulo'])
print("**********************")
# Agora sem Max, Sem Min e sem Lambidas
# como encontrar a mais e menos tocada ?!?!?!?!?
max = 0
nome = ''
for musica in musicas:
    if musica['tocou'] > max:
        max = musica['tocou']
        nome = musica['titulo']

print(f' A musica {nome} tocou {max} vezes ')
print("**********************")
# Jeito de Portugues
for musica in musicas:
    if musica['tocou'] == max:
        print(musica['titulo'])