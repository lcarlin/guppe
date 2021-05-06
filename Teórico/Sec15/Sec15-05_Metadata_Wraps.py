"""
Preservando MetaData com wrapps
MetaDatas:-> São dados intrisecos em arquivos
Wraps :-> são funcões que envolvem elementos com diversas finalidadesa
====================================================================================================================
#problema
def ver_log(funcao):
    def logar(*args, **kwargs):
        #  Eu sou uma função de logar dentro da outra
        print(f'você está a chamar a função {funcao.__name__}')
        print(f'E aqui você tem a documentacao: {funcao.__doc__}')
        return  funcao(*args, **kwargs)
    return logar

@ver_log
def soma (a, b) :
    # Somar 2 numeros
    return a + b

print('-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-')
print(soma(10,30))
print('-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-')
print(soma.__name__)
print(soma.__doc__)
====================================================================================================================
"""
#Resolução
from functools import wraps

def ver_log(funcao):
    @wraps(funcao)
    def logar(*args, **kwargs):
        """Eu sou uma função de logar dentro da outra"""
        print(f'você está a chamar a função {funcao.__name__}')
        print(f'E aqui você tem a documentacao: {funcao.__doc__}')
        return  funcao(*args, **kwargs)
    return logar

@ver_log
def soma (a, b) :
    """Somar 2 numeros """
    return a + b

print('-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-')
print(soma(10,30))
print('-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-')
print(soma.__name__)
print(soma.__doc__)