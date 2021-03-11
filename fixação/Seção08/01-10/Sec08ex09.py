from math import pi
def volumeCilindro(raio, altura):
    return pi * (raio**2) * altura

valorRaio = int(input("entre com o Raio do cilindro  :-> "))
valorAltura = int(input("entre com a altura do cilindro  :-> "))
volume = volumeCilindro(valorRaio,valorAltura)
print(f'E o volume do cilindro é  :-> {volume}')