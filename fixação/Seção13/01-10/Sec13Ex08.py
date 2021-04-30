# -*- coding: cp1252 -*-
arquivoEntrada = input(f'Entre com o nome de O Arquivo de entrada:-> ')
arquivoSaida   = input(f'Entre com o nome de O Arquivo de Saida  :-> ')

try:
    with open(arquivoEntrada, 'r') as arquivo:
        linhas = arquivo.read()
        novo = linhas.upper()
        try:
            with open(arquivoSaida, 'w') as saida:
                saida.writelines(novo)
        except FileNotFoundError:
            print('Arquivo não achado')

except FileNotFoundError:
    print('Arquivo não achado')
