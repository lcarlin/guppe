qtdNumeros = int(input("Entre com a qualtidade de numeros :-> "))
maior = 0
contador = 1
contaMAior = 1
atual = 0
while contador <= qtdNumeros:
    atual = int (input(f"Entre com o numero {contador} Atual :-> "))

    if atual > maior:
        contaMAior = 1
        maior = atual
    elif atual == maior:
        contaMAior += 1

    contador += 1

print(f"E o maior numero digitado foi {maior}")
print(f"E apareceu {contaMAior} Vezes  ")
