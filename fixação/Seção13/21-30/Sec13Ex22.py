# -*- coding: cp1252 -*-
arquivoEntrada = 'NotasDasCriancas.txt'
arquivoSaida = arquivoEntrada + '.out'

try:
    with open(arquivoEntrada, 'r') as arquivo, open(arquivoSaida, 'w') as saida:
        linhasEntrada = arquivo.readlines()
        dictNotas = {}
        for linha in linhasEntrada:
            nome = linha[0:39]
            notas = linha[39:].split()
            notas.sort()
            estringue = nome + ' '
            for i in range(0,len(notas)):
                estringue += str(notas[i])+ ' '

            saida.write(f'{estringue}\n')
            print(estringue)

except FileNotFoundError:
    print('Arquivo não achado')
