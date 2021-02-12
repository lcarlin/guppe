"""
44 - Leia um número positivo do usuário, então, calcule e imprima a sequência Fibonacci até o primeiro número superior
     ao número lido.

     Exemplo: se o usuário informou o número 30, a sequência a ser impressa será: 0 1 1 2 3 5 8 13 21 34
"""

soma = 0
num_atual = 0
num_anterior = 1
sequencia = [0, 1]

numero = int(input('Digite um número para cálculo da sequência de Fibonacci: '))

while numero < 0:
    print('Você deve digitar um número positivo!')
    numero = int(input('Digite um número para cálculo da sequência de Fibonacci: '))
while True:
    soma = num_atual + num_anterior
    num_anterior = max(sequencia)
    sequencia.append(soma)
    if max(sequencia) > numero:
        break
    else:
        num_atual = soma
print(sequencia)

print("=================================================")
print("Final de O programas")
