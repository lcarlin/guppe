"""
Entendedo o *args
O *args é um parametro como outro qualquer, isso significa que voc~e poderá chamar de qualquer coisa, desde que começe
com um *
Por Exemplo:
*xis
mas Por convençao, a comunidade deciciu que iria adotar o nome ' *args ' para defini-lo
Mas, o que é o *args ?
OParametro *args utilizado em uma função, coloca os valores extras informados como entrada em uma Tupla, então desde
já lembre-se que tuplas são IMUTAVEIS
====================================================================================================================
#Exemplo
def soma_todos_numeros_old (num1, num2, num3):
    return num1 + num2 + num3

def soma_todos(*args):
    # como o *args é uma TUPLA, pode se entao usar uma função
    #total = 0
    #for numero in args:
    #    total += numero
    #
    #return total
    return (sum(args))

# NOte-se que nesse caso, vc tem 2 parametros OBRIGATORIOS, e o resto vaipro *args , casoi existe
def soma_todos_2(nome, sobrenome, *args):
    return (sum(args))
# print(soma_todos_numeros_old(4,6,9))

print(soma_todos(3,5,8))
print(soma_todos(3,6,9,2,5,8))

print(soma_todos_2('Nome', 'Sobrenme', 1,2,3,4,5,6))
====================================================================================================================
def verifica_info(*args):
    if 'Geek' in args and 'Univeristy' in args:
        return 'Olá nerde'
    else:
        return 'Sei lá quem vc é !'

print(verifica_info())
print(verifica_info(1, True, 'Univeristy', 4, False, 'Geek'))
print(verifica_info('University', 3.1415))
====================================================================================================================

"""

def soma_todos(*args):
    return (sum(args))


numeros = [1,2,3,4,5,6,7,8,9]
# OBS o Asterisco sever para que informemos ao Puython que estamos passando como argumento uma coleção de dados
# destaforma ele saberá que rpecisara antes desempactatr esses dados
print(soma_todos(*numeros))