# 24 -
"""
Escreva uma função que gera um triângulo de altura e lados n e base 2*n-1. Por exemplo, a saída para n = 6 seria:
     *
    ***
   *****
  *******
 *********
***********
"""

a = int(input("Digite um valor n positivo: "))
'''
for i in range(1, n+1):
    tri = (' ' * (n - i)) + ('*' * (2 * i - 1))
    print(tri)
'''


# refatorando:
def triagulo(n=6):
    list(print(' ' * (n - i) + ('*' * (2 * i - 1))) for i in range(1, n + 1))


triagulo(a)