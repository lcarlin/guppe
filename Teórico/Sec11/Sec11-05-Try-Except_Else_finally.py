"""
Try / Except / Else / Finnaly
Toda entrada de dados  deve ser tratada
A função do Usuário é destruir o seu sistema
====================================================================================================================
# Else :-> é esecutado somente se não ocorrer o erro
num = 0
try:
    num = int (input('Informe um numero: '))
except ValueError:
    print('Valor Incorreto')
else:
    print(f'Você digitou :-> {num}')
====================================================================================================================
O Bloco FINALLY É SEMPRE EXECTADO, independente se houve ou não excessão
# O Finally é usado para Fechar E/OU desalocar recursos.
# Else :-> é esecutado somente se não ocorrer o erro
num = 0
try:
    num = int (input('Informe um numero: '))
except ValueError:
    print('Valor Incorreto')
else:
    print(f'Você digitou :-> {num}')
finally:
    print('Executando o Finnally')
====================================================================================================================
# Você é o responsável pelas entradas de suas funções, engrão0: trate-asss
def dividir (a, b):
    try:
        return int(a) / int(b)
    except ValueError :
        return 'Valores incorretos'
    except ZeroDivisionError:
        return  'Não é possivel dividir por zero '

num1 = int(input('Informe o 1º num :-> '))
num2 = int(input('Informe o 2º num :-> '))

print(dividir(num1,num2))
====================================================================================================================
Tratamento generico
# Você é o responsável pelas entradas de suas funções, engrão0: trate-asss
def dividir (a, b):
    try:
        return int(a) / int(b)
    except :
        return 'Um Erro ocorretu '

num1 = int(input('Informe o 1º num :-> '))
num2 = int(input('Informe o 2º num :-> '))

print(dividir(num1,num2))
====================================================================================================================
"""


def dividir (a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Um Erro ocorretu :-> {err} '

num1 = input('Informe o 1º num :-> ')
num2 = input('Informe o 2º num :-> ')

print(dividir(num1,num2))