"""
Módulo Collections - Named Tuple
    *   São tuplas diferenciadas onde eespecificamos um nome para a mesma e também parametros

====================================================================================================================
review
tupla = (1,2,3)
print(tupla)
print(tupla[0])
====================================================================================================================
https://docs.python.org/3/library/collections.html#collections.namedtuple
====================================================================================================================
"""
from collections import namedtuple
# Apos o import tem que definir o nome e para-metros

# Forma 1 declaração de NT
cachorro = namedtuple('cachorro', 'idade raca nome')

#forma2
cachorro = namedtuple('cachorro', 'idade, raca, nome')

#forma3
cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])

ray = cachorro(idade=2, raca='Chow-Chow', nome='Ray')
print(ray)
print("**********************")
#acessando os dados forma 1
print(ray[0])
print(ray[1])
print(ray[2])

print("**********************")
#acessando os dados forma 1
print(ray.idade)
print(ray.raca)
print(ray.nome)

print("**********************")
print(ray.index('Chow-Chow'))
print(ray.count('Chow-Chow'))