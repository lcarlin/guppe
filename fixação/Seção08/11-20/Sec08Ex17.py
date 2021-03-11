def somaIntervalos ( num1, num2 ):
    soma = 0
    if num1 > num2:
        menor = num2
        maior = num1
    else:
        menor = num1
        maior = num2

    for i in range(menor, maior+1):
        print(i)
        soma += i

    return soma


valor1 = int(input("Digite o 1º Numero :-> "))
valor2 = int(input("Digite o 2º Numero :-> "))
print(f'E a soma dos valores no intervalo é de {somaIntervalos(valor1, valor2)}')
