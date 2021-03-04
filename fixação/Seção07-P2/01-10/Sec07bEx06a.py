import random

matrizUm = []
matrizDois = []
matrizTres = []
linhaAtualUm = []
linhaAtualDois = []
linhaAtualTres = []
linhas = 4
colunas = 4

print("=================================================")
print(f'Preenche todos os valores para a matriz A e Matriz B [{linhas},{colunas}]')
for i in range(linhas):
    for j in range(colunas):
        # valor = int(input(f'Entre com elemento [{i}][{j}] :=-> '))
        valorUm = random.randint(0,1000)
        print(f'Entre com elemento [{i}][{j}] para a Matriz "A" :=-> {valorUm}')
        linhaAtualUm.append(valorUm)

        valorDois = random.randint(0,1000)
        print(f'Entre com elemento [{i}][{j}] para a Matriz "B" :=-> {valorDois}')
        linhaAtualDois.append(valorDois)

        if valorUm > valorDois:
            maior = valorUm
        else:
            maior = valorDois

        linhaAtualTres.append(maior)

    matrizUm.append(linhaAtualUm)
    matrizDois.append(linhaAtualDois)
    matrizTres.append(linhaAtualTres)
    linhaAtualUm = []
    linhaAtualDois = []
    linhaAtualTres = []

print("=================================================")
print('Matrix "A"' )
for linha in matrizUm :
    print(linha)
print("=================================================")
print('Matrix "B" ')
for linha in matrizDois :
    print(linha)
print("=================================================")
print('Matrix "C" ')
for linha in matrizTres :
    print(linha)
