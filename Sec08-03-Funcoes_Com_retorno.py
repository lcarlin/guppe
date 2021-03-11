"""
F|unções com retorno
OBS:     em Python, quando uma função não retorna nenhum valor, o retorno padrao é o tipo None
OBS:    Funções em Python que retornam valores, devem retorna-los com a palavra reservada Return
OBS:    Não precisa necessáriamente criar uma variavel pra receber o retorno de uma função. POde passar o resultado
        da execução para outras funções aninhadas
OBS:    Return  - Finaliza a função - ou seja : ela SAI da execução da função
                - Podemos er um uma função diferentres RETURNs
                - Podemos em uma função, retornar qualquer tipo de dado e até mesmo multiplos valores
====================================================================================================================
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
ret = numeros.pop()
print(f'Rentoirno de POP {ret}' )
print(numeros.pop())
ret_pr = print(numeros)
print(f'Retorno de O Print {ret_pr}')

====================================================================================================================
def quadrado_de_sete():
    print (7*7)


ret = quadrado_de_sete()
print(f'E o retorno de ret é {ret}')
====================================================================================================================
# refatorar essa função para retornar um valor
def quadrado_de_sete():
    return 7 * 7

# Auqi é criada uma variavel pra receber o retorno da função
ret = quadrado_de_sete()
print(f'E o retorno de ret é {ret}')

print(f'retorno é {quadrado_de_sete() + 1 }')
====================================================================================================================
# Refatorando a 1º função
def diz_oi():
    return 'Oi !!! !! ! '

print(diz_oi())
alguem = 'Pedro'
print(diz_oi() + alguem )
====================================================================================================================
# Exemplo 1
def diz_oi() :
    print('Estou sendo executado antes do retorno ... .. .')
    return 'oi'
    print('Estou a ser executado após o REtorno ')


print(diz_oi())
====================================================================================================================
# Exemplo 2
def nova_funcao():
    variavel = None
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return  'Bolas'


print(nova_funcao())
====================================================================================================================
# Exemplo 3 - desempacotamento
def outra_funcao():
    return 2 , 3, 4, 5

#num1, num2 , num3, num4 = outra_funcao()
#print(num1, num2, num3, num4) # aqui é impresso como variaveis separadas
print(outra_funcao()) # aqui é impresso como Tuplas
print(type(outra_funcao()))
====================================================================================================================
# Criar uma função para Jogar 1 moeda, dando CAra_e_coroa
from random import random
def joga_moeda():
    #gera um numero pseud-aleatorio entre o e 1 [
    valor = random()
    if valor > 0.5:
        return 'Cara'
    return 'Coroa'

print(joga_moeda())
====================================================================================================================
====================================================================================================================
====================================================================================================================
====================================================================================================================
====================================================================================================================
"""
#Erros comum na utilização de uma função, nem é erro mas sim codificação desnecessária.
def eh_impar():
    numero = 5
    if numero % 2 != 0 :
        return True
    else:
        return False