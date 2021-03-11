from math import sqrt
def hipotenusa (catetoA, catetoB):
    return sqrt((catetoA**2) + (catetoB**2))

valor1 = int(input("Entre com o cateto A :-> "))
valor2 = int(input("Entre com o Cateto B :-> "))
valorHip = hipotenusa(valor1, valor2)
print(f'E a Hipoteniusa é :-> {valorHip}')