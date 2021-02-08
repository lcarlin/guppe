import math

num1 = int(input("Digite o um Numero :-> "))
if num1 >= 0:
    print(f"O numero {num1} é positvo e eis a sua Raiz Quadrada:-> " + str(math.sqrt(num1)))
else:
    print(f"O numero {num1}  tá negativo e eis o seu Quadrado " + str(num1 ** 2))
