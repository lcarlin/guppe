def triangLateral(valor):
    for i in range(valor):
        print("*"*i)
    for j in range(valor,0, -1):
        print("*"*j)

valor1 = int(input("Digite o 1º Numero :-> "))
triangLateral(valor1)
