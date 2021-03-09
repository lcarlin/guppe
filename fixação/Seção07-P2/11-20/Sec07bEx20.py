import random

matrizInicial = []
matrizFinal = []
linhaAtual = []
linhas = 3
colunas = 6
somaColunasIMpares = somaGeral = contaGeral = mediaSegQuarCol = 0
print("=================================================")
for i in range(linhas):
    print("**********************")
    for j in range(colunas):
        # valor = int(input(f'Entre com elemento [{i}][{j}] :=-> '))
        valor = random.randint(-1000,1000)
        print(f'Entre com elemento [{i}][{j}] :=-> {valor}')
        linhaAtual.append(valor)
        if j%2 != 0 :
            somaColunasIMpares += valor
        if j == 1 or j == 3 :
            somaGeral += valor
            contaGeral += 1

    matrizInicial.append(linhaAtual)
    linhaAtual = []


mediaSegQuarCol = somaGeral / contaGeral

# Não sei o motivo pelo qual as linahs abaixo não funcionaram
#matrizFinal = matrizInicial.copy()
#for i in range(linhas):
#    matrizInicial[i][5] = matrizInicial[i][0] + matrizInicial[i][0]

# Ai tive que apelar pro metodo abaixo
for i in range(linhas):
    for j in range(colunas):
        linhaAtual.append(matrizInicial[i][j])

    matrizFinal.append(linhaAtual)
    linhaAtual = []
    matrizFinal[i][5] = matrizFinal[i][0] + matrizFinal[i][1]

# matrizInicial[0][0] = 9999

print("=================================================")
print(f"A soma de todos os elementos das colunas impares :=-> {somaColunasIMpares}")

print("=================================================")
print(f"Media Aritmédica 2ª e 4ª coluna :=-> {mediaSegQuarCol}")

print("=================================================")
print("Matriz Gerada")
for linha in matrizInicial:
    print(linha)

print("=================================================")
print("Matriz Substituida")
for dois in matrizFinal:
    print(dois)