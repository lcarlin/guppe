# -*- coding: cp1252 -*-
arquivoEntrada = 'comprasDoJao.txt'
try:
    with open(arquivoEntrada, 'r') as arquivo:
        linhasEntrada = arquivo.readlines()
        dictProdutos = {}
        somaTotal = 0
        for linha in linhasEntrada:
            produto = linha[0:39].strip()
            valor = float(linha[39:])

            dictProdutos[produto] = valor

        somaTotal = sum(dictProdutos.values())
        # maiorCidade = max(dictCidadesFull, key=dictCidadesFull.get)

        print(dictProdutos)
        print(f'E o valor total das compras é de :-> {somaTotal}')

except FileNotFoundError:
    print('Arquivo não achado')
