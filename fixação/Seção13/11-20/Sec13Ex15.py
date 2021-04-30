# -*- coding: cp1252 -*-
from datetime import  date

#arquivoEntrada = input(f'Entre com o nome de O Arquivo de entrada:-> ')
#arquivoSaida   = input(f'Entre com o nome de O Arquivo de Saida  :-> ')
#anoAtual       = int(input(f'Entre com o ano atual :-> '))

anoAtual = date.today().year
arquivoEntrada = 'DatasENomes2.txt'
arquivoSaida = arquivoEntrada + '.out'

try:
    with open(arquivoEntrada, 'r') as arquivo, open(arquivoSaida, 'w') as saida:
        linhasEntrada = arquivo.readlines()
        for linhaAtual in linhasEntrada:
            nome = linhaAtual[0:39].strip()
            anoNasc = int(linhaAtual[39:])
            idade = anoAtual - anoNasc
            if idade < 18 :
                MSG = 'Menor de Idade'
            elif idade > 18:
                MSG = 'Maior de Idade'
            else:
                MSG = 'esta entrando na Marioridade'

            saida.write(f'{nome} tem {idade} e {MSG} \n')

except FileNotFoundError:
    print('Arquivo não achado')
