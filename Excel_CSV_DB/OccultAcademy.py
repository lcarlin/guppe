import sqlite3
import pandas as pd
import datetime
import numpy as np
import configparser
import os
import threading

# Conectar ao banco de dados MySQL
db_file = "G:\\Meu Drive\\Occult Academy\\OccultAcademy.db"
load_file = "G:\\Meu Drive\\Occult Academy\\Arcanos Menores.xlsx"
# Conectar ao banco de dados MySQL cnx = mysql.connector.connect(user='seu_usuario', password='sua_senha', host='seu_host', database='seu_banco_de_dados')
cnx = sqlite3.connect(db_file)

# Ler as planilhas em um arquivo Excel
arquivo_excel = pd.ExcelFile(load_file)
planilhas = arquivo_excel.sheet_names

# Loop através das planilhas e inserir os dados no banco de dados
for planilha_nome in planilhas:
    # Ler a planilha em um DataFrame do pandas
    df = pd.read_excel(arquivo_excel, sheet_name=planilha_nome)
    # Inserir os dados no banco de dados
    df.to_sql(name=planilha_nome, con=cnx, if_exists='replace', index=False)

# Fechar a conexão com o banco de dados
cnx.close()