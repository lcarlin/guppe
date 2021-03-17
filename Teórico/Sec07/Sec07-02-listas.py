"""
LIstas em Python funcionam como vetores/matrizes arrays em outras libguagens, com a diferença dew serem dinamicos
e tambem poder colocar qualquer tipo de dados .
Liguagem C/JAVA
    - possui tamanho e tipo de dados fixos;
    ou seja , nestas linguans se vc criar uma array int com tamanho 5 , essse array será sempre do tipo inteiro e vc
    podera gravar apenas 5 valores.


Ja no Python
    - Dinamico, não possui tamahnho fixos, ou seja podemos criar a lista e simplesmente ir adicionando elementos
    - As listas não possuem tipos de dados fixo, Podemos colocar qualquer tipo de dados misturados
    - as listas em Python são representaas por " [ ] "
    - as listas são MUTÁVEIS

====================================================================================================================
Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
type ("a")
<class 'str'>
type (1)
<class 'int'>
type (True)
<class 'bool'>
type([1,2,3])
<class 'list'>
====================================================================================================================
lista1 = [ 1, 99, 4 , 27 , 15 , 22 ,3 ,1 ,44 , 42 ,27 ]
lista2 = ['G', 'e','e','k', ' ', 'U', 'n', 'i', 'v', 'e','r', 's', 'i', 't', 'y']
lista3 = []
lista4 = list(range(11))
lista5 = list('Geek Univerisity')
podemos chegar facilmete se um valos esta na lista
num = 18
if num in lista4:
    print(f"Achei {num}")
else:
    print (f"Nao Achei {num}")

Essa técninica é possivel com quyalquer tipo de listas

lista5 = list('Geek Univerisity')
if 'e' in lista5:
    print("Encontrei a letra e ")
else:
    print ("Nao ac hei e letras e")


====================================================================================================================
Achar todos os metodos pertinentes à listas
dir(lista5)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__',
 '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__',
 '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__',
 '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__',
 '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove',
 'reverse', 'sort']
====================================================================================================================
Podemos facilmente orderar uma lista :
lista1 = [ 1, 99, 4 , 27 , 15 , 22 ,3 ,1 ,44, 42 ,27 ]
lista1.sort()
print (lista1)
OBS. a ordenação é feita na propria lista, alteranbdo-a

lista5 = list('Geek Univerisity')
print (lista5)
lista5.sort()
print (lista5)
====================================================================================================================
Podemos facilmente contar o numero de ocorrencias de valor em uma lista:
lista1 = [ 1, 99, 4 , 27 , 15 , 22 ,3 ,1 ,44 , 42 ,27 ]
print(lista1.count(1))

lista5 = list('Geek Univerisity')
print (lista5.count('e'))
====================================================================================================================
Adicionar elementos/valores em listas, utilizamos o metodo append:
lista1 = [ 1, 99, 4 , 27 , 15 , 22 ,3 ,1 ,44 , 42 ,27 ]
print(lista1)

lista1.append(42)
print(lista1)
OBS: com append apenas conseguimos adicionar um elemento por vez .
Porem pode-se adicionar uma outra lista a lista

adiciona a sublista abaixo como um unico elemento
lista1.append([8,3,1])
print(lista1)

if [8 , 3 , 1]  in lista1:
    print ('encontrei a sublista na lista')
else:
    print ('nada feito ')

Agora, adiciona os elemetos abaixo individualmente e nçao como listas
o Extend não aceita valor unico, para isso use o Append
lista1.extend([123,44,67])
print(lista1)
lista1.extend('Geeka')
print(lista1)
====================================================================================================================
POdemos inserir um valor em qualquer posição da listas, deslocando os demais valores
lista1 = [ 1, 99, 4 , 27 , 15 , 22 ,3 ,1 ,44 , 42 ,27 ]
print(lista1)

lista1.insert(2,'novo valor')
print(lista1)
====================================================================================================================
Podemos juntar 2 listas
lista1 = [ 1, 99, 4 , 27 , 15 , 22 ,3 ,1 ,44 , 42 ,27 ]
lista2 = ['G', 'e','e','k', ' ', 'U', 'n', 'i', 'v', 'e','r', 's', 'i', 't', 'y']
lista6 = lista1 + lista2
print (lista6)
#OU
lista1.extend(lista2)
print(lista1)
#OU
lista1 = lista1 + lista2
print(lista1)
====================================================================================================================
Para inverter a lista inteira use reverse
lista1 = [ 1, 99, 4 , 27 , 15 , 22 ,3 ,1 ,44 , 42 ,27 ]
lista2 = ['G', 'e','e','k', ' ', 'U', 'n', 'i', 'v', 'e','r', 's', 'i', 't', 'y']
print(lista1)
print(lista2)
#para imprimir a lista reversa
#forma 1
lista1.reverse()
lista2.reverse()
## ou
#forma 2
print(lista1[::-1])
print(lista2[::-1])

print(lista1)
print(lista2)
====================================================================================================================
PAra copiar uma lista,
lista1 = [ 1, 99, 4 , 27 , 15 , 22 ,3 ,1 ,44 , 42 ,27 ]
lista2 = ['G', 'e','e','k', ' ', 'U', 'n', 'i', 'v', 'e','r', 's', 'i', 't', 'y']

lista6 = lista2.copy()
print(lista6)
====================================================================================================================
contar o tamanho das lista ( total de elemento)
lista1 = [ 1, 99, 4 , 27 , 15 , 22 ,3 ,1 ,44 , 42 ,27 ]
lista2 = ['G', 'e','e','k', ' ', 'U', 'n', 'i', 'v', 'e','r', 's', 'i', 't', 'y']

print (len(lista1))
print(len(lista2))
====================================================================================================================
remover os elementos de uma lista  ( do ultimo elemento para "cima"
O pop remove o ultimo elemento e o retorna para algum lugar
lista5 = list('Geek Univerisity')
print(lista5)
x = lista5.pop()
print(lista5)
print (x)

# remove um i9tem de uma posição especifica (começando de ZERO ) , deslocando os demais elementos
y = lista5.pop(3)
print(lista5)
print (y)
====================================================================================================================
PAra limpar, zerar a lista
lista5 = list('Geek Univerisity')
print(lista5)
lista5.clear()
print(lista5)
====================================================================================================================
PAra replicar os elementos em uma lista
nova = [1, 2, 3]
nova = nova * 3
print (nova)
[1, 2, 3, 1, 2, 3, 1, 2, 3]
====================================================================================================================
#converter uma string em lista
O Split por padrão separar os elemehntos da lista pelo espaço em branco

curso = "Programação em Python: Essencial"
curso2 = curso.split()
print(curso2)

PAra usar um caractere como separador
curso = "Programação,em,Python:,Essencial"
print(curso)
curso2 = curso.split(",")
print(curso2)
print(curso2)
====================================================================================================================
#Convertendo uma lista em uma estrigue
lista6 = ['Programaçao', 'Em', 'Python:', 'Esencial']
print(lista6)

curso = ' '.join(lista6)
print(curso)

curso = ' -'.join(lista6)
print(curso)

curso = '$'.join(lista6)
print(curso)

====================================================================================================================
# As lista pode ter dados heterogeneos
lista6 = [ 1, 2.34, True, 'Geek', 'd', [1,2,3], 45345345345 ]
====================================================================================================================
# Utilzando FOR
lista1 = [ 1, 99, 4 , 27 , 15 , 22 ,3 ,1 ,44 , 42 ,27 ]
for elemento in lista1:
    print(elemento)
====================================================================================================================

# uTILIZANDO whILE
carrinho = []
produto = ""
while produto != "sair":
    print ("Adicione um produto ou 'sair' pra sair : ")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)
====================================================================================================================
Criar listas com variáveis
numeros = [1, 2, 3, 4, 5 ]
num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5
numeros2 = [num1, num2, num3, num4, num5 ]
print (numeros2)
print(numeros)
====================================================================================================================
# Acesso aos elementos é de forma indexada
cores = ['verde', 'amarelo', 'azul', 'branco']
print(cores[0])
print(cores[1])
print(cores[2])
print(cores[3])

# realizar o acesso aos elementos de forma indexada inversa
cores[-1]
'branco'
cores[-2]
'azul'
cores[-3]
'amarelo'
cores[-4]
'verde'


====================================================================================================================
cores = ['verde', 'amarelo', 'azul', 'branco']

for cor in cores :
    print(cor)

indice = 0
while indice < len(cores):
    print(cores[indice])
    indice += 1

====================================================================================================================
cores = ['verde', 'amarelo', 'azul', 'branco']

#para pegar o indice de uma posução especifica
for indice, cor in enumerate(cores):
    print(indice, cor)
====================================================================================================================
# as litas aceitam valores repetidos
lista = []
lista.append(42)
lista.append(42)
lista.append(33)
lista.append(33)
lista.append(42)

print(lista)
====================================================================================================================
# Encontrar o indice de um elemento na listas
numeros = [5, 6, 7, 5, 8, 9, 10]
# em qual indicie está o valor ' 6 '
print (numeros.index(6))

# em qual indicie está o valor ' 9 '
print (numeros.index(9))


# em qual indicie está o valor ' 4 ', como não existe dá error
#print (numeros.index(4))

# pode-se fazer bisca em um range, indicie inicial e final
print (numeros.index(5, 1))
print (numeros.index(8, 3, 6))
====================================================================================================================
lista[inicio:fim:passo]
range[inicio:fim:passo]
lista = [1,2,3,4]

# Iniciando do elemento 1 (2º elemento ) e indo até ao final
print (lista[1:])

#pegar todos
print (lista[::])

# imprime à partir do 2ª elemento
print (lista[1:])

# imprie ate o 2º elemento ( limite é o 3º)
print (lista[:2])

#Inicia no 2ª elemento até o 3º
print(lista[1:3])

# Contando do Final da lista, vá até o elemento de indice N
print(lista[1:-1])

#começa em 1 (2º elemento) até o final pulando de 2 em 2
print (lista[1::2])

# idem ao anterior,m começando na pos 0
print (lista[::2])
====================================================================================================================
# invertendo valores em uma lista
nomes = ['Geek', 'Univerisity']
print(nomes)
nomes[0], nomes[1] = nomes[1], nomes[0]

print(nomes)

# invertendo usando metodos nativos
nomes = ['Geek', 'Univerisity']
nomes.reverse()
print(nomes)
====================================================================================================================
# Soma, Máxmimo, minimo, tamanho de uma lista
# Somente Se valores inteiros e reais

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(sum(lista))
print(max(lista))
print(min(lista))
print(len(lista))

====================================================================================================================
# Transformar uma lista em uma TUPLA
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lista)
print(type(lista))

tupla = tuple(lista)
print(tupla)
print(type(tupla))
====================================================================================================================
# Desempacotamento de listas
lista = [ 1,2,3]
num1 , num2 , num3 = lista
print(num1)
print(num2)
print(num3)

====================================================================================================================
# Copia de listas - cuidado com isso
# Shallow - raza - duas listas apontam para o mesmo endereço de memoria, logo, mesma lista
# Deep - profunda  uma cópia distinda da mesma lista, enderecps de memoria diferente, logo, inicialmente dados iguis,
lista = [1,2,3]
print (lista)
nova = lista.copy()   ## deep copy
nova.append(4)
print(lista)
print(nova)

lista = [1,2,3]
print (lista)
nova = lista   ## Shallow
nova.append(4)
nova.append(4)
====================================================================================================================
====================================================================================================================
====================================================================================================================
====================================================================================================================
====================================================================================================================

"""
# Iterando com as listas
lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]
lista2 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']
lista3 = []
lista4 = list(range(11))
lista5 = list('Geek Univerisity')
lista6 = [1, 2.34, True, 'Geek', 'd', [1, 2, 3], 45345345345]
cores = ['verde', 'amarelo', 'azul', 'branco']

# Copia de listas - cuidado com isso
# Shallow - raza - duas listas apontam para o mesmo endereço de memoria, logo, mesma lista
# Deep - profunda  uma cópia distinda da mesma lista, enderecps de memoria diferente, logo, inicialmente dados iguis,
lista = [1,2,3]
print (lista)
nova = lista   ## Shallow
nova.append(4)
print(lista)
print(nova)