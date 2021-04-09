"""
Sistema de Arquivos - Manipulação

====================================================================================================================
import os
#Descobrir se um arquivo/diretorio existe ?
#Paths Relativos

print(os.path.exists('jaspion.txt'))
print(os.path.exists('frutas.txt'))
print(os.path.exists('Geek'))
print(os.path.exists('Geek\\University')) # path relativo

#Paths Absolutos
print((os.path.exists("C:\\Users\\luizc\\PycharmProjects\\guppe\\Teórico\\Sec13")))
====================================================================================================================
import os
open("dois.txt",'w').close()

# forma 2
open('tres.txt', 'a').close()

# forma 3
with open('quatro.txt', 'w') as arquivo:
    pass


====================================================================================================================
import os
# Criando arquivos
os.mknod('cinco.txt')
os.mknode("/home/kodi/teste.txt")
# Se vc estivar com MacOs pode haver erro de PermissionError
# OBS : criando um aruqaivco via MNode() se o arquivo ja exitir treremos um eror  FileExistError
====================================================================================================================

import os
# A funcao cria um diretório, se ele exitir dá um FileExistsError
os.mkdir('Tres')
# |SE não tivre permissão, dá PermissionError
====================================================================================================================
import os
# Criando arvores de diretórios
# ira criar os diretórios à partir do Atual - Relativo
os.makedirs('um/dois/tres/quatro/cinco')

# ira criar à partir do Raiz - Absoluto
os.makedirs('C:/Temp/um/dois/tres/quatro')

====================================================================================================================
import os
os.makedirs('um/dois/tres/quatro/cinco', exist_ok=True) # Tenta criar o diretório, se exitir não dá error não

====================================================================================================================

import os
# renomaar diretórios
os.rename('um', 'abobra')

# OBS : Se o diretório não exitir, teremos um FileNotFoundError
# OBS : Se o diretório que queremos renomear nao estiver vazio teremos um OSError
====================================================================================================================
import os
# ATENÇÃO TOme cuidado com os comandos de exclusão
# removendo arquivos
os.remove("geek.txt")
#Se for no windows e o arquivo estiver em uso, dá error
# caso o arquivo não exista , dá o fileNotFoundError
# Se você informar um diretório ao inves de arquivo , teremos um IsADirectoryError
====================================================================================================================
import os
# para remover diretórios
os.rmdir('abobra')
# Obs: se o diretório não estiver vazio, á um OSError
# OBS Se o diretório não exitir, dá error
====================================================================================================================
import os
# para remover diretórios de forma recursiva
os.rmdir('abobra')
# Obs: se o diretório não estiver vazio, á um OSError
# OBS Se o diretório não exitir, dá error
for arquivo in os.scandir('geek2')
    if arquivo.is_file():
        os.remove(arquivo.path)

====================================================================================================================
# sudo apt install lsb-core
# pip install send2trash
from send2trash import send2trash
send2trash('arquivo.txt') # vai pra lixeira do S.O. se o arquivo não exitir , dá error

====================================================================================================================
# TRabalhando com arquivos/dietórios temporários
# Nesse caso, os arquivos só exititrão dentro do blockl With
import tempfile, os
with tempfile.TemporaryDirectory() as tmp1:
    print(f'Criei o dir temp em  {tmp1}')
    with open(os.path.join(tmp1, 'TempFIle001.txt'), 'w') as arquivo :
        arquivo.write('Uiversidade Geka\n')
    input()

====================================================================================================================
import tempfile
with tempfile.TemporaryFile() as tmp:
    tmp.write(b'Geek File\n')
    tmp.seek(0)
    print(tmp.read())

# obs em arquivos temporarios só conseguimos escrerver Bits, por isso utiliza-se 'b'
====================================================================================================================
Sem o blockl With
import tempfile, os
arquivo = tempfile.TemporaryFile()
arquivo.write(b'Bolinha\n')
arquivo.seek(0)
print(arquivo.read())
arquivo.close()
====================================================================================================================
import os, tempfile
arquivo =  tempfile.NamedTemporaryFile()
arquivo.write(b'TEsticulo\n')
print(arquivo.name)
input()
arquivo.close()
====================================================================================================================
https://docs.python.org/3/library/os.html?highlight=os#module-os
====================================================================================================================
"""
