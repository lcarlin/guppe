from random import randint

# arquivoSaida   = input(f'Entre com o nome de O Arquivo de Saida  :-> ')
# anoAtual       = int(input(f'Entre com o ano atual :-> '))

arquivoEntrada = 'DatasENomes3.txt'
arquivoSaida = arquivoEntrada + '.out'

totalElementos = 10
elementoMaximo = 1000

vetorGrande = [randint(1, elementoMaximo) for _ in range(totalElementos)]
print(vetorGrande)

try:
    with open(arquivoSaida, 'w') as saida:
        for atual in vetorGrande:
            # saida.write(str(atual).zfill(4) + " -> " + "{0:b}".format(atual).zfill(20) + '\n')
            saida.write(str(atual).zfill(4) + " -> " + ("{0:b}".format(atual)).rjust(12, ' ') + '\n')
except FileNotFoundError:
    print('Arquivo não achado')
