import math

num1 = int(input("Digite o um Numero :-> "))
if num1 >= 0:
    print(f"O numero {num1} é positvo e eis a sua Raiz Quadrada:-> " + str(math.sqrt(num1)) +
          " E eis ele elevado ao quadrado :-> " + str(num1 ** 2))
else:
    print(f"O numero {num1}  tá negativo")
