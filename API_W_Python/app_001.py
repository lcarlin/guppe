"""
https://youtu.be/FBLAV1SbJFk
# API é um lugar pra disponibilizar recursos e/ou funcionalidades
# 1. Objetivo - crair um API de disponibilizar consulta, criação, exclusao de books 
# 2. URL BASE - 127.0.0.1
# 3. Endpoints  localhost/livros (get)   
                localhost/livros (post)  
#               localhost/livros/id (get) 
#               localhost/livros/id (put) 
#               localhost/livros/id (delete) 

# 4. Recursos - livros (?) 
pip install flask
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {'id' : 1, 
    'titulo' : 'O Senhor dos anés',
    'autor' : 'tolkien'
    },
    {'id' : 2, 
    'titulo' : 'Duna',
    'autor' : 'Frank Herbert'
    },
        {'id' : 3, 
    'titulo' : 'NeuroMancer',
    'autor' : 'William Gibbson'
    }
]

@app.route('/livros', methods=['GET'])
def obter_livros():
    return jsonify(livros)  

@app.route('/livros/<int:id>', methods=['GET'])
def obter_livros_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro) 

@app.route('/livros/<int:id>', methods=['PUT'])
def editar_livros_por_id(id):
    livro_alterado = request.get_json()
    for indice, livro in enumerate (livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])

@app.route('/livros', methods=['POST'])
def incluir_livros_por_id():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    return jsonify(livros)

@app.route('/livros/<int:id>', methods=['DELETE'])
def excluir_livros_por_id(id):
    for indice, livro in enumerate (livros):
        if livro.get('id') == id:
            del livros[indice]

    return jsonify(livros)


app.run(port=5000, host='localhost', debug=True)