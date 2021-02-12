contador = 1
valor1 = 0
while valor1 <= 0: valor1 = int(input("Entre com o 1 numero  :-> "))
soma = 1
while contador <= valor1:
    fatorial = 1
    print (f"Calculandoo fatorial de {contador} ")
    for n in range(1, contador + 1):
        fatorial *= n

    print (f"Adicionando {1/fatorial} à soma ")
    soma += (1 / fatorial)
    contador += 1

print(f"E a soma fatoriais  de {valor1} é {soma:.4f}")
