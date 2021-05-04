# -*- coding: cp1252 -*-
arquivoSaida = 'NotasAlunosConcatenadas.txt'
vetorAlunos =['João',
              'Pedro',
              'Maria',
              'Paulo',
              'Lucas',
              'Cassia',
              'Aurora',
              'Alessandra',
              'Paola',
              'Stella' ]
vetorNotasAlunos = [9.0,
                    8.6,
                    4.5,
                    7.9,
                    3.5,
                    8.9,
                    4.3,
                    6.3,
                    5.9,
                    6.6]
try:
    with  open(arquivoSaida, 'w') as saida:
        totalIteracoes = min(len(vetorAlunos), len(vetorNotasAlunos))
        estringue = ''
        for i in range(0,totalIteracoes):
            estringue = vetorAlunos[i][0:40].ljust(40,' ') + str(vetorNotasAlunos[i] )
            saida.write(f'{estringue}\n')

except FileNotFoundError:
    print('Arquivo não achado')