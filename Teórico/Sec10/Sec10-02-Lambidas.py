"""
Lambdas:
    *   conhecidas por expressões Lambdas ou simplesmente Lambdas são funções sem nomes, ou seja, funções anonimas

# Exemplo de função em Python
def soma ( a, b) :
    return a + b
====================================================================================================================
def funcao(x):
    return 3 * x + 1

print(funcao(4))

# Exemplo de expressão Lambda
# lambda x : 3 * x + 1

# E como utilizar a expressão Lamda?
calc =  lambda x : 3 * x + 1
print(calc(4))
====================================================================================================================
Podemos ter expressões Lambdas com multiplas entradas

nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()
print(nome_completo(' diones ', ' felicidade  '))
====================================================================================================================
# Em funções Python, podemos ter NENUM ou Varias entradas e em lambdas também
odeo = lambda: ' como não odiar o Nelipe Fetto'

uma = lambda x: 3 * x + 1
duas = lambda x, y: (x * y) ** 0.5
tres = lambda x, y, z: 3 / (1 / x + 1 / y + 1 / z)
# n = lambdax1, x2, .....xn : <expressao>
print(odeo())
print(uma(6))
print(duas(5,7))
print(tres(3,6,9))
# oBS :-> se passarmos a quantidade errada de argumentos do que parametros esperados, teremos TypeErrors
====================================================================================================================
autores = ['George Orwells','Frank Herbert','Aldus Huxley', 'Phillip K., Dick', 'H. P. Lovecraft', 'Aleister Crowley',
           'Isaac Asimov', 'H. G. Wells', 'Arthur C. Clack', 'Orson Scott Card']
print(autores)
# Exemplo classico de como se deve usar a Exprssão de Lambidas
autores.sort(key=lambda sobrenome: sobrenome.split (' ')[-1].lower())
print(autores)
====================================================================================================================

"""

# Função Quadrática:
# f(x) = a * x ** 2 + b * x + c
#Fefinindo a funcao:
def geradorFuncaoQuadratica (a, b, c ):
    """
    retorna a função f(x) =  a * x ** 2 + b * x + c
    :param a:
    :param b:
    :param v:
    :return:
    """
    return lambda x :  a * x ** 2 + b * x + c

teste = geradorFuncaoQuadratica(2,3,-5)
print(teste(0))
print(teste(1))
print(teste(2))

print(geradorFuncaoQuadratica(3,0,1)(2))