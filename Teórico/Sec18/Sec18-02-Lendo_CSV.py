# -*- coding: cp1252 -*-
"""
Se��o 18 : Lendo arquivo CSV
CSV -> Comma Separated Value
Separadores:
    -   Por virgula
    -   Por Ponto-e-virgura
    -   Por Pipe
    -   Por TAB
    -   Por espa�os
A linguagem Pyuthon possui 2 formas diferentes pra ler CSV :
    -   reader -> Permite que iteremos sobre as linhas dos arquivos como lista
    -   DictReader -> Permite que iteremos sobre as linhas do aquivo CSV como OrderedDicts

====================================================================================================================
http://dados.gov.br/dataset
====================================================================================================================
def abre_arquivo(file):
    ## Popssivel de se trabalhar mas n�o � o ideal, � travbalhoso
    with open(file, 'r') as arquivo:
        dados = arquivo.read().split(',')
        print(type(dados))
        print(dados)
    return dados

====================================================================================================================
from csv import reader
def abre_arquivo(file):
    with open(file, 'r') as arquivo:
        leitor_csv = reader(arquivo)
        next(leitor_csv)
        ## cada linha � uma lista
        for linha in leitor_csv:
            print(f' {linha[0]} nasceu no  {linha[1]} e tem {linha[2]} de alturas')

        return leitor_csv
====================================================================================================================
from csv import DictReader
def abre_arquivo(file):
    with open(file, 'r') as arquivo:
        leitor_csv = DictReader (arquivo)
        # next(leitor_csv)
        ## cada linha � um Ordered Dict
        for linha in leitor_csv:
            print(f" {linha['Nome']} nasceu ns {linha['Pa�s']} e mede {linha['Altura (em cm)']} cms de altura")

        return leitor_csv
====================================================================================================================
====================================================================================================================
"""
# Reader
from csv import DictReader
def abre_arquivo(file):
    with open(file, 'r') as arquivo:
        leitor_csv = DictReader (arquivo, delimiter=',')
        # next(leitor_csv)
        ## cada linha � um Ordered Dict
        for linha in leitor_csv:
            print(f" {linha['Nome']} nasceu ns {linha['Pa�s']} e mede {linha['Altura (em cm)']} cms de altura")

        return leitor_csv

def main():
    print('-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-')
    dois = abre_arquivo('lutadores.csv')
    print(type(dois))


## e � aqui que a brincadeitra come�a
if __name__ == '__main__':
    main()
