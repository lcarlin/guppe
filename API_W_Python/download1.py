import os
import sqlite3
from flask import Flask, send_file, render_template_string
from datetime import datetime

app = Flask(__name__)

# Caminho do arquivo DB no servidor
DB_PATH = '/caminho/do/servidor/PDW.db'
DB_PATH =  'C:\\Users\\actdigital\\PDW\\PDW.db'

# Função para atualizar o banco de dados após o download
def update_database():
    # Conectar ao banco de dados SQLite remoto
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Comando SQL para atualizar a coluna EXPORT_DATE
    cursor.execute("UPDATE Transient_data SET EXPORT_DATE = datetime('now') WHERE EXPORT_DATE IS NULL;")

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
    download_filename = f'PDW.{timestamp}.db'

    # Atualizar o banco de dados
    update_database()

    # Realizar o download do arquivo
    return send_file(DB_PATH, as_attachment=True, download_name=download_filename)

# Iniciar o servidor Flask
if __name__ == '__main__':
    app.run(debug=True)
