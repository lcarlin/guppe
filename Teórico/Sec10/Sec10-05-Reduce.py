"""
Reduce
OBS: à parir do Python 3+ a função Reduce não é mais uma função Integrada (Built-in)
agora temos que importar e utilizar essa função à partir do Módulo "functools"

Guido Von Rossum : Utilize a função Reduce se vc realmente precida dela. Em todos os casos, 99% das vezes
im Loop for é Mais legivel

Para entender o Reduce: Imagine que você temuja coleçãode dados
dados [ a1, a2, a3, a4, ... , an]
E vocÊ tem uma função que recebe 2 parametros
def funcao(x,y)
    return x**y

Assim como Map() e Filter() , a função reduce recebe 2 parametros ,a funç~çao e o Iterável
Reduce (funcao, dados)

a Funcao Reduce() funciona da seguinte forma:
    Passo 1) res1 = f(a1, a2) # aplica a função nos 2 primeiros elementos da coleção e guarda o resultado
    Passo 2) res2 = f(res1, a3) Aplica a função passando o resultado do Passo 1 + 3º elemento

    Isso é repetido até o final
    Passo 3) res3 = f(res2, a4)
    Passo n) resn = f(res(n-1), an)
    OU seja em caa passo ela aplica a função passando como primeiro argumento o resultado da aplicação anterior. No final
    reduce() ira retornar o final
Alternativamente, poderiamos ver a funcção Reduce() como :
funcao(funcao(funcao(a1,a2),a3),a4),...),an)
====================================================================================================================
====================================================================================================================
====================================================================================================================
====================================================================================================================
====================================================================================================================
====================================================================================================================
====================================================================================================================
====================================================================================================================
====================================================================================================================
"""
# como isso funciona na pratica ?
# Utilizar a função reduce para multiplicar todos os numeros de 1 lista
from functools import reduce
dados = [2,3,4,5,6,7,8,9,11,13,17, 19, 23, 29, 31]
# Para utilizar o reduce, precisamos de uma funcao que recebe 2 parametros
mult = lambda x, y : x * y
res = reduce(mult, dados)
print(type(res))
print(res)

# Agora utilizado Loop
res = 1
for n in dados:
    res *= n

print(res)