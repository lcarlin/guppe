"""
TRabalhando com modulos Built-in (integrados)que já vem no python
====================================================================================================================
https://docs.python.org/3/py-modindex.html
====================================================================================================================
# utilizando o Alias (Apelidos) para modulos / funções
import random as rdm
print(rdm.random())
====================================================================================================================
# Podemos importar todas as funções de um módulo utilizando o " * "
from random import *
print(random())
====================================================================================================================
# utilizando alias (apelidos) para modulos/funções
from random import randint as rdi, random as rdm
print(rdi(5,89))
print(rdm())
====================================================================================================================

"""
# costumamos a utilizar tuple para colocar mulstiplos imports de um mesm modulo
from random import (
    randint,
    random,
    choice,
    shuffle
)
lista =  ['pedra', 'papel', 'tesoura', 'Spock', 'lagarto']
shuffle(lista)
print(random())
print(randint(0,10))
print(lista)
print(choice('University'))
