# -*- coding: cp1252 -*-
arquivoUm    = input(f'Entre com o nome do arquivo de cidades:-> ')
arquivoSaida = input(f'Entre com o nome do Arquivo de Saida  :-> ')

dictCidadesFull = {}

try:
    with open(arquivoUm, 'r') as entradaUm, open(arquivoSaida, 'w') as saida:
        linhasUm = entradaUm.readlines()

        for linhas in linhasUm :
            regCidade = linhas.split('|')
            dictCidadesFull[regCidade[0]] = int(regCidade[1])

        maiorCidade = max(dictCidadesFull, key=dictCidadesFull.get)

        saida.write(f'{maiorCidade}:{dictCidadesFull[maiorCidade]} \n')

except FileNotFoundError:
    print('Arquivo não achado')