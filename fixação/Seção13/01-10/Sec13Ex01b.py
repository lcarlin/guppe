
with open('arq.txt','w') as arquivo:
    while True:
        letra = input('Informa uma Fruta ou digite Sair :-> ')
        if letra != 'sair':
            arquivo.write(letra)
            arquivo.write('\n')
        else:
            break