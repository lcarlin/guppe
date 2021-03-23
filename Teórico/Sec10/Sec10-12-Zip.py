"""
ZIP -> cria um iterável chamado ZipObject que agrega elementos de cada um dos iteráveis passados como entrada em Pares

====================================================================================================================
lista1 = [1,2,3]
lista2 = [4,5,6]
zip1 = zip (lista1, lista2, 'abc')

print(zip1)
print(type(zip1))
#Sempre podemos gear uma lista, Tupla, ou dicionároi
zip1 = zip (lista1, lista2, 'abc')
print(list(zip1))
zip1 = zip (lista1, lista2, 'abc')
print((tuple(zip1)))
zip1 = zip (lista1, lista2, 'abc')
print (set(zip1))
zip1 = zip (lista1, lista2)
print(dict(zip1))
print("**********************")
# OBS o zip utiliza como parametroo menor tamanho de iterável, isso signifca que se estiver trabalhando com iteráveis
# de tamanhos diferentes, irá parar quando elementos do mentor ityerável acabar.
lista3 = [7,8,9,10, 11]
zip2 = zip(lista1, lista2, lista3)
print(list(zip2))
====================================================================================================================
tupla = 1,2,3,4,5
lista = [6,7,8,9,0]
dicionario = {'a':11, 'b':12, 'c':13, 'd':14, 'e':15}
zt = zip(tupla, lista, dicionario)
print(list(zt))
print("**********************")
dados = [(0,1), (1,2) ,(2,3), (3,4), (4,5)]
print(list(zip(*dados)))
====================================================================================================================
"""

prova1 = [80,91,78]
prova2 = [98,89,53]
alunos = ['Maria', 'Pedro', 'Karla']

final= {dado[0]:max(dado[1], dado[2]) for dado in zip (alunos, prova1, prova2)}
print(final)
print("**********************")
#podemos utilizar o map pra fazer isso
final = zip (alunos, map(lambda nota: max(nota),zip(prova2, prova1)))
print (dict(final))