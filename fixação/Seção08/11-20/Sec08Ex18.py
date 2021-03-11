def expoManu (base, exponente ):
    result = 1
    for i in range(exponente ):
        result *= base

    return result


valor1 = int(input("Digite o numero :-> "))
valor2 = int(input("Digite a Base   :-> "))
valor3 = expoManu(valor1, valor2)
print(f'E o resultado da exponenciação é : {valor3}')