"""
Enunciado:
        Faça um programa para gerar automaticamente numeros entre 0 e 99 de uma cartela de Bingo. Sabendo que cada
    cartela deverá conter 5 linhas de 5 numeros , gere eses dados de modo a não ter numeros repetidos dentro das
    cartelas. O programa deverá exibir na tela a cartela gerada.
"""
import random

matrizInicial = []
linhaAtual = []
linhas = 5
colunas = 5

print("=================================================")
for i in range(linhas):
    for j in range(colunas):
        while True:
            naoExiste = True
            valor = random.randint(0, 99)
            print(f'Entre com elemento [{i}][{j}] :=-> {valor}')
            for k in range(0, i):
                if valor in matrizInicial[k]:
                    naoExiste = False

            if naoExiste:
                break
            else:
                continue

        linhaAtual.append(valor)

    matrizInicial.append(linhaAtual)
    linhaAtual = []

print("=================================================")
print("Imprime a 'Cartela' ")
for linha in matrizInicial:
    print(linha)

print("=================================================")
print("Aqui, para validação, transformei a matriz em um vetor \n e imprimi para so ter o visual ")
vetorUm = []
for i in range(linhas):
    for j in range(colunas):
        vetorUm.append(matrizInicial[i][j])

vetorUm.sort()
print(vetorUm)