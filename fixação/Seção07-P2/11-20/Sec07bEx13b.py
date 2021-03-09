import random

matrizInicial = []
matrizFinal = []
linhaAtual = []
linhaNova = []
linhas = 4
colunas = 4

print("=================================================")
for i in range(linhas):
    for j in range(colunas):
        # valor = int(input(f'Entre com elemento [{i}][{j}] :=-> '))
        valor = random.randint(1,21)
        print(f'Entre com elemento [{i}][{j}] :=-> {valor}')
        linhaAtual.append(valor)
        if i < j:  # j > i:
            valor = 0
        linhaNova.append(valor)
    matrizInicial.append(linhaAtual)
    matrizFinal.append(linhaNova)
    linhaAtual = []
    linhaNova = []

print("=================================================")
for linha in matrizInicial:
    print(linha)
print("=================================================")
for linha in matrizFinal:
    print(linha)
print("=================================================")
print(f'E a soma dos valores Acima da Diagonal Secundária é :=-> {soma}')

