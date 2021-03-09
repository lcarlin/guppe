import random

matrizUm = []
matrizDois = []
matrizTres = []
linhaAtual = []
linhas = 3
colunas = 3
valor = 0
print("=================================================")
print("Matriz 01 ")
for i in range(linhas):
    for j in range(colunas):
        # valor = int(input(f'Entre com elemento [{i}][{j}] :=-> '))
        valor = random.randint(-1000,1000)
        print(f'Entre com elemento [{i}][{j}] :=-> {valor}')
        linhaAtual.append(valor)

    matrizUm.append(linhaAtual)
    linhaAtual = []

for linha in matrizUm:
    print(linha)
print("=================================================")
print("Matriz 02 ")
for i in range(linhas):
    for j in range(colunas):
        # valor = int(input(f'Entre com elemento [{i}][{j}] :=-> '))
        valor = random.randint(-1000,1000)
        print(f'Entre com elemento [{i}][{j}] :=-> {valor}')
        linhaAtual.append(valor)

    matrizDois.append(linhaAtual)
    linhaAtual = []

for linha in matrizDois:
    print(linha)
print("=================================================")
print("A multiplicação de matrizes é feita pela soma das multiplicações das linhas X colunas")
"""
Como multiplicar matrizes 
https://www.youtube.com/watch?v=PyVahsZQT-c&ab_channel=MatematicaGenial
Solucação em Python 
https://pt.stackoverflow.com/questions/384972/como-fa%C3%A7o-para-multiplicar-duas-matrizes-no-python
"""
print("Matriz 03 ")
for i in range(linhas):
    matrizTres.append([])
    for j in range(colunas):
        for k in range(linhas):
            # valor = int(input(f'Entre com elemento [{i}][{j}] :=-> '))
            valor += (matrizUm[i][i] * matrizDois[k][i])
        matrizTres[-1].append(valor)


print("=================================================")
for linha in matrizTres:
    print(linha)