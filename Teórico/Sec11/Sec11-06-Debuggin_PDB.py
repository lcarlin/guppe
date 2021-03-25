"""
Debugando com PDB
PDB :-> Python Debugger
Bug :-> Insecto

====================================================================================================================
def dividir (a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Um Erro ocorretu :-> {err} '

num1 = input('Informe o 1º num :-> ')
num2 = input('Informe o 2º num :-> ')

print(dividir(num1,num2))
====================================================================================================================

"""
# Existem formas mais profissionais de se fazer Debug, utilzando o Debugger
# Em Python podemos fazer isso em diferentres IDEs, como  o PyCharm ou utiliznao o
# O PDB - Python debugger
# Para utilizar o Python Debugger , tem que importatr a Biblioteca e a função Set_trace()
# comandos Básicos do PDB
# l - listar onde estamos n código
# n - proxima linha
# p - imprime variavel
# c - continua a execução  - finalizar o debigger


nome = 'Apalpa '
sobrenome = 'MInha Naba'
#import pdb; pdb.set_trace()
breakpoint()
nome_compreto = nome + ' ' + sobrenome
curso = 'Programaçao em Pyhon: Essencial '

final = nome_compreto +' faz o curso ' + curso

print(final)

# Porque utilizar com o ";" ??? ?? ?
# O Debugg é utilizado durante o desenvolvimento, costimamos realizaar os imports de bibliotecas no nicio do arquivo
#Por  isso colocamos "import pdb; pdb.set_trace()" apenas no ponto onde vamos utilizar
# à partir do Python 3.7 não é mais necessário importatr a biblioteca PDB, pois o comando de debug foi imcorporara como
# built-in (integrada) e pe chamada breakpoint()
# cuidado com conflito com nomes de variaveis e os comandos do PDB
# eVITE USAR variaveis com nomes de letras simples, como L, N , P C ., pois são os comandos do PDB