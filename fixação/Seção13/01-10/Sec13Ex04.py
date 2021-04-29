nomeArquivo = input(f'Entre com o nome de O Arquivo :-> ')

try:
    with open (nomeArquivo, 'r') as arquivo:
        totalVogais = 0
        totalLetras = 0
        totalConsoantes = 0
        linhas = arquivo.readlines()
        for linhaAtual in linhas :
            linhaTemp = linhaAtual.replace(' ','').upper()
            # linhaTemp = linhaAtual.upper()
            totalLetras += len(linhaTemp)
            totalVogais += linhaTemp.count('A')
            totalVogais += linhaTemp.count('E')
            totalVogais += linhaTemp.count('I')
            totalVogais += linhaTemp.count('O')
            totalVogais += linhaTemp.count('U')

        totalConsoantes = totalLetras - totalVogais
        print(f'E o total de Vogais do arquivo {nomeArquivo} é de {totalVogais}')
        print(f'E o total de consoantes é de {totalConsoantes}')
        print(f'E o total geral de letras é de {totalLetras}')

except FileNotFoundError:
    print('Arquivo não achado')
