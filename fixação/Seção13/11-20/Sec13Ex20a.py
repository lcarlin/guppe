# -*- coding: cp1252 -*-
arquivoSaida = 'NotasAlunosConcatenadas.txt'
totalAlunos = 0
while totalAlunos <= 0:
    totalAlunos = int(input(f'Digite a quantidade de alunos a ser processadas :-> '))

vetorAlunos = [ ]
vetorNotasAlunos = [ ]
for j in range(0, totalAlunos):
    print('----------------')
    vetorAlunos.append(input(f'Entre com o nome do {j+1}º Aluno :-> ' ))
    vetorNotasAlunos.append(float(input(f'Entre com a nnota do {j+1}º Aluno :-> ' )))

try:
    with  open(arquivoSaida, 'w') as saida:
        totalIteracoes = min(len(vetorAlunos), len(vetorNotasAlunos))
        estringue = ''
        for i in range(0,totalIteracoes):
            estringue = vetorAlunos[i][0:40].ljust(40,' ') + str(vetorNotasAlunos[i] )
            saida.write(f'{estringue}\n')

except FileNotFoundError:
    print('Arquivo não achado')