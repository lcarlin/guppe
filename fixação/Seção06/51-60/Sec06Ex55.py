def e_primo(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


qtd = int(input('Informe a quantidade de números primos para somar: '))
contador = 0
soma = 0
referencia = 2
while contador < qtd:
    if e_primo(referencia):
        soma += referencia
        contador += 1
        print(f'Primo? {referencia}')
    referencia += 1

print(f'A soma dos {qtd} primeiros primos é {soma}')