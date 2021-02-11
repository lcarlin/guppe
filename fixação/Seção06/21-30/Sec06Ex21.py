soma = 0
multiplica = 1
valor1 = int(input("Entre com o 1º numero  :-> "))
valor2 = valor1 - 1
while valor2 < valor1: valor2 = int(input("Entre com o 2º numero  :-> "))

while valor1 <= valor2:
    if valor1%2 ==0 :
        soma += valor1

    if valor1%3 == 0:
        multiplica *= valor1

    valor1 += 1


print (f"A soma dos Pares é {soma}")
print (f" A multiplicacao dos impares é {multiplica}")