""""
Um quadrado perfeito ou número quadrado perfeito é um número natural que se radicado, possui como resultado outro número natural.

Ou seja, são resultados da operação de um número multiplicado por ele mesmo.
A fórmula do quadrado perfeito é representada por: n × n = a ou n2 = a. Desse modo, n é um número natural e a é um número quadrado perfeito.
"""
from math import sqrt
def isQuadradoPErfeito (valor):
    quadrado = sqrt(valor)
    if (quadrado* quadrado ) == valor:
        return True
    return False

numero = int(input("Entre com o 1 numero  :-> "))
print(isQuadradoPErfeito(numero))

