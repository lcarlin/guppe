# -*- coding: cp1252 -*-
arquivoEntrada = 'NotasDasCriancas.txt'

try:
    with open(arquivoEntrada, 'r') as arquivo:
        linhasEntrada = arquivo.readlines()
        dictNotas = {}
        for linha in linhasEntrada:
            registro = linha.replace('NOME','').replace('NOTA','').split(':')
            # vetorNotas.append([registro[1].strip(), float(registro[2])])
            dictNotas[registro[1].strip()] = float(registro[2])

        print(dictNotas)
        maiorNota = max(dictNotas, key=dictNotas.get)
        print(f'E o aluno que teve a maior nota é :-> {maiorNota} ; e a sua nota foi {dictNotas[maiorNota]}')

except FileNotFoundError:
    print('Arquivo não achado')
