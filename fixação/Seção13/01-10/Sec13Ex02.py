nomeArquivo = input(f'Entre com o nome de O Arquivo :-> ')

try:
    with open (nomeArquivo, 'r') as arquivo:
        linhas = arquivo.readlines()
        totalLinhas = len(linhas)
        print(f'E o total de linhas do arquivo {nomeArquivo} é de {totalLinhas}')

except FileNotFoundError:
    print('Arquivo não achado')
