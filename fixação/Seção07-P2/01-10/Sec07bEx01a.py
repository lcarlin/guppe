matrizFinal = []
linhaAtual = []
linhas = 4
colunas = 4
contaMaio10 = 0
print("**********************")
for i in range(linhas):
    for j in range(colunas):
        valor = int(input(f'Entre com elemento [{i}][{j}] :=-> '))
        linhaAtual.append(valor)

    matrizFinal.append(linhaAtual)
    linhaAtual = []
    # linhaAtual.clear() o clear nesse caso provoca erro, acho que ele "mata" a linha
print("**********************")
print(matrizFinal)
print (matrizFinal[2][2])
print("=================================================")
# pegadinha do malanro pra imprimir a matriz
for row in matrizFinal:
    print(' '.join([str(elem) for elem in row]))


for i in range(linhas):
    for j in range(colunas):
        if matrizFinal[i][j] > 10 :
            contaMaio10 += 1

print("**********************")
print(f'Tota de numeros > 10 :-> {contaMaio10}')