# -*- coding: utf-8 -*-

"""
Escrevendo em arquivos
OBSG: ao abrir um arquivo para leitura, não pdoemos realizar a escrita, da mesma forma, se abrirums um aruqivo para
ESCRITA não podemos lê-lo, somente gravar (????)_

https://docs.python.org/3/library/functions.html#open

PAra escrever dados em um arquivo, após abri-lo usa=-ser a função write, essa função recebe uma Estringue como parametro

Abrindo um arquivo para escrita com o modo W, se ele não existir, será criado, caso exista, será sobrescritp.
dessa forma todo o conteudo anterior será perdido

====================================================================================================================
#Exemplo de escrita Pythonica
with open('novo.txt', 'w') as arquivo1:
    arquivo1.write('È muito facil escrever dados em arquivos \n ')
    arquivo1.write(' Pode-ser colocar tantas linhas quanto nmecessároi\n ')
    arquivo1.write(' \n ')
    arquivo1.write('E essa é a ultima linhas \n ')
    arquivo1.write(' \n ')


====================================================================================================================
# Forma tradicionao não pythonica de trabalhar com arquivos
arquivo = open('novo.txt','w')
arquivo.write('Talkey\n')
arquivo.write('forte abraço\n')
arquivo.close()

====================================================================================================================
with open('geek.txt','w') as arquivo:
    arquivo.write('Geek ' * 1000 )
====================================================================================================================

"""

with open('frutas.txt','w') as arquivo:
    while True:
        fruta = input('Informa uma Fruta ou digite Sair :-> ')
        if fruta != 'sair':
            arquivo.write(fruta)
            arquivo.write('\n')
        else:
            break