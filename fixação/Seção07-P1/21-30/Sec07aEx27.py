def e_primo(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


vetInicial = []
conjPrimos = []
totalNumeros = 10

# Faze 01 - ler os 10 numeros;
for n in range(totalNumeros):
    numero = 0
    while numero <= 0: numero = int(input(f"Entre com o numero {n + 1}  inteiro e maior que Zero  :-> "))
    vetInicial.append(numero)

# Fase 02 Determinar quais são primos, e as suas posições no vetor, criano num novo conjngo
for i in range(len(vetInicial)):
    if e_primo(vetInicial[i]):
        conjPrimos.append((i, vetInicial[i]))

print("=================================================")
print(conjPrimos)
