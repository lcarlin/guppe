# -*- coding: cp1252 -*-
"""
Seção 18 :
    Escrevendo em arquivos CSVs
Utilzar sempre metodos semelhantes pra ler/escrever
reader()
writerow() -> escreve uma unica linhas

write() -> gera um uobjeto para que possamos escreber em um arquivo CSV,
Utilizamos o metodo writerow()  para escrever cada linha Este metodo recebe uma lista
====================================================================================================================
def gravar(file):
    with open(file, 'w') as arquivo:
        escritor_csv = writer(arquivo)
        escritor_csv.writerow(['Titulo','Gênero', 'Duracao'])
        while True:
            filme = input(f'Fala ai o filme :-> ')
            if filme.upper() == 'SAIR':
                break
            genero  = input(f'Agora o Genero  :-> ')
            duracao = input(f'E a duracao     :-> ')
            escritor_csv.writerow([filme, genero, duracao])
====================================================================================================================
====================================================================================================================
====================================================================================================================
====================================================================================================================
====================================================================================================================
"""
# Agora com DictReader
# As chaves do dicionário devem ser as mesmas utilzadas como cabecalhjo
from csv import DictWriter

def gravar(file):
    with open(file, 'w') as arquivo:
        cabecalho = (['Titulo', 'Gênero', 'Duracao'])
        escritor_csv = DictWriter(arquivo, fieldnames=cabecalho)
        escritor_csv.writeheader()
        while True:
            filme = input(f'Fala ai o filme :-> ')
            if filme.upper() == 'SAIR':
                break
            genero = input(f'Agora o Genero  :-> ')
            duracao = input(f'E a duracao     :-> ')
            escritor_csv.writerow({"Titulo":filme, "Gênero":genero, "Duracao":duracao })


def main():
    print('-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-')
    gravar('Filmes.dat')


## e é aqui que a brincadeitra começa
if __name__ == '__main__':
    main()
