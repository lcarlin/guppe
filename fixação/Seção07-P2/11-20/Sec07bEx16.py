import random

matrizAlunoResposta = []
vetorGabarito = []
vetorResultado = []
linhaAtual = []
linhas = 10
colunas = 3
notaCorte = 7
contaAprovado = 0

print("=================================================")
print("Preenchendo as notas ")
for i in range(colunas):
    print(f"Notas do aluno {i} ")
    for j in range(linhas):
        valor = chr(random.randint(97,101))
        print(f'Entre com a resposta do aluno [{i}][{j}] :=-> {valor}')
        linhaAtual.append(valor)

    matrizAlunoResposta.append(linhaAtual)
    linhaAtual = []

print("=================================================")
print("Preenchendo O Gabarito  ")
for i in range(linhas):
    valor = chr(random.randint(97,101))
    print(f"Entre com a resposta da {i} questão :=->  {valor}")
    vetorGabarito.append(valor)

print("=================================================")
print("Matriz de notas")
for linha in matrizAlunoResposta:
    print(linha)

print("=================================================")
print("Vetor de Gabarito ")
print(vetorGabarito)

print("=================================================")
print("Corrigido as provas e dando notas")
for i in range(colunas):
    print ("**********************")
    print(f"Corrigindo a prova do aluno {i}")
    nota = 0
    for j in range(linhas):
        print(f'Aluno-Nota {i} - {j}: {matrizAlunoResposta[i][j]} ')
        print(f'respostaCorreta: {vetorGabarito[j]}')
        if matrizAlunoResposta[i][j] == vetorGabarito[j]:
            nota += 1

    if nota >= notaCorte:
        msg = "Aprovado"
    else:
        msg = "Reprovado"

    aproveitamento = (nota/10)* 100
    vetorResultado.append([i,nota, msg, aproveitamento, matrizAlunoResposta[i] ])
    if msg == "Aprovado":
        contaAprovado += 1



print("=================================================")
print("E eis o resultado :")
for linha in vetorResultado:
    print(linha)

print("=================================================")
print("Percentual de aprovados ",(  contaAprovado/notaCorte ) * 100)