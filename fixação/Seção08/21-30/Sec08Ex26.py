def somaIntervalo (valor):
    soma = 0
    for i in range(1, valor + 1 ):
        soma += i
    return soma

a = int(input("Digite o 1º Numero :-> "))
result = somaIntervalo(a)
print(result)