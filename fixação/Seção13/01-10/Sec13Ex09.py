# -*- coding: cp1252 -*-
arquivoUm    = input(f'Entre com o nome de O 1� Arquivo de entrada:-> ')
arquivoDois  = input(f'Entre com o nome de O 2� Arquivo de Saida  :-> ')
arquivoSaida = 'Saida_Sec13Ex09.out.txt'

try:
    with open(arquivoUm, 'r') as entradaUm:
        linhasUm = entradaUm.read()
except FileNotFoundError:
    print('Arquivo n�o achado')

try:
    with open(arquivoDois, 'r') as entradaDois:
        linhasDois = entradaDois.read()
except FileNotFoundError:
    print('Arquivo n�o achado')

try:
    with open(arquivoSaida, 'w') as saida:
        saida.writelines(linhasUm)
        saida.writelines(linhasDois)
except FileNotFoundError:
    print('Arquivo n�o achado')