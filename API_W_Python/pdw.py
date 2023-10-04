from flask import Flask, request, jsonify
import pandas as pd
import sqlite3
import numpy as np
import datetime

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
                           'origem': [origem],
                           'CREATION_DATE': datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
                           'EXPORT_DATE':  np.nan
        })

        # Conectar ao banco de dados SQLite3
        conn = sqlite3.connect('seu_banco_de_dados.db')

        # Inserir o DataFrame no banco de dados
        df.to_sql('Lancamentos_gerais_tmp', conn, if_exists='append', index=False)

        conn.close()

        return jsonify({"message": "Lançamento inserido com sucesso!"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
