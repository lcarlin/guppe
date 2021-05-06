# -*- coding: cp1252 -*-
arquivoUm    = input(f'Entre com o nome do arquivo de cidades:-> ')
arquivoSaida = input(f'Entre com o nome do Arquivo de Saida  :-> ')

dictCidadesFull = {}
try:
    with open(arquivoUm, 'r') as entradaUm, open(arquivoSaida, 'w') as saida:
        linhasUm = entradaUm.readlines()

        for linhas in linhasUm :
            dictCidadesFull[linhas[0:40].strip()] = int(linhas[41:])

        maiorCidade = max(dictCidadesFull, key=dictCidadesFull.get)

        saida.write(f'{maiorCidade}:{dictCidadesFull[maiorCidade]} \n')

except FileNotFoundError:
    print('Arquivo não achado')