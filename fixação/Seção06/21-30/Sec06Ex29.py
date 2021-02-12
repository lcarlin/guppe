contador = 1
valor1 = 0
while valor1 <= 0: valor1 = int(input("Entre com o 1 numero  :-> "))
soma = 0
while contador <= valor1:
    fatorial = 1
    fatorador = contador * 2
    for n in range(1, (fatorador) + 1):
        fatorial *= n

    resulto = (contador / fatorial)
    soma += resulto
    print(f"Adicionando {contador} / {fatorador}! ( {resulto:.4f})  à soma ")
    contador += 1

print("=======================================================")
print(f"E a soma fatoriais  de {valor1} é {soma:.4f}")
