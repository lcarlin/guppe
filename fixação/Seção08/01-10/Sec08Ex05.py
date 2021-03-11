from math import pi
def volumeEsfera(raio):
    return 4/3 * pi * (raio**3)


numero = int(input("entre com o Raio da Es-Fera :-> "))
print(f'E o Volume para a esfera com raio {numero} é :-> {volumeEsfera(numero)}')