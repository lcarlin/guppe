"""
####################################################################################
# Author  : Carlin, Luiz A. .'.
# e-mail  : luiz.carlin@gmail.com
# Date    : 04-OCT-2023
# purpose : API to populate tha table
#           ET&L -> Extract, Transform & Loader
####################################################################################
# Version control
# Date       # Version #    What                            #   Who
# 2023-10-04 # 1.0.0   # Inicial Version                    # Carlin, Luiz A. .'.
# 2024-11-07 # 2.0.0   # Database file dowwnload previa     #
####################################################################################
# Current Version :2.0.0
####################################################################################
# TODO: Read parameters from configuration (data base, tables, etc)
# TODO:   READ : Database dir.
# TODO:   READ : database Name
# TODO:   READ : TRANSIENT table name
# TODO:   READ : TRANSIENT DATA COLOUMN
# TODO: Print configurarion
# TODO: Print Inserted item
# TODO: Print read Item from form
####################################################################################
"""

from flask import Flask, request, jsonify, render_template, send_file, render_template_string
import pandas as pd
import sqlite3
import numpy as np
import datetime
import configparser
from gevent.pywsgi import WSGIServer


app = Flask(__name__)
# Rota para inserir um lançamento
@app.route('/inserirLancamento', methods=['POST'])
def inserir_lancamento():
    try:
        data = request.form['data']
        tipo = request.form['tipo']
        descricao = request.form['descricao']
        credito = float(request.form['credito'])
        debito = float(request.form['debito'])
        origem = request.form['origem']
        # Criar um DataFrame com os dados do lançamento
        df = pd.DataFrame({'data': [data],
                           'tipo': [tipo],
                           'descricao': [descricao],
                           'credito': [credito],
                           'debito': [debito],
                           f'{origem_dados}' : [origem],
                           'CREATION_DATE': datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
                           'EXPORT_DATE':  np.nan
        })
        # Conectar ao banco de dados SQLite3
        conn = sqlite3.connect(sqlite_database)
        print(out_line)
        print(df)

        # Inserir o DataFrame no banco de dados
        df.to_sql(transient_data_table, conn, if_exists='append', index=False)
        conn.close()
        return jsonify({"message": "Lançamento inserido com sucesso!"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 400


@app.route('/formulario', methods=['GET'])
def form():
    conn = sqlite3.connect(sqlite_database)
    cursor = conn.cursor()
    # Busque os valores da tabela "Tipos"
    cursor.execute(f"SELECT Descrição as nome FROM {types_of_entries}")
    tipos = [row[0] for row in cursor.fetchall()]
    # Busque os valores da tabela "Origens"
    cursor.execute("SELECT nome FROM Origens")
    origens = [row[0] for row in cursor.fetchall()]
    conn.close()
    return render_template('seu_template.html', tipos=tipos, origens=origens)


# Função para atualizar o banco de dados após o download
def update_database():
    # Conectar ao banco de dados SQLite remoto
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Comando SQL para atualizar a coluna EXPORT_DATE
    cursor.execute(f"UPDATE {transient_data_table} SET EXPORT_DATE = datetime('now') WHERE EXPORT_DATE IS NULL;")

    # Confirmar e fechar a conexão
    conn.commit()
    conn.close()

# Rota principal da página HTML com o botão de download
@app.route('/')
def index():
    return render_template_string('''
        <!DOCTYPE html>
        <html lang="pt-br">
        <head>
            <meta charset="UTF-8">
            <title>Download Banco de Dados</title>
        </head>
        <body>
            <h1>Baixar Banco de Dados Remoto</h1>
            <form action="/download" method="get">
                <button type="submit">Baixar Banco-de-dados remoto</button>
            </form>
        </body>
        </html>
    ''')

# Rota para realizar o download do banco de dados
@app.route('/download')
def download_file():
    # Adicionar timestamp ao nome do arquivo
    timestamp = datetime.now().strftime('%Y%m%d.%H%M%S')
    download_filename = f'{out_db}.{timestamp}.{db_file_type}'

    # Atualizar o banco de dados
    update_database()

    # Realizar o download do arquivo
    return send_file(DB_PATH, as_attachment=True, download_name=download_filename)


#############################################################################################
current_version = "9.7.0"
api_version = "2.0.0"
config = configparser.ConfigParser()
config_file = '..\\Excel_CSV_DB\\PersonalDataWareHouse.cfg'
try:
    print('Reading configuration file ... .. .')
    with open(config_file) as cfg:
        config.read_file(cfg)

    parameters_version = config['SETTINGS']['CURRENT_VERSION']
    parameters_api_version = config['SETTINGS']['API_VERSION']
    if parameters_version != current_version and api_version != parameters_api_version: 
        print('Something went wrong ... ')
        print(f'The version(s) in parameter file {config_file} does not Match')
        print('Application ')
        print(f'Informed :-> {parameters_version}')
        print(f'Expected :-> {current_version}')
        print('API ')
        print(f'Informed :-> {parameters_api_version}')
        print(f'Expected :-> {api_version}')
        exit(1)

    transient_data_table = config['SETTINGS']['TRANSIENT_DATA_TABLE']
    transient_data_file = config['FILE_TYPES']['TRANSIENT_DATA_FILE']
    origem_dados = config['SETTINGS']['TRANSIENT_DATA_COLUMN']
    dir_db = config['DIRECTORIES']['DATABASE_DIR']
    out_db = config['FILE_TYPES']['OUT_DB_FILE']
    db_file_type = config['FILE_TYPES']['DB_FILE_TYPE']
    types_of_entries = config['SETTINGS']['TYPES_OF_ENTRIES']
    sqlite_database = dir_db + out_db + '.' + db_file_type

except FileNotFoundError:
    print(f"Configuration file {config_file} not found !")
    exit(1)
except configparser.Error as e:
    print(e)
    exit(1)
except Exception as e:
    print(e)
    exit(1)

out_line = ">" + ("=" * 120) + "<"
print(out_line)
print(f'Current Version         :-> {current_version}')
print(f'Transient Data Table    :-> {transient_data_table}')
print(f'Input Databse file      :-> {sqlite_database}')
print(f'Source of Data Column   :-> {origem_dados}')
print(f'Type of Entries column  :-> {types_of_entries}')
print(out_line)
DB_PATH = sqlite_database


if __name__ == '__main__':
    #app.run(debug=True)
    http_server = WSGIServer(('0.0.0.0',8123 ), app)
    http_server.serve_forever()


#############################################################################################