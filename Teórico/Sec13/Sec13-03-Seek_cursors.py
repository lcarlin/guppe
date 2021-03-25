# -*- coding: utf-8 -*-
"""
Seek :-> é uitilizada para movimentar o cursor pelo arquivo

Obs : QUando abrimos um arquivo ocm a função Open, ´é criada uma conexão enttre o arquivo no disco do computador e o
programa. Essa conexão é chamada de Streaming. Ao finalizar os trabalhos com o arquivo, devemos fechar essa conexão.
PAra isso usamos a função close

Passo para trabalhar com o arquivo
1) Abrir o arquivo
2) Trabalhar com oAruivo
3) Fechar o arquivo
====================================================================================================================
arquivo = open('arquivo.txt')
print(arquivo.read())
print("===============================================================")
arquivo.seek(0)
print(arquivo.read())
print("===============================================================")
arquivo.seek(22)
print(arquivo.read())
print("===============================================================")
====================================================================================================================
arquivo = open('arquivo.txt')
# readline() le po arquivo linha-a-linha
for i in range (0,7):
    print(arquivo.readline())
====================================================================================================================
arquivo = open('arquivo.txt')
ret = arquivo.readline()
print(type(ret))
print(ret)
print(ret.split(' '))
print("===============================================================")
====================================================================================================================
arquivo = open('arquivo.txt')
linhas = arquivo.readlines()
print(len(linhas))
print("===============================================================")
====================================================================================================================
# 1) Abrir o arquivo
arquivo = open('arquivo.txt')

# 2) Trabalhar o arquivo

print(arquivo.closed)  ## Flag Booleana para o status do arquivo

# 3) fechar o arquivo
arquivo.close()

print(arquivo.closed)  ## Flag Booleana para o status do arquivo
print(arquivo.read()) # Se tentarmos manipular o arquivo após o seu fechamento, teremos um
# ValueError: I/O operation on closed file.

print("===============================================================")
====================================================================================================================
"""

# 1) Abrir o arquivo
arquivo = open('arquivo.txt')
print(arquivo.read(3)) # imprime os primeiros N caracteres do arquivo.