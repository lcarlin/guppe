nomeArquivo = input(f'Entre com o nome de O Arquivo :-> ')
caracterAContar = input(f'Entre com o caracter pra contrar :-> ')
try:
    with open (nomeArquivo, 'r') as arquivo:
        totalLetras = 0
        linhas = arquivo.read().upper()
        totalLetras = linhas.count(caracterAContar.upper())
        print(f'E o total de letras "{caracterAContar}" no arquivo {nomeArquivo} é de {totalLetras}')

except FileNotFoundError:
    print('Arquivo não achado')
