"""
Conjuntos:
    *   Quando falamos em conjuntos em qualquer LImguagem, estamos referenciando à teoria de conjuntos de matematicas
    *   Em Pyhton, conjuntos são chamaos de Sets, analogo à matematica, :
        -   Sets não possuem valores duplicados
        -   Não possuem valores ordenados
        -   A ordem de inclusão dos itens não é a mesma arqmzenada em memoria
        -   Elementos não sao acessados via Indice ( connjunto não é indexado)
    *   São bons para se utilizar quando precisamos armazenar elementos mas não nos importamos com a ordenação
    *   QUando não precisamos nos preoocupar com chaves, valores e itens duplicados
    *   Os conjuntos (sets) são referenciados em Python com  " { } " chaves
    *   Diferença entre conjuntos (set) e mapas (dict) :
        -   Um dicionario possui chava/valor
        -   Conjunto possui somente valor
====================================================================================================================
# Definindo um conjunto
# forma 1
s = set({1, 2, 3, 3, 3, 4, 5, 5, 5, 6, 7, })  # repare que temos valores que se repetem
# mas os valores repetidos não sãoi inseridos no Set
# Ao criar um conjuto, caso seja adicionado um valor ja existente o mesmo será ignmorado, e não fará parte do conjhuto
# sem dar error
print(s)
print(type(s))  #
print("**********************")

# forma 2
s = {1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 8, 7, 5}
print(s)
print(type(s))  #
print("**********************")

#
s = set('Geek University')
print (s)
print(type(s))  #
print("**********************")

lista = [1,2,3,3,4,5,6,6,6,7,8,9,9,9]
s = set (lista)
print (s)
print (lista)
print("**********************")

tupla = (1,3,4,3,6,7,8)
s = set(tupla)
print((tupla))
print(s)
====================================================================================================================
s = set({1, 2, 3, 3, 3, 4, 5, 5, 5, 6, 7, })
print(s)
print(type(s))  #
print("**********************")

# verificar se um elemento está no conjunto, como foi feita em outras coleções
if 99 in s :
    print ("Localizei o valor ")
else:
    print ('nada feito ')
====================================================================================================================
# importante lembrar que alem de não termos valores duplicados, não temos ordenação aluma
# listas aceitam valores duplicados
lista = [99, 2, 34, 23, 12, 1, 44, 5, 2, 34]
print(lista)
print(len(lista))
print("**********************")
# Tuplcas tbm aceitam valores duplicados
tupla = (99, 2, 34, 23, 12, 1, 44, 5, 2, 34)
print(tupla)
print(len(tupla))
print("**********************")
# Dicionários não aceitam CHAVES duplicadas
dicionario = {}.fromkeys([99, 2, 34, 23, 12, 1, 44, 5, 2, 34], 'dict')
print(dicionario)
print (len(dicionario))
print("**********************")
# Conjuntos não aceitam valores duplicados.
conjunto = {99, 2, 34, 23, 12, 1, 44, 5, 2, 34}
print(conjunto)
print (len(conjunto))
print("**********************")
====================================================================================================================

# Assim como todo outro tipo d conjunto python, podemos ter dados heterogenos em SETs
s = { 1 ,'b', True, 32,444, 998, "Casa"}
print (s)
print(type(s))  #
print("**********************")

for valor in s :
    print (valor)
====================================================================================================================
# Usos interessante com SETs
# retirar a duplicidade de uma lista.
# Dado uma lista com varios elementos (repetidos entre eles) , o Set tira as repetições.
cidades = ['Belzonti',
           'São Paulo',
           'Londrina',
           'Big Field',
           'Cui-A-Ba',
           'Belzonti',
            'Belzonti',
           'São Paulo',
           'Cui-A-Ba',
           'Big Field',
           'Big Field' ]
total = len(cidades)
distintos = len(set(cidades))

print("total de visitntes  :=-> ", total)
print("total de cidades    :=-> ", distintos)
====================================================================================================================
# Adicionando elementos ao conjunto
# se for adicionar um elemento duplicado, não gera erro, simplistenmte é ignorado, talkey
s = {1,2,3,4}
print (s)
s.add(5)
print (s)
print("**********************")
====================================================================================================================
# Remover um elemento de um conjunto
s = {1,2,3,4}
print (s)
# forma 1
s.remove(3) ## é o valor e não o indice. atenção nisso .
## nenhum valor ´pe retornaro
## se for tentar remover um valor que não existe , dá Key Error - cuidado com isso .
print (s)
print("**********************")
====================================================================================================================
# Remover um elemento de um conjunto
s = {1,2,3,4}
print (s)
# forma 2
s.discard(2)
# com o Discard não é gerado erro quando o valor não existe. Optar por ela
print (s)
print("**********************")
====================================================================================================================
# copiando um conjunto pra outro
# Deep copy e shallow copy
s = {1,2,3,4}
print (s)
# forma 1 de copya = Deep copy
novo = s.copy()
print(novo)
novo.add(5)
print(s)
print(novo)
print("**********************")
====================================================================================================================
# copiando um conjunto pra outro
# Deep copy e shallow copy
s = {1,2,3,4}
print (s)
# forma 2 Shallow copy
novo = s
print(novo)
novo.add(5)
print(s)
print(novo)
print("**********************")
====================================================================================================================
# remover todos os elementos do conjunto
s = {1,2,3,4}
print (s)
s.clear()
print (s)
====================================================================================================================
# Metodos matematicos de conjuntos.
# lista1 estudandes curso Python
estudantesPython = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
# lista2 estudantes curso Java
estantesJava = {'Fernando','Gustavo','Julia', 'Ana', 'Patricia'}
#Note que alguns alunos estão nos 2 cursos.
# Gerar um conjunto com nomes de estudandes Unicos
# forma 1 Union
unicos1 = estudantesPython.union(estantesJava)
print(unicos1)

print("**********************")
# forma 2 - usando o Pipe " | "
unicos2 = estudantesPython | estantesJava
print(unicos2)

print("**********************")
# forma 2 - usando o Pipe " | "
unicos2 = estudantesPython | estantesJava
print(unicos2)

====================================================================================================================
# lista1 estudandes curso Python
estudantesPython = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
# lista2 estudantes curso Java
estantesJava = {'Fernando','Gustavo','Julia', 'Ana', 'Patricia'}
#Note que alguns alunos estão nos 2 cursos.
# Gerar uma lista de estudantes que estão em ambos os cursos
# forma 1 Intersect
unicos1 = estantesJava.intersection(estudantesPython)
print(unicos1)
print("**********************")

# forma 2 " & "
unicos2 = estantesJava & estudantesPython
print(unicos2)
print("**********************")
====================================================================================================================
# lista1 estudandes curso Python
estudantesPython = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
# lista2 estudantes curso Java
estantesJava = {'Fernando','Gustavo','Julia', 'Ana', 'Patricia'}
# conjunto qde estudantes de um curso que NÃO ESTÃO no outro
soPython = estudantesPython.difference(estantesJava)
soJava = estantesJava.difference(estudantesPython)
print(f'So Java    :=-> {soJava}')
print(f'So Python  :=-> {soPython}')
print("**********************")
====================================================================================================================
# Soma , maior , Menor , total
# se valores todos inteiros ou reais
s = {1,2,3,4,5,6,7,8,9}
print('Soma  :=-> ', sum(s))
print('Min   :=-> ', min(s))
print('Max   :=-> ', max(s))
print('total :=-> ', len(s))
====================================================================================================================
"""
