"""
MOdule -> é apenas um arquivo Python que pode ter diversas funções;
Pacote -> é um DIRETÓRIO contendouma coleção de modulos
OBS nas versoles Python < 3 , um pacote deveria conter um arquivc chamado __init__.py
NAs versões Python >= 3, a utizlização do arquivo __init__.py não é obrigatorio, mas aconselhaverl pra manter compatibilidade

====================================================================================================================
"""

from geek import geek1, geek2
from geek.university import geek3, geek4
print(geek1.piu)
print(geek1.funcao1(4,6))
print(geek2.curso)
print(geek2.funcao2())