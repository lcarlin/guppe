valor1 = maior = 0
menor = 999999
while True:
    valor1 = int(input("Entre com o 1 numero  ( -1 pra sair ) :-> "))
    if valor1 == -1:
        break
    if valor1 > maior:
        maior = valor1

    if valor1 < menor:
        menor = valor1

print(f"E o maior valor é :-> {maior}")
print(f"E o menor valor é :-> {menor}")
