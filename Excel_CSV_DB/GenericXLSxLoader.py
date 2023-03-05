import sqlite3
import pandas as pd
import argparse
import datetime
import numpy as np
import configparser
import os
import threading

parser = argparse.ArgumentParser()

## definindo os argumentos de linha de comando
parser.add_argument('--s', '--sqlite3-database', help='Path + nome do Banco-de-dadosSQLite')

parser.add_argument('--x', '--excel-input-file', help='Path + Nome do arquivo Excel a ser carregado ')

args = parser.parse_args()

# Conectar ao banco de dados MySQL

#db_file = "G:\\Meu Drive\\Occult Academy\\OccultAcademy.db"
#load_file = "G:\\Meu Drive\\Occult Academy\\Arcanos Menores.xlsx"
db_file = args.s
load_file = args.x

# Conectar ao banco de dados MySQL cnx = mysql.connector.connect(user='seu_usuario', password='sua_senha', host='seu_host', database='seu_banco_de_dados')
cnx = sqlite3.connect(db_file)

# Ler as planilhas em um arquivo Excel
arquivo_excel = pd.ExcelFile(load_file)
planilhas = arquivo_excel.sheet_names

# Loop através das planilhas e inserir os dados no banco de dados
print(f'Input XLSx File          :-> {load_file}')
print(f'Output SQLite3 data-base :-> {db_file}')
for planilha_nome in planilhas:
    print(f'Loading XLSx WorkSheet   :-> {planilha_nome}')
    # Ler a planilha em um DataFrame do pandas
    df = pd.read_excel(arquivo_excel, sheet_name=planilha_nome)
    # Inserir os dados no banco de dados
    df.to_sql(name=planilha_nome, con=cnx, if_exists='replace', index=False)

# Fechar a conexão com o banco de dados
cnx.close()