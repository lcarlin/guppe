# -*- coding: utf-8 -*-

"""
Leitura de Arquivos.
Para ler o conteudo de um arquivo em Python utilizamos a funcao integrada open()
que literalmente seignifica abrir

open() :-> Na forma + simples de utilizacao , nós passamos apenas um parametro de entrada que neste caso é o nome+caminho
do arquivo a ser lido. Essa função retorna um _io.TextIOWrapper e é com ele que iremos trabalhar então
https://docs.python.org/3/library/functions.html#open
# Obs: como podrãop a função open abre o arquivo como somente-leitura, Esse arquivo deve esxistir ou então teremos
o erro FileNotFoundError
====================================================================================================================
arquivo = open('arquivo.txt')
# print(arquivo)
# print(type(arquivo))
# para ler o conteudo de um arquivo, apos sua abertura devemos utlizar a função read()
print(arquivo.read())
print("===============================================================")
print(arquivo.read())
# OBS : o Python usa um recurso chamado de courso prar atrabalhar com arquivos. Esse cursor funciona como um  cursor da
# tela quando estamos escrevendo, logo, quando aplicamos um read() o cursor vai parar no final do arquivo.
====================================================================================================================
"""
arquivo = open('arquivo.txt')
# Aqui le o arquivo sequencialmente , converte como uma String e coloca na variavel
ret = arquivo.read()
print(type(ret))

print(ret)
print("===============================================================")
print(ret)
print("===============================================================")
