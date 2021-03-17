"""
Tuplas (tuple)
tuplas são bastante parecidas com listas
Basicamente 2 diferenças:
    1 - tuplas são represantas por parenteses " ( ) " e listas por colchetes " [ ] "
    2 - tuplas são imutáveis - não pode adicionar nem remover elementos apos criados, toda a operação em uma tupla gera
            uma nova tupla
    3 - Aceitam dados Heterogêneos
    4 - o acesso às posições é feito como na lista
        tupla[1]
        tupla[3:7]
        tupla[2:12:2]

    5 - tuplas são mais rápidas que listas
    6 - Deixam o código mais seguro, pois são imutáveis.



====================================================================================================================
tupla1 = (1,2,3,4,5,6)
print (tupla1)
print(type(tupla1))

#As tuplas podem ser criadas assim, sem parendeses sem nada , - cuidado com issos
tupla2 = 1,2,3,4,5,6
print (tupla2)
print(type(tupla2))

# tuplas com 1 elemento ??
tupla3 = (4) # isso nao é uma tupla
print (tupla3) # e retornada tipo INT - cuidado
print(type(tupla3))

tupla4 = (4,) # para fazer tupla com 1 elemento tem que colocar a " , "
print (tupla4) # e retornada tipo TUPLE
print(type(tupla4))
# TUPLAS SÃO DEFINIDAS PELA VIRGULA E NÃO PELO " ( ) "

tupla5 = 5, # para fazer tupla com 1 elemento tem que colocar a " , "
print (tupla5) # e retornada tipo TUPLE
print(type(tupla5))
# TUPLAS SÃO DEFINIDAS PELA VIRGULA E NÃO PELO " ( ) "
====================================================================================================================
# gERAR tuplas com RANGE, com todos os beneficios do Range ( inicio, fim, passo )
tupla = tuple(range(11))
print(tupla)
====================================================================================================================
# Desempacotamento ( unwrapper) de tuplas
tupla = ('Geek University', 'Programação em Python: Essencial ')
escola, curso = tupla
print (escola)
print((curso))
====================================================================================================================
# Tuplas são imutaveis, não existe remoçao, adicçao de eçlemento s
# Metodos Min, Max, Len, Sum, existem , respeitando o tipo de dado.

tupla = (1,2,3,4,5,6 )
print (sum(tupla))
print (max(tupla))
print (min(tupla))
print (len(tupla))
====================================================================================================================
# COncatenação de tuplas
tupla1 = (1,2,3,)
print(tupla1)

tupla2 = (4,5,6)
print(tupla2)

print(tupla1+tupla2)
print(tupla1)
print(tupla2)

# cria uma nova tupla com a concatenação de 2
tupla3 = tupla1 + tupla2
print(tupla3)

# Atribuição substitutiva da tupla1 - sobrescrever o valor
tupla1 = tupla1 + tupla2
print(tupla1)
====================================================================================================================
# Verificar se u m elemeto está na tupla
tupla = (1,2,3)
print ( 3 in tupla)
print ( 4 in tupla)
====================================================================================================================
# interando sobre uma tupla
tupla = (9,7,8)
for n in tupla:
    print(n)

for indice, valor in enumerate(tupla):
    print (indice, valor)
====================================================================================================================
# contando elementos dentro de uma tupla
tupla = ('a','b','c','d', 'a', 'c')
print (tupla.count('a'))

escola = tuple ('Geek University')
print (escola)
print (escola.count('e'))
====================================================================================================================
# Deve-se utilizar TUPLAS sempre que não haver a necessidade de alterar os dados da coleção
# Ex. Meses
meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')
print(meses)

====================================================================================================================
meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')
# Iterar com While/For
i = 0
print ("**********************")
while i < len(meses):
    print(meses[i])
    i += 1
print ("**********************")
for k in meses:
    print(k)
print ("**********************")
for j in range(len(meses)):
    print(meses[j])
====================================================================================================================
meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')
# O Acesso de elementos é o mesmo e possui os mnesmos metodos
print (meses[5])
print( meses.index("Maio")) # Analogo à lista, se o elemento não existir será geradoum ValueError;.
print( meses.index("Maio", 3))
====================================================================================================================
# Deve-se utilizar TUPLAS sempre que não haver a necessidade de alterar os dados da coleção
# Ex. Meses
meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')
print(meses)
print ("**********************")
# Slicing
# tupla[inicio:fim:passo] m
print(meses[5:9])
====================================================================================================================
# copiando tuplas
tupla = (1,2,3)
print (tupla)

nova = tupla   ## Em lista isso gera uma Shallow copy, porem não Tupla isso não ocorre
print(nova)
print(tupla)

outra = (4,5,6)

nova = nova + outra
print (nova)
print (tupla)
====================================================================================================================
====================================================================================================================
====================================================================================================================
"""
