totalNumeros = 15
matrizFinal = []
linhaAtual = []
linhas = 4
colunas = 4
print("**********************")
for i in range(linhas):
    for j in range(colunas):
        valor = i * j
        print(f'Entre com elemento [{i}][{j}] :=-> {valor}')
        linhaAtual.append(valor)

    matrizFinal.append(linhaAtual)
    linhaAtual = []

print("**********************")
print(matrizFinal)

print("=================================================")
# pegadinha do malanro pra imprimir a matriz
for row in matrizFinal:
    print(' '.join([str(elem) for elem in row]))

print("=================================================")
