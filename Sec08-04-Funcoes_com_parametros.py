"""
funções com parametro de entrada
    *   Funções que recebem dados para ser processados dentro da mesma
    *   Funções podem ter N parametros de entarda. podemos receber tantos parametros quanto necessários, separados por " , "

Se a gente pensar em qualquer programa, geralmente temos
entrada -> processamento -> saida

Nos casos de funções :
-   Funções sem entrada
-   Funções sem saidas
-   Possuem entrada mas não possuem saida
-   Possuem saida mas não tem entrada
-   Possuem entrada e saida
====================================================================================================================
# Refatorando uma função:
def quadrado_de_seth():
    return 7 * 7


def quadrado(numero):
    # return numero * numero
    return numero ** 2

print(quadrado(7))
print(quadrado(2))
print(quadrado(5))
====================================================================================================================
# exemplo 2
def cantar_parabens(aniversariante ):
    print('parabéns proce')
    print('É rola é rola é rola')
    print(f'morre diabo {aniversariante}')


cantar_parabens('MarKYS')
====================================================================================================================
def soma(a, b):
    return a + b


def multimplica(num1, num2):
    return num1 * num2


def outa(num1, b, msg):
    return (num1 + b) * msg
# Obs se for informado um numero errado de parametro ou argumentos, teremos TypeError
====================================================================================================================
# NOmeando Parametros
def nome_completo (nome, sobrenome):
    return f'Seu nome completo é {nome} {sobrenome}'

print(nome_completo('Negao', 'do Zap'))

# A diferenca entre parametros e Argumentos
# parametros sao variaveis na definicao de uma função
# Argumentos são dados passados durante a execução de uma função
# A ordem dos parametros importa

#Argumentos Nomeados -> KeyWordArguments
#Caso utilizamos nomes dos parametros nos argumentos para informalos, podemos utilizar qualquer ordem:
print(nome_completo(nome='Scalet', sobrenome='Johansenn'))
print(nome_completo(sobrenome='Grey', nome='Sasha'))
====================================================================================================================
"""


# Erro comum na utilização do return
def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total += num
    return total


lista = [1, 2, 3, 4, 5, 6, 7, 8]
print(soma_impares(lista))
