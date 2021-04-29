nomeArquivo = input(f'Entre com o nome de O Arquivo :-> ')

try:
    with open (nomeArquivo, 'r') as arquivo:
        totalVogais = 0

        linhas = arquivo.readlines()
        for linhaAtual in linhas :
            linhaTemp = linhaAtual.upper()
            totalVogais += linhaTemp.count('A')
            totalVogais += linhaTemp.count('E')
            totalVogais += linhaTemp.count('I')
            totalVogais += linhaTemp.count('O')
            totalVogais += linhaTemp.count('U')

        print(f'E o total de Vogais do arquivo {nomeArquivo} é de {totalVogais}')

except FileNotFoundError:
    print('Arquivo não achado')
