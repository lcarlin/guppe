"""
Dictionary Comprehension
    *   Para crar uma lista:
        lista = [1, 2, 3, 4]
    *   para criar uma Tupla
        tupla = (1,2,3,4)
    *   para criar um COnjunto
        conj = {1, 2, 3 , 4}
    *   para criar um dicionpario
        Dicio =  {1: 'a', 2:'b', 3:'c', 4:'d'}

Sintaxe de Dictionary COmprechension
{chave: valor for in iteravel}
====================================================================================================================
numeros = {'a':1 , 'b':2, 'c':3, 'd':4, 'e':5}
quadrado = { chave:valor **2 for chave, valor in numeros.items()}
print(quadrado)
====================================================================================================================
numeros = [1,2,3,4,5]
quadrado = { valor: valor**2 for valor in numeros }
print(quadrado)
====================================================================================================================
chaves = 'abcde'
valores = [1,2,3,4,5]
mistura = {chaves[i]: valores[i] for i in range (0,len(chaves))}
print (mistura)
====================================================================================================================

"""

numeros = [ 1,2,3,4,5]
res = {num: ('Par' if num%2==0 else 'Impar') for num in numeros }
print(res)