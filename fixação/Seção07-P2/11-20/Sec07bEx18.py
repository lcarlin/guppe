import random

matrizInicial = []
linhaAtual = []
linhas = 3
colunas = 3
matrizSoma = [0,0,0]
print("=================================================")
for i in range(linhas):
    for j in range(colunas):
        # valor = int(input(f'Entre com elemento [{i}][{j}] :=-> '))
        valor = random.randint(-1000,1000)
        print(f'Entre com elemento [{i}][{j}] :=-> {valor}')
        linhaAtual.append(valor)
        matrizSoma[j] += valor
    matrizInicial.append(linhaAtual)
    linhaAtual = []

print("=================================================")
print("Matriz Gerada")
for linha in matrizInicial:
    print(linha)

print("=================================================")
print('SOmas Geradas das colunas')
print(matrizSoma)
