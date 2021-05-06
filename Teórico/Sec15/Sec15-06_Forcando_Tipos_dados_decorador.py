"""
Forçando os tipos de decoradores
FUNZÇÃO ZIP
A =  (1, 3, 5)
B = (2, 4, 6)
c= zip(A,B)
(1,2), (3,4), (5,6)
====================================================================================================================
"""

def forca_tipo(*tipos):
    def decorador (funcao):
        def converte(*args, **kwargs):
            novo_args = []
            for (valor, tipo) in zip(args, tipos):
                novo_args.append(tipo(valor)) #str('Geek')
            return funcao(*novo_args, **kwargs)
        return converte
    return decorador

@forca_tipo(str, int)
def repete_msg(msg, vezes):
    for vez in range(vezes):
        print(msg)

@forca_tipo(float, float)
def dividir(a, b):
    print(a/b)

print('-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-')
repete_msg('Geek','3')

print('-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-')
dividir('1',5)