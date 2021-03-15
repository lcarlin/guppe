'Ex27'
print('Este programa recebe o valor de um ângulo x, em graus, e retorna a śerie de Taylor, até o 5o termo, da função '
      'sin(x).')

def fatorial(n):
    prod = 1
    for k in list(range(1, n + 1)):
        prod *= k
    return prod

def taylor_sin(x):
    pi = 3.141593
    rad = x * pi / 180
    seno = 0
    for k in range(6):
        seno += (-1) ** k * rad ** (2 * k + 1) / fatorial(2 * k + 1)

    return seno


ang = float(input('Ângulo (graus): '))
print(round(taylor_sin(ang), 8))  # o valor 8 pode ser alterado a gosto do freguês