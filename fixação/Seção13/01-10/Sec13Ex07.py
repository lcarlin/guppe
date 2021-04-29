# -*- coding: cp1252 -*-
nomeArquivo = input(f'Entre com o nome de O Arquivo :-> ')

try:
    with open(nomeArquivo, 'r') as arquivo:
        linhas = arquivo.read()
        novo = linhas.replace('a', '*').replace('A', '*').replace('a', '*').replace('E', '*').replace('e', '*').replace(
            'I', '*').replace('i', '*').replace('O', '*').replace('o', '*').replace('U', '*').replace('u', '*')

        try:
            saidaArquivo = nomeArquivo + '.novo.txt'
            with open(saidaArquivo, 'w') as saida:
                saida.writelines(novo)

        except FileNotFoundError:
            print('Arquivo não achado')

except FileNotFoundError:
    print('Arquivo não achado')
