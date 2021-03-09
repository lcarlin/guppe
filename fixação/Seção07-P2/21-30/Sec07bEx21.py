import random

matrizUm = []
matrizDois = []
matrizTres = []
linhaAtual = []
linhas = 2
colunas = 2
escolha = ""
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

print("=================================================")
print("Escolha uma das opções abaixo: ")
print("a - Somar as duas matrizes;")
print("b - Subtrair a 1º da 2ª Matriz;")
print("c - Adicionar uma COnstanter à 2 matrizes;")
print("d - Imprimir as Matrizes;")
escolha = input('faça uma escolha entre a e d:=-> ')
if escolha.upper() == 'A' :
    for i in range(linhas):
        for j in range(colunas):
            valor = matrizUm[i][j] + matrizDois[i][j]
            linhaAtual.append(valor)

        matrizTres.append(linhaAtual)
        linhaAtual = []

    print("=================================================")
    print("Matriz Gerada pela Soma das 2 matrizes ")
    for linha in matrizTres:
        print(linha)
elif escolha.upper() == 'B' :
    for i in range(linhas):
        for j in range(colunas):
            valor = matrizUm[i][j] + matrizDois[i][j]
            linhaAtual.append(valor)

        matrizTres.append(linhaAtual)
        linhaAtual = []

    print("=================================================")
    print("Matriz Gerada pela SUBTRACAO  2 matrizes ")
    for linha in matrizTres:
        print(linha)

elif escolha.upper() == 'C' :
    valor = int(input(f'Entre com uma comnstante pra agregar as 2 matrizes :=-> '))
    for i in range(linhas):
        for j in range(colunas):
            matrizUm[i][j] += valor
            matrizDois[i][j] += valor

    print("=================================================")
    for linha in matrizUm:
        print(linha)
    print("=================================================")
    for linha in matrizDois:
        print(linha)

elif escolha.upper() == 'D' :
    print("=================================================")
    for linha in matrizUm:
        print(linha)
    print("=================================================")
    for linha in matrizDois:
        print(linha)
else:
    print("Opcao Inválida")