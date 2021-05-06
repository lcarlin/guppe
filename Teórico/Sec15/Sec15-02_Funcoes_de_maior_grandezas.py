"""
Funções de Maior Grandeza = Higher order Function - HOF
O Que isso Singinifca?

- QUando uma linguagem de programação suporta HOF indica quepodemos ter funções que retornar outras funções como
    resultado ou mesmo que podemos passar funções como argumentos para outras funções e até mesmo criar variavéis do
    tipo de funções nos nossos programas

OBS: na sessão de funções já utilizamos isso
Em python as funções são cidadoes de primeira Classe - First Class Citizen

====================================================================================================================
# Exemplo: Definindo as funções:
def somar (a, b):
    return a + b

def diminuir (a, b) :
    return a - b

def dividir (a, b) :
    return a / b

def multiplicar (a, b) :
    return a * b

def calcular (num1, num2, funcao):
    return funcao (num1, num2)

# Testando as funções:
print(calcular(4, 3, somar))

print(calcular(4,3, diminuir))

print(calcular(4,3, multiplicar))

print(calcular(4,3, dividir))
====================================================================================================================
# Nested Function - funções ANinhadas
Em  Python podemos ter funcçoes dentro de funçoes que são conhecidas como Nested Functions ou Inner functions
   (Funções Internas )
====================================================================================================================
from random import choice
def cumprimento(pessoa):
    def humor ():
        return choice(('E ai? ', 'Morre, Diabo ', 'Talkey, Forte Abraço '))

    return  humor() + pessoa

print(cumprimento(' Jubille'))
print(cumprimento(' StarFire'))
print(cumprimento('HArley Quinn '))
print(cumprimento('RAven'))
====================================================================================================================
# Retornando funções de outras funções
from random import choice
def faz_me_rir():
    def rir():
        return choice(('hahahahahaha', 'kkkkkkkkkkkk', 'hehehehehehehe'))
    return rir

rindo = faz_me_rir()
print(rindo())
====================================================================================================================
"""

# Inner functios (funções Internas / Nested Functions ) podem acessar o escopo de funções mais externas
from random import choice
def faz_me_rir_novamente(pessoa):
    def dando_risada():
        risada = choice(('hahahahahaha', 'kkkkkkkkkkkk', 'hehehehehehehe', 'LOLOLOLOLOLOLOLO'))
        return f'{risada} {pessoa}'
    return dando_risada

rindo = faz_me_rir_novamente('Poison Ivy')
print(rindo())
print(rindo())
print(rindo())
print(rindo())
print(rindo())