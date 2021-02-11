contador = 1
soma = 0
valor1 = int(input("Entre com o 1 numero  :-> "))
while   contador < valor1:
    if valor1%contador == 0:
        print(f" E o numero {valor1} é divisivel por {contador}")
        soma += contador

    contador += 1

print(f"E a soma dos divisores do numero {valor1} é :-> {soma}")