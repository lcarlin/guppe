# -*- coding: cp1252 -*-
arquivoUm    = input(f'Entre com o nome de O 1º Arquivo de entrada:-> ')
arquivoDois  = input(f'Entre com o nome de O 2º Arquivo de Saida  :-> ')
arquivoSaida = 'Saida_Sec13Ex09.out.txt'

try:
    with open(arquivoUm, 'r') as entradaUm:
        linhasUm = entradaUm.read()
except FileNotFoundError:
    print('Arquivo não achado')

try:
    with open(arquivoDois, 'r') as entradaDois:
        linhasDois = entradaDois.read()
except FileNotFoundError:
    print('Arquivo não achado')

try:
    with open(arquivoSaida, 'w') as saida:
        saida.writelines(linhasUm)
        saida.writelines(linhasDois)
except FileNotFoundError:
    print('Arquivo não achado')