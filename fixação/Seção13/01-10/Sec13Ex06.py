from collections import Counter

nomeArquivo = input(f'Entre com o nome de O Arquivo :-> ')

try:
    with open (nomeArquivo, 'r') as arquivo:
        linhas = arquivo.read().upper()
        listaGigante = list(linhas)
        dictTotais = Counter(listaGigante)
        print(dictTotais)

except FileNotFoundError:
    print('Arquivo não achado')
