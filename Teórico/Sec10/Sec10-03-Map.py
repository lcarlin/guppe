"""
MAP
Com MAP, fazemos mapeamento de valroes para função:
====================================================================================================================
import math

def area(r):
   # calcula a área de um circulo com o raio 'r '
    return math.pi * (r**2)

print(area(2))
print(area(3))
print(area(4))
print(area(5.3))

# MAP é uma função que recebe 2 parametros: O Primeiro é a funcao o Segundo um iteravel . retornna um MAP Object

# forma -1 classico
raios = [2,3,5,7,0.3, 10, 44]
areas = []
for r in raios:
    areas.append(area(r))
print(areas)

# forma 2 melhor
areas = []
areas = map(area, raios)
print(areas)
print(type(areas))
print(list(areas))


## forma 3 MAP com lambdas
print (list(map ( lambda r: math.pi * (r**2) , raios)))
# OBS: após utilizar a função map() depois da 1ª utilização do resultado, ele ZERA
====================================================================================================================
# Para fixar MAP
# temos dados Iteraveis a1, a2, ..., an
# temos uma função
# funçao : f(x)
# utilizamos a função map(f,dados) onde map irá mapear cada elemento dods dados e aplicar a funçlção
# o MAP Object : f(a1), f(a2), ... f(an)

====================================================================================================================

"""

#Mais um explos
cidades = [
    ('Berlin', 29),
    ('Cairo', 36),
    ('Bois nos Ares',19),
    ('Los Anfeles', 26),
    ('Tokio',27),
    ('Nova Iorque', 28),
    ('Londres', 22) ]

print(cidades)
# f = 9/5  * c + 32
celciusParaF = lambda dado: (dado[0], (9/5*dado[1]+32))
print(list(map(celciusParaF,cidades)))