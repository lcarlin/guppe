from flask import Flask, request, jsonify
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'G:\\TEST\\TEMP'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/upload', methods=['POST'])
def upload_file():
    # Verifica se o arquivo está na requisição
    if 'file' not in request.files:
        return jsonify({'error': 'Nenhum arquivo encontrado'}), 400

    file = request.files['file']
    codigo_cliente = request.form['codigo_cliente']
    data_nascimento = request.form['data_nascimento']
    numero_cpf = request.form['numero_cpf']

    # Verifica se o arquivo tem um nome válido
    if file.filename == '':
        return jsonify({'error': 'Nome de arquivo inválido'}), 400

    # Salva o arquivo no diretório configurado
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))

    # Pode fazer algo com as variáveis recebidas, como salvar em um banco de dados

    return jsonify({'message': 'Arquivo enviado com sucesso',
                    'codigo_cliente': codigo_cliente,
                    'data_nascimento': data_nascimento,
                    'numero_cpf': numero_cpf}), 200

if __name__ == '__main__':
    app.run(debug=True)