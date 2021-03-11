def fatorial (fatorador ):
    fatorial = 1
    for n in range(1, (fatorador) + 1):
        fatorial *= n

    return fatorial

valor1 = 0
while valor1 <= 0: valor1 = int(input("Entre com o 1 numero  :-> "))
result = fatorial(valor1)
print(f'E o fatorial é :-> {result}')

print("=======================================================")