import random

matrizFinal = []
linhaAtual = []
linhas = 4
colunas = 4
maior = 0
posXmaior = 0
posYmaior = 0
print("**********************")
for i in range(linhas):
    for j in range(colunas):
        # valor = int(input(f'Entre com elemento [{i}][{j}] :=-> '))

        valor = random.randint(0,1000)
        print(f'Entre com elemento [{i}][{j}] :=-> {valor}')
        linhaAtual.append(valor)
        if valor > maior:
            maior = valor
            # posXmaior = i
            # posYmaior = j
            # print(f'Maior: {maior} ; I: {posXmaior}; J:{posYmaior}')

    matrizFinal.append(linhaAtual)
    linhaAtual = []
    # linhaAtual.clear() o clear nesse caso provoca erro, acho que ele "mata" a linha

for k in matrizFinal:
    if maior in k:
        posYmaior = k.index(maior)
        break
    posXmaior += 1

print("=================================================")
for linha in matrizFinal :
    print(linha)

print("=================================================")
print(f'E o mair numero é :-> {maior}')
print(f'E a posicao [X,Y] do Maior é [{posXmaior},{posYmaior}]')