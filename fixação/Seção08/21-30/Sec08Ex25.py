def somaSerie(valor):
    soma = 0
    for i in range(valor):
        soma += ((i**2)+1)/(i+3)
    return soma

a = int(input("Digite o 1º Numero :-> "))
result = somaSerie(a)
print(result)