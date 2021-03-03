vetor1 = []
vetor2 = []
vetor3 = []

for n in range(1, 11):
    n1 = int(input(f'Informe o valor {n} do primeiro vetor: '))
    vetor1.append(n1)

    # posição par do vetor 3
    vetor3.append(n1)

    n2 = int(input(f'Informe o valor {n} do primeiro vetor: '))
    vetor2.append(n2)

    # Posição ímpar do vetor 3
    vetor3.append(n2)

print(vetor3)