# -*- coding: cp1252 -*-
from collections import Counter

arquivoEntrada = input(f'Entre com o nome de O Arquivo de entrada:-> ')
palavraEspecial = input(f'Entre com a palavra a ser pesquisada    :-> ')
try:
    with open(arquivoEntrada, 'r') as arquivo:
        resultado = Counter(arquivo.read().split())
        total = resultado.get(palavraEspecial)
        print(f'E a palavra especal "{palavraEspecial}" apareceu {total} vezes no arquivo {arquivoEntrada}')

except FileNotFoundError:
    print('Arquivo não achado')

