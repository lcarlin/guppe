# -*- coding: cp1252 -*-
from collections import Counter
import string
arquivoEntrada = input(f'Entre com o nome de O Arquivo de entrada:-> ')
dicionario = dict()
try:
    with open(arquivoEntrada, 'r') as arquivo:
        linhas = arquivo.readlines()
        totalLinhas = len(linhas)
        arquivo.seek(0)
        linhas = arquivo.read()
        totalPalavras = len(linhas.split())
        totalLetras = len(list(linhas))
        arquivo.seek(0)
        caracter = str(arquivo.read())

        print(f' E vamos nós: Arquivo         :-> {arquivoEntrada}')
        print(f' Total de Total de caracteres :-> {totalLetras}')
        print(f' Total de Linhas Absolutas    :-> {totalLinhas}')
        print(f' Total de Palavras            :-> {totalPalavras}')
        [dicionario.update({letra: caracter.lower().count(letra)}) for letra in caracter.lower() if
         letra in string.ascii_letters]
        for key, value in sorted(dicionario.items()):
            print(f'{key} - {value}')

except FileNotFoundError:
    print('Arquivo não achado')
