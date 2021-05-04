# -*- coding: cp1252 -*-
arquivoSaida = 'NotasAlunosConcatenadas.bin'
totalAlunos = 0
while totalAlunos <= 0:
    totalAlunos = int(input(f'Digite a quantidade de alunos a ser processadas :-> '))

vetorAlunos = []
for j in range(0, totalAlunos):
    print('----------------')
    nome = input(f'Entre com o nome do {j + 1}º Aluno :-> ')
    nota = float(input(f'Entre com a nnota do {j + 1}º Aluno :-> '))
    vetorAlunos.append([nome, nota])

try:
    with  open(arquivoSaida, 'wb') as saida:
        totalIteracoes = len(vetorAlunos)
        estringue = ''
        print('Gerando o arquivo Binário ')
        for i in range(0, totalIteracoes):
            estringue = vetorAlunos[i][0][0:39].ljust(40, ' ') + str(vetorAlunos[i][1]) + '\n'
            print(estringue)
            saida.write(estringue.encode('utf-8'))

    with  open(arquivoSaida, 'rb') as entrada:
        lista = []
        for dado in entrada:
            linha = dado.decode('utf-8')
            aluno = linha[0:39].strip()
            nota = float(linha[39:].strip().replace('\n',''))
            elemento = {'nome': aluno , 'nota': nota }
            lista.append(elemento)

        dados = sorted(lista, key=lambda a: a['nota'], reverse=True)
        print(f"O(a) aluno(a) {dados[0]['nome']} tem a maior nota {dados[0]['nota']}")


except FileNotFoundError:
    print('Arquivo não achado')
