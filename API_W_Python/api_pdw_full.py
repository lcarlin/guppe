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
# 2024*12-23 # 2.0.0.  # Agora Baixa o XLSX pronto, ao inves do DB
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

from flask import Flask, request, jsonify, render_template, send_file, render_template_string, Response
import pandas as pd
import sqlite3
import numpy as np
import datetime
import configparser
import time, os

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
        # return jsonify({"message": "Lançamento inserido com sucesso!"}), 201
        return render_template_string('''
        <!DOCTYPE html>
        <html lang="pt-br">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Redirecionando...</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    margin: 0;
                    padding: 0;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    background-color: #f9f9f9;
                    text-align: center;
                    color: #333;
                }
                .container {
                    max-width: 600px;
                    padding: 20px;
                    background: #fff;
                    border-radius: 10px;
                    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                }
                h1 {
                    font-size: 1.5rem;
                    margin-bottom: 10px;
                }
                p {
                    font-size: 1rem;
                    margin-bottom: 20px;
                }
                @media (max-width: 480px) {
                    h1 {
                        font-size: 1.25rem;
                    }
                    p {
                        font-size: 0.9rem;
                    }
                }
            </style>
            <script>
                setTimeout(function() {
                    window.location.href = "/formulario";
                }, 5000); // 5000ms = 5 segundos
            </script>
        </head>
        <body>
            <div class="container">
                <h1>Lançamento inserido com sucesso!</h1>
                <p>Você será redirecionado para o formulário em 5 segundos...</p>
            </div>
        </body>
        </html>
        '''), 201

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

# Rota principal de download que chama a função de envio do arquivo e depois atualiza o banco de dados
@app.route('/download')
def download_file():
    # Adicionar timestamp ao nome do arquivo
    timestamp = datetime.datetime.now().strftime('%Y%m%d.%H%M%S')
    # download_filename = f'PDW.{timestamp}.db'
    download_filename = transient_data_exportator(sqlite_database, dir_db, out_type, transient_data_file, transient_data_table,  origem_dados )

    # Gerar a resposta de streaming
    response = Response(
        # stream_file(DB_PATH),
        stream_file(download_filename),
        headers={
            'Content-Type': 'application/octet-stream',
            'Content-Disposition': f'attachment; filename={download_filename}'
        }
    )

    # Adicionar a lógica para chamar `update_database` após a transmissão do arquivo
    @response.call_on_close
    def on_close():
        update_database()
        os.remove(download_filename)

    return response

# Função para realizar a atualização do banco de dados
def update_database(  ):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    sql_sentence = f"UPDATE Transient_data SET EXPORT_DATE = datetime('now') WHERE EXPORT_DATE IS NULL;"
    print(sql_sentence)
    cursor.execute(sql_sentence)
    conn.commit()
    conn.close()
    print(f'Meteu o Update no banco de dados')

# Função para ler o arquivo em blocos e transmiti-lo como resposta
def stream_file(file_path):
    # Ler o arquivo em blocos e transmiti-lo
    with open(file_path, 'rb') as file:
        while chunk := file.read(8192):  # 8192 bytes por vez (8 KB)
            yield chunk

# Rota para exibir o relatório
@app.route('/relatorio')
def relatorio():
    conn = sqlite3.connect(sqlite_database)
    df = pd.read_sql_query(f"SELECT * FROM {transient_data_table} where export_date is null ORDER BY 1", conn)
    conn.close()

    # Converte o DataFrame para HTML
    tabela_html = df.to_html(index=False, classes='table table-striped table-responsive', border=0)
    return render_template('relatorio.html', tabela=tabela_html)

def transient_data_exportator(sqlite_database, dir_out, out_extension, file_name, transient_data_table, origing_column):
    print('Exporting Transient data into individual Sheelts ... .. .  ')
    #file_full_path = dir_out + file_name + '.' + datetime.datetime.now().strftime(
    file_full_path = file_name + '.' + datetime.datetime.now().strftime(
        "%Y%m%d.%H%M%S") + '.' + out_extension
    connection = sqlite3.connect(sqlite_database)
    xlsx_writer = pd.ExcelWriter(file_full_path, engine='xlsxwriter', date_format='yyyy-mm-dd')
    guiding_df = pd.read_sql(f"select distinct {origing_column} from {transient_data_table}", connection)
    conn = connection.cursor()

    for i, linhas in guiding_df.iterrows():
        excel_sheet = f"{linhas.Origem}"
        message = f'   . .. ... Step: {i + 1:04} :-> Exporting Sheet {excel_sheet.ljust(25)} to {file_full_path}'
        sql_statment = f"SELECT * FROM {transient_data_table} where {origing_column} = '{linhas.Origem}' and EXPORT_DATE is null order by 1;"
        df_out = pd.read_sql(sql_statment, connection)
        if len(df_out) > 0 :
            print(message)
            df_out.to_excel(xlsx_writer, sheet_name=excel_sheet, index=False)
#            conn.execute(f"UPDATE {transient_data_table} SET EXPORT_DATE = datetime('now') WHERE {origing_column} = '{linhas.Origem}'; ")
#            conn.execute('COMMIT; ')

    connection.close()
    xlsx_writer.close()
    return file_full_path

#############################################################################################
current_version = "9.7.0"
api_version = "2.0.0"
config = configparser.ConfigParser()
## atenção , sempre alterar esse PATH em Produção
config_file = '../Excel_CSV_DB/PersonalDataWareHouse.cfg'
os.environ['TZ'] = 'America/Sao_Paulo'
## atenção , sempre descompentar a linha abaixo em prod
#time.tzset()
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
    last_update_file = 'LAST_UPDATE_FILE.dat'
    out_type =  config['FILE_TYPES']['TYPE_OUT']

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
    app.run(debug=True)
    #http_server = WSGIServer(('0.0.0.0',8123 ), app)
    #http_server.serve_forever()


#############################################################################################
