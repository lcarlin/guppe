
matrizFinal = []
linhaAtual = []
linhas = 10
colunas = 10
valor = 0
for i in range(linhas):
    for j in range(colunas):
        if i < j :
            valor = (2*i) + (7*j) - 2
        elif i == j:
            valor = (3 * (i**2)) - j
        else:
            valor = (4*(i**3)) - (5*(j**2)) + 1

        linhaAtual.append(valor)

    matrizFinal.append(linhaAtual)
    linhaAtual = []

print("=================================================")
print('Matrix Gerada ')
for linha in matrizFinal :
    print(linha)
