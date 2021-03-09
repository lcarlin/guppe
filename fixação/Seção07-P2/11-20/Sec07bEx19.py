matrizInicial = []
linhaAtual = []
linhas = 5
colunas = 4
maiorNota = 0
alunoMaiorNota = 0
mediaProvas = mediaTrabalhos = notaFinal = somaNotasFinais = 0

print("=================================================")
for i in range(linhas):
    matricula = int(input(f'Entre com a Matricula do aluno [{i}] :=-> '))
    mediaProvas = float(input(f'Entre com a média das provas :=-> '))
    mediaTrabalhos = float(input(f'Entre com a média dos Trabalhos :=-> '))
    notaFinal = (mediaProvas + mediaTrabalhos) / 2
    linhaAtual = [matricula, mediaProvas, mediaTrabalhos, notaFinal]
    matrizInicial.append(linhaAtual)
    somaNotasFinais += notaFinal

    if notaFinal > maiorNota:
        maiorNota = notaFinal
        alunoMaiorNota = matricula

print("=================================================")
print(f"O Aluno que teve a maior nota foi p {alunoMaiorNota} e a sua media foi {maiorNota}")
print(f"E a média das notas foi :-> {somaNotasFinais/5}")
