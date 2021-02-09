import math

valorA = int(input("entre com Valor A :-> "))
valorB = int(input("entre com Valor B :-> "))
valorC = int(input("entre com Valor C :-> "))

delta = (valorB ** 2) - (4 * valorA * valorB)

if delta < 0:
    print("Não existe raiz para os valores selecionados ")
else:

    if delta == 0:
        print("Existe apenas uma unica raiz ")
        raiz1 = (-1 * valorB) / (2 * valorA)
        print(raiz1)
    else:
        print("existem duas raizes  ")
        raiz1 = ((-1 * valorB) + math.sqrt(delta)) / (2 * valorA)
        raiz2 = ((-1 * valorB) - math.sqrt(delta)) / (2 * valorA)
        print(raiz1)
        print(raiz2)
