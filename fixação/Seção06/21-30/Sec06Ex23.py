contador = 1
valor1 = int(input("Entre com o 1 numero  :-> "))
while   contador <= valor1:
    if valor1%contador == 0:
        print(f" E o numero {valor1} é divisivel por {contador}")

    contador += 1