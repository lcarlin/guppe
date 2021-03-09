import random

matrizFinal = []
linhaAtual = []
linhas = 3
colunas = 3
soma = 0
print("=================================================")
for i in range(linhas):
    for j in range(colunas):
        # valor = int(input(f'Entre com elemento [{i}][{j}] :=-> '))
        valor = random.randint(0,1000)
        print(f'Entre com elemento [{i}][{j}] :=-> {valor}')
        linhaAtual.append(valor)
    matrizFinal.append(linhaAtual)
    linhaAtual = []

print("=================================================")
valorC = colunas - 1
for i in range(linhas):
    soma += matrizFinal[i][valorC]
    valorC -= 1

print("=================================================")
for linha in matrizFinal:
    print(linha)

print("=================================================")
print(f'E a soma dos valores Acima da Diagonal Secundária é :=-> {soma}')

