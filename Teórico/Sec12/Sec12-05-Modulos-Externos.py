"""
Modulos Externos
Utilizamos o gerenciador de pacotes Pyheon chamado PIP Python Installer Packager
Pode-se conhecer todos os pacotes externos oficiasis em https://pypi.org/
====================================================================================================================
Instalando um modulo:
num terminal (dos/shell/bash) usar
pip install {package}
====================================================================================================================

"""
# colorama -> é utilizado para permitir impressao de textos coloridos no terminal
from colorama import Fore, Back, Style
print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')