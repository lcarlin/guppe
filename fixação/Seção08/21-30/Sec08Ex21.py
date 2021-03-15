def quantidadePrimos(numero):
    contaPrimos = 0
    for i in range(numero+1):
        if e_primo(i):
            contaPrimos += 1
    return contaPrimos


def e_primo(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True



valor1 = int(input("Digite o 1º Numero :-> "))
totalPrimos = quantidadePrimos(valor1)

print(f'E a quantidade de primos abaixo de {valor1} é de :-> {totalPrimos}')