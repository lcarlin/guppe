""""
sISTEMAS DE arqiuyvos e Navegação no FileSystem

PAra fazer uso e manipulação de arquivos do SDistema Operacional, precisamos importar e fazer uso do modulo OS
os -> Operating System
====================================================================================================================
#Fazer o import
import os
# os.getcwd() -> Pega o current Work Directory
#Retorna o caminho absoluto de onde o .py está , o de o interpredador do Python é Invocado
print(os.getcwd())

#paramudar de diretórios, usamos o CGDIR()
os.chdir('../..')
print(os.getcwd())

os.
====================================================================================================================
#Fazer o import
import os
# podemos checar se um diretório é relativo ou absoluto (Abstoluto começa da Raiz, relativo comea à partir do Dir. Atual
# Sempre usar " / " mesmo no Windows ou Usar duplasBarras " // "
print(os.getcwd()) #
print(os.path.isabs('C:\\Users\\luizc\\PycharmProjects\\guppe\\Teórico\\Sec13')) #True
print(os.path.isabs('C:/Users/luizc/PycharmProjects/guppe/Teórico/Sec13/outro.txt'))
====================================================================================================================
#Fazer o import
import os
#Podemos identificar o S.O. com o módulo OS
print(os.name)

# Pode-ser tewr mais detalhes do S.O.
print(os.uname()) ## apenas em POSIX
====================================================================================================================
#Fazer o import
import os
print(os.getcwd())

res = os.path.join(os.getcwd(),'Geek') # Adiciona o diretório ao Path Absoluto, sem testar se o dir. existe ou não
os.chdir(res)
print(os.getcwd())
# Veja que o os.path.join() recebe 2 parametros, sendo o primeiroo diretório atual e o segundo o diretório que seja
# concatenado ao atual
====================================================================================================================
#Fazer o import
import os
# Podemos listar os aquivos e diretórios com o os.listdir, o retorno é uma LISTA
print (os.listdir())
print(len(os.listdir()))
for i in os.listdir():
    print(i)

====================================================================================================================

"""
#Fazer o import
import os
# Podemos listar os aquivos com mais detalhes com o ScanDir()
# print (list(os.scandir()))

scanner = os.scandir()
arquivos = list(scanner)
print(arquivos)
print(arquivos[0])

print(dir(arquivos[0])) # quais metodos são permitdos
# 'inode', 'is_dir', 'is_file', 'is_symlink', 'name', 'path', 'stat'
print(arquivos[0].inode())
print(arquivos[0].is_dir())
print(arquivos[0].is_file())
print(arquivos[0].is_symlink())
print(arquivos[0].name)
print(arquivos[0].path)
print(arquivos[0].stat())

#OBs quando usamos a função ScanDir, precisamos fecha-la assim como usamos um aquivo
scanner.close()