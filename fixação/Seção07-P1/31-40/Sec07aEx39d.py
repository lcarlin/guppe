n = 0
vet = []

while n <= 0:
    n = int(input("Qual o número de linhas para imprimir o 'Triangulo de Pascal'? "))


def imprime(*args):
    for i in range(len(args)):
        print(args[i], end=' ')
    print()


for i in range(n):
    if i == 0:
        vet.append(1)
        imprime(*vet)
        continue
    if i == 1:
        vet.append(1)
        imprime(*vet)
        continue
    vetaux = vet.copy()
    vet.clear()
    vet.append(1)
    for j in range(1, i):
        vet.append(vetaux[j] + vetaux[j - 1])
    vet.append(1)
    imprime(*vet)

print('...')