"""
LIst Comprehension :->
    *   Utilizando o List Comprehension podemos gear novaslitas com dados processados à partir de outro Iterável


Sintxase da bagaça
[ dado  for dado in iterável]
====================================================================================================================
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
res = [numero * 10 for numero in numeros]
print(res)

Para entender melhor o que está acontecendo devemos dividir a exporessão em 2 partes:
- A primeira parte : ' for numero in numeros '
- a segunda parte : numero * 10

res = [ numero / 2 for numero in numeros]
print(res)

def funcao (valor):
    return valor * valor

res = [ funcao(numero ) for numero in numeros]
print(res)
====================================================================================================================
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
numerosDobrados = []
for numero in numeros:
    numeroDobro = numero * 2
    numerosDobrados.append(numeroDobro)

print(numerosDobrados)
#Agora com LIstCompreHension
print([ numero * 2 for numero in numeros])
====================================================================================================================

"""
print("=================================================")
# Exemplo 01
nome = 'Geek University'
print ([letra.upper() for letra in nome ])
print(nome.upper())

print("=================================================")
#Exemplo 02
def caixaAlta(nome):
    nome = nome.replace(nome[0], nome[0].upper())
    return nome


amigos =  ['maria', 'julia', 'pedro', 'vanessa', 'stanislau']
print([amigo[0].upper() for amigo in amigos ])

print([amigo.upper() for amigo in amigos ])
print([amigo.title() for amigo in amigos ])
print([caixaAlta(amigo) for amigo in amigos ])

print("=================================================")
# Exemplo 03
print ([ numero ** 1/3 for numero in range (1,11)])

print("=================================================")
# exemplo 4
print ([bool(valor) for valor in [0, [], '', True, 1, 3.1415]])

print("=================================================")
# exemplo 5
print ([str(numero) for numero in [0,2,3,4,5,6,7,8,9]])