""""
Funções com parametro Padrão
    *   Funções onde a passagem de parametro seja Opcional
    *   Permite ser mais flexivel nas funções
    *   Evita erros com passagem de paratetros
    *   Nos permitye trabalhar com exmplos mais loegiveis de códigos
    *   Qualeur tipo de dado pode ser usado como padrão

====================================================================================================================
# Exemplo de função com passagem de parametro opcional
print('Geek University')
print()
====================================================================================================================
# Exemplo de função onde a pssagem de parametro é obrigatorio

def quadrado(numero):
    # return numero * numero
    return numero ** 2
====================================================================================================================
# OBSe se o usuário passar somente UM parametro, ese será atribuido ao NUMERO  e será calculado o quadrado
# se ele passar 2 argumentos, , o primeiro será atribiudo ao numero e o segundo à potencias
# assi será calculada a potencia
def exponencial (numero, potencia=2):
    return numero ** potencia

print (exponencial(2, 10))
print(exponencial(3))

====================================================================================================================
# OBS : em funções Python, os parametros com valores default (padrao)devem sempre estar ao final da declaração
#ERROR
def teste (num=2, potencia ):
    return num ** potencia

# correto
def teste ( potencia, num=2 ):
    return num ** potencia
====================================================================================================================
def mostra_informacao (nome = 'Geek', isntrutor=False):
    if nome == 'Geek' and isntrutor:
        return 'Bem-vindo instrutor Geek !'
    elif nome == 'Geek':
        return 'Eu sei que você era o instrutor'
    return f'Ola {nome}'



print(mostra_informacao())
print(mostra_informacao(isntrutor=True))
print(mostra_informacao('Ezzy'))
====================================================================================================================
def soma(num1, num2):
    return num1 + num2


def mat(num1, num2, fun=soma):
    return fun(num1, num2)


def subrtracao(num1, num2):
    return num1 - num2


print(mat(2, 3))
print(mat(8, 5, subrtracao))

====================================================================================================================


# Escopo - variaveis locais e globais
instrutor = 'Geek' # global variavel

def diz_oi ():
    instrutor = 'Python'
    return f'oi {instrutor}'


print(diz_oi())
print(instrutor)
# Se tivermos uma variavel local com o mesmo nome de uma variavel global, a local tera preferenci a
====================================================================================================================
def diz_oi ():
    instrutor = 'Python'
    return f'oi {instrutor}'
print(diz_oi())
print(instrutor) # NameError
====================================================================================================================
# Atenção com variaveis gloabsi, se puder, evite
total = 0
def incrementa () :
    global  total # avisando que queremos utilizar a variavel global
    total += 1
    return  total

print(incrementa())
print(incrementa())
print(incrementa())
print(incrementa())
print(incrementa())
====================================================================================================================
====================================================================================================================
"""
# Podemos ter funções que são declaradas dentro de funções e também tem uma forma especial de espoco de variavel
def fora():
    contador = 0
    def dentro () :
        nonlocal contador
        contador += 1
        return contador
    return dentro()