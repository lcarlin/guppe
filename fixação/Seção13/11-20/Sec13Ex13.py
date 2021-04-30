# -*- coding: cp1252 -*-
import os

arquivoEntrada = input(f'Entre com o nome de O Arquivo de entrada:-> ')
modoAbertua = 'a'
if not os.path.isfile(arquivoEntrada):
    modoAbertua = 'w'

try:
    with open(arquivoEntrada, modoAbertua) as arquivo:
        telefone = '0'
        while True:
            print ('--------------------------------------------------')
            nome = input(f'Entre com o nome  do Cara :-> ')
            telefone = input(f'Entre com o telefone do Cara :-> ')
            if telefone == '0':
                break

            arquivo.write(nome + ";" + telefone + "\n")
except FileNotFoundError:
    print('Arquivo não achado')
