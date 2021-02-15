def e_primo(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True



final = inicio = soma = 0
while inicio <= 0: inicio = int(input("Entre com o 1 numero  :-> "))
while final <= inicio: final = int(input("Entre com o 2 numero  :-> "))
counter = 0

while inicio <= final:
    if e_primo(inicio):
        counter += 1
        soma += inicio
        print(f'Primo? {inicio}')

    inicio += 1

print(f'A quantidade de primos é de {counter} ')
print(f'A soma dos {counter} primos no intervalo é {soma}')