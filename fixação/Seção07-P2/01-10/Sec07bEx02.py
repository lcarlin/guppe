matrizFinal = []
linhaAtual = []
linhas = 5
colunas = 5
padrao = 0
print("**********************")
for i in range(linhas):
    for j in range(colunas):
        if i == j:
            valor = 1

        linhaAtual.append(valor)
        valor = 0

    matrizFinal.append(linhaAtual)
    linhaAtual = []
    # linhaAtual.clear() o clear nesse caso provoca erro, acho que ele "mata" a linha

print("=================================================")
# pegadinha do malanro pra imprimir a matriz
for row in matrizFinal:
    print(' '.join([str(elem) for elem in row]))