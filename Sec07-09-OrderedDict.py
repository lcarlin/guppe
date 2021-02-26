"""
Modulo Collections :-> Ordered Dict
Em um dicionário,a ordem de inerção dos elementos não é garantida
====================================================================================================================
dicionario = {'a': 1,
              'b': 2,
              'c': 3,
              'd': 4,
              'e': 5}
print(dicionario)

for chave, valor in dicionario.items():
    print(f'chave = {chave} ; valor = {valor}')
====================================================================================================================
OrderedDict -> Dicionário que nos garante a ordem de inserção dos elementos .
Talkey
====================================================================================================================
from collections import OrderedDict
dicionario = {'a': 1,
              'b': 2,
              'c': 3,
              'd': 4,
              'e': 5}

for chave, valor in dicionario.items():
    print(f'chave = {chave} ; valor = {valor}')
====================================================================================================================
"""

from collections import OrderedDict

# dicionario comum
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1 }
print (dict2 == dict1)  # verdadeiro, já que a ordem não importa para os dicionários

odict1 = OrderedDict({'a': 1, 'b': 2})
odict2 = OrderedDict( {'b': 2, 'a': 1 })
print(odict2 == odict1) ## Agora mostra como falso, pois até a ordem é considerada