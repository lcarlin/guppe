arquivo = open('arq.txt','w')
while True:
    letra = input('Digite um caractere ')
    if letra != '0':
        arquivo.write(letra)
        # arquivo.write('\n')
    else:
         break

arquivo.close()

arquivo = open('arq.txt','r')
retorno = arquivo.read()
print(retorno)
arquivo.close()