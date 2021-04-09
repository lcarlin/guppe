"""
StringIO
Atenção, para Ler ou escrever dados em arqauivos do sistema operacional o Softywares oreciusa ter  permissoes de:
    -   Permissão de Leitura -> para Ler o Arquivo
    -   Permissao de Escrita -> Para gravar o arquivo

StringIO -> Utilizado para Ler e Criar arquivos em Memória.

====================================================================================================================
"""
# primeiro, faz-se o Import
from io import StringIO
mensagemn = 'Esse é apenas uma String Normal'

#Podemos criar um arqauivo em memoria jpa com uma String inserida ou mesmo Vazio para inserirmos textos depois
arquivo = StringIO(mensagemn)
# arquivo = open('arquivo.txt','w')

# Agora, tenmdo o arquivo podemos utilizar tudo o que já sabemos
print(arquivo.read())
arquivo.write("Mais um texto")
#Podemos inclusive movimentar o cursor

arquivo.seek(0)
print(arquivo.read())