import os
import py7zr

# Diretório onde os arquivos 7z estão
diretorio = 'C:\\Users\\luizc\\Desktop\\PS2_Games'

# Percorre todos os arquivos do diretório
for nome_arquivo in os.listdir(diretorio):
    # Verifica se o arquivo tem a extensão 7z
    if nome_arquivo.endswith('.7z'):
        # Cria um objeto Py7zr para descompactar o arquivo
        with py7zr.SevenZipFile(os.path.join(diretorio, nome_arquivo), 'r') as zip_file:
            # Extrai todos os arquivos do arquivo 7z
            print(nome_arquivo)
            # zip_file.extractall()
