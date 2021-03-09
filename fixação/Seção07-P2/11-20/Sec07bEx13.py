import random

matrizInicial = []
matrizFinal = []
linhaAtual = []
linhas = 4
colunas = 4

print("=================================================")
for i in range(linhas):
    for j in range(colunas):
        # valor = int(input(f'Entre com elemento [{i}][{j}] :=-> '))
        valor = random.randint(1,21)
        print(f'Entre com elemento [{i}][{j}] :=-> {valor}')
        linhaAtual.append(valor)
    matrizInicial.append(linhaAtual)
    linhaAtual = []

print("=================================================")
for i in range(linhas):
    for j in range(colunas):
        valor = matrizInicial[i][j]
        if i < j:   # j > i:
            valor = 0

        linhaAtual.append(valor)
    matrizFinal.append(linhaAtual)
    linhaAtual = []

print("=================================================")
for linha in matrizInicial:
    print(linha)
print("=================================================")
for linha in matrizFinal:
    print(linha)
print("=================================================")
print(f'E a soma dos valores Acima da Diagonal Secundária é :=-> {soma}')

