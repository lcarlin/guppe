arquivoEntrada = 'EnterTheMatrix.txt'
arquivoSaida = arquivoEntrada + '.out'
"""
linha 1 dimensões da matriz e qtd de posições a serem anuladas
linha 2..n posições a serem anunladas
"""
try:
    with open(arquivoEntrada, 'r') as arquivo, open(arquivoSaida, 'w') as saida:
        linhasEntrada = arquivo.readlines()
        matrizACriar = []
        posicoesAZerar = []
        matrizFinal = []

        counter = 0
        # Fase 01 - ler o arquivo e as posições
        for linha in linhasEntrada:
            if counter == 0:
                matrizACriar = linha.split()
            else:
                posicoesAZerar.append(linha.split())
            counter += 1
        numLinhas = int(matrizACriar[0])
        numColunas = int(matrizACriar[1])

        for j in range(0, int(numLinhas)):
            linhaTemp = []
            for k in range(0, numColunas):
                linhaTemp.append(1)

            matrizFinal.append(linhaTemp)

        # com isso, temos a garantia de não estourar os limites da matriz
        tamanhoMatrizFinal = len(matrizFinal)
        aZerar = min(int(matrizACriar[2]),len(posicoesAZerar) )
        for i in range(0, aZerar):
            linha = int(posicoesAZerar[i][0])
            coluna = int(posicoesAZerar[i][1])
            if linha <= tamanhoMatrizFinal :
                tamanhoColunaAZerar = len(matrizFinal[linha])
                if coluna <= tamanhoColunaAZerar :
                   print(linha, coluna)
                   matrizFinal[linha][coluna] = 0
                else:
                    print(f'Valores da linha {i + 1} arquivo de entrada fora do ALcance ')
                    print(f' LInha :-> {linha} / Coluna :->{coluna}')
            else:
                print(f'Valores da linha {i+1} arquivo de entrada fora do ALcance ')
                print(f' LInha :-> {linha} / Coluna :->{coluna}')

        # Fase 03 - Gravar linha-a-linha no arquivo de saida
        for k in range(0, len(matrizFinal)):
            estringue = ' '
            for l in range(0, len(matrizFinal[k])):
                estringue += str(matrizFinal[k][l]) + ' '

            saida.write(estringue + ' \n')

except FileNotFoundError:
    print('Arquivo não achado')
