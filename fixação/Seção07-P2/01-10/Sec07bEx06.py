import random

matrizUm = []
matrizDois = []
matrizTres = []
linhaAtual = []
linhas = 4
colunas = 4

print("**********************")
print(f'Preenche todos os valores para a matriz A [{linhas},{colunas}]')
for i in range(linhas):
    for j in range(colunas):
        # valor = int(input(f'Entre com elemento [{i}][{j}] :=-> '))
        valor = random.randint(0,1000)
        print(f'Entre com elemento [{i}][{j}] para a Matriz "A" :=-> {valor}')
        linhaAtual.append(valor)

    matrizUm.append(linhaAtual)
    linhaAtual = []
    # linhaAtual.clear() o clear nesse caso provoca erro, acho que ele "mata" a linha

print("**********************")
print(f'Preenche todos os valores para a matriz B [{linhas},{colunas}]')
for i in range(linhas):
    for j in range(colunas):
        # valor = int(input(f'Entre com elemento [{i}][{j}] :=-> '))
        valor = random.randint(0,1000)
        print(f'Entre com elemento [{i}][{j}] para a Matriz "B" :=-> {valor}')
        linhaAtual.append(valor)

    matrizDois.append(linhaAtual)
    linhaAtual = []
    # linhaAtual.clear() o clear nesse caso provoca erro, acho que ele "mata" a linha

print("**********************")
print('Gerando a Matriz "C" com os maiores valores de cada matriz "A" e "B"' )
for i in range(linhas):
    for j in range(colunas):
        if matrizUm[i][j] > matrizDois[i][j]:
            maior = matrizUm[i][j]
        else:
            maior = matrizDois[i][j]
        linhaAtual.append(maior)

    matrizTres.append(linhaAtual)
    linhaAtual = []

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
