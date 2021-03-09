"""
"""
import random

matrizNotasAlunos = []
matrizNotasTransposta = []
linhaAtual = []
alunosLInhas = 10
provasColunas = 3

print("=================================================")
print("Criando a matriz de Notas Aleatorias (0..10")
for i in range(alunosLInhas):
    for j in range(provasColunas):
        valorNotaAluno = random.randint(0, 10)
        print(f'Aluno :[{i}] ; Prova : [{j}] :=-> {valorNotaAluno}')
        linhaAtual.append(valorNotaAluno)

    matrizNotasAlunos.append(linhaAtual)
    linhaAtual = []

print("=================================================")
print("Imprime a cartela de notas" )
for linha in matrizNotasAlunos:
    print(linha)

print("=================================================")
print("Determinando quem teve as piores notas P1, P2, P3 ")
for k in range(provasColunas):
    for l in range(alunosLInhas):
        linhaAtual.append(matrizNotasAlunos[l][k])
    matrizNotasTransposta.append(linhaAtual)
    linhaAtual = []

#Detertmninar qual é a menor nota
notaMinP1 = min(matrizNotasTransposta[0])
notaMinP2 = min(matrizNotasTransposta[1])
notaMinP3 = min(matrizNotasTransposta[2])
qtdAlunP1 = matrizNotasTransposta[0].count(notaMinP1)
qtdAlunP2 = matrizNotasTransposta[0].count(notaMinP2)
qtdAlunP3 = matrizNotasTransposta[0].count(notaMinP3)

print("=================================================")
for linha in matrizNotasTransposta:
    print(linha)

print(f'A pior nota na Prova P1 foi {notaMinP1} e q quandidade de alunos com essa nota é {qtdAlunP1}')
print(f'A pior nota na Prova P1 foi {notaMinP2} e q quandidade de alunos com essa nota é {qtdAlunP2}')
print(f'A pior nota na Prova P1 foi {notaMinP3} e q quandidade de alunos com essa nota é {qtdAlunP3}')

print("=================================================")
print("FInal")

