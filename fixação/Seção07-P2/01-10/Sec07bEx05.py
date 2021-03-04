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

    matrizFinal.append(linhaAtual)
    linhaAtual = []

print("=================================================")
for linha in matrizFinal:
    print(linha)

maior = int(input(f'Entre com um numero pra eu localizar nessa bagaça ai :-> '))
encontrou = False
for k in matrizFinal:
    if maior in k:
        posYmaior = k.index(maior)
        encontrou = True
        break
    posXmaior += 1

if encontrou:
    print(f'E a posicao [X,Y] do Maior é [{posXmaior},{posYmaior}]')
else:
    print('Nao encontrei ')
print("=================================================")

