import random

matrizInicial = []
matrizFinal = []
linhaAtual = []
linhas = 3
colunas = 3
print("=================================================")
for i in range(linhas):
    for j in range(colunas):
        # valor = int(input(f'Entre com elemento [{i}][{j}] :=-> '))
        valor = random.randint(0,1000)
        print(f'Entre com elemento [{i}][{j}] :=-> {valor}')
        linhaAtual.append(valor)
    matrizInicial.append(linhaAtual)
    linhaAtual = []

print("=================================================")
for i in range(linhas):
    for j in range(colunas):
        valor = matrizInicial[j][i]
        linhaAtual.append(valor)
    matrizFinal.append(linhaAtual)
    linhaAtual = []

print("=================================================")
print('Matriz Inicial ')
for linha in matrizInicial:
    print(linha)

print("=================================================")
print('Matriz TRansposta ')
for linha in matrizFinal:
    print(linha)

