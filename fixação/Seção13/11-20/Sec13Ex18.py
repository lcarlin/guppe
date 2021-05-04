# -*- coding: cp1252 -*-
arquivoEntrada = 'comprasDoJao.txt'
try:
    with open(arquivoEntrada, 'r') as arquivo:
        linhasEntrada = arquivo.readlines()
        matrizProdutos = []
        somaTotal = 0
        for linha in linhasEntrada:
            produto = linha[0:39].strip()
            valor = int(linha[39:])
            somaTotal += valor
            matrizProdutos.append([produto, valor])

        print(f'E o valor total das compras é de :-> {somaTotal}')
        print(matrizProdutos)

except FileNotFoundError:
    print('Arquivo não achado')


