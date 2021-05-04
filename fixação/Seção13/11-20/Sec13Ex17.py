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
        aZerar = int(matrizACriar[2])
        for j in range(0, int(numLinhas)):
            linhaTemp = []
            for k in range(0, numColunas):
                linhaTemp.append(1)

            matrizFinal.append(linhaTemp)

        print(matrizFinal)
        # fase 02 - AGora temos que zerar as posições
        for i in range(0, aZerar):
            linha = int(posicoesAZerar[i][0])
            coluna = int(posicoesAZerar[i][1])
            print(linha, coluna)
            matrizFinal[linha][coluna] = 0

        # Fase 03 - Gravar linha-a-linha no arquivo de saida
        for k in range(0, len(matrizFinal)):
            estringue = ' '
            for l in range(0, len(matrizFinal[k])):
                estringue += str(matrizFinal[k][l]) + ' '

            saida.write(estringue + ' \n')

except FileNotFoundError:
    print('Arquivo não achado')
