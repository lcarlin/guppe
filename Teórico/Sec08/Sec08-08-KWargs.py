"""
**kwargs
Poderiamos chamar este parametro de ' **xis ', mas por convençao chamamos de **kwargs.
est6e é só mais um parametro, mas diferente de *args que coloca os valores extras em uma Tupla, o **kwargs exige
que utilizemos parametros nomeados, que transforma esses paramentros extras em 1 dicionário.
====================================================================================================================
#Exemplo
def cores_favoritas(**kwargs):
    print(kwargs)
    print('**********')
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} é :-> {cor}')

cores_favoritas(marcos='abobra', feminzi='azuis', jao='terra', pedro='Pedra')
# OBS os parametros *args e **kwargs não são obrigatórios
====================================================================================================================
# exemplo mais complexo
def cumnprimento_especial(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'Python':
        return 'Voce recebeu um cumprimento Pythonico Geek'
    elif 'geek' in kwargs:
        return f"{kwargs['geek']} Geek!"
    return 'Não tenho certeza de quem vc é '

print(cumnprimento_especial())
print(cumnprimento_especial(geek='Python'))
print(cumnprimento_especial(geek='especial'))
print(cumnprimento_especial(geek='OI'))
print(cumnprimento_especial(jaspion='Tres'))
====================================================================================================================
# Nas nossas funções podemos ter (NESTA Ordem ) :
-   PArametros Obrigatórios
-   *args;
-   Parametros Default não obrigatórios
-   **kwargs

def minha_funcao(idade, nome, *args, solteiro=False, **kwargs):
    print('===============================')
    print(f'{nome} tem {idade}')
    print(args)
    if solteiro:
        print('Solteiro')
    else:
        print('Casado')
    print(kwargs)


minha_funcao(8, 'JUlia')
minha_funcao(18, 'Felicidade', 4, 5, 3, solteiro=True)
minha_funcao(34, 'Felpe', eu='Nao', voce='Vai')
minha_funcao(19, 'Carla', 3, 4, 9, java=False, python=True)
====================================================================================================================
# Entenda o motivo pelo quel é importante manter a ordem dos parametros na declaração:
# função com a ordem correta de parametros
#def mostra_info(a, b, *args, instrutor = 'Geek', **kwargs):
#    return [a, b, args, instrutor, kwargs]

# função com a ordem incorreta de parametros
def mostra_info(a, b, instrutor = 'Geek',  *args, **kwargs):
    return [a, b, args, instrutor, kwargs]

a = 1
b = 2
args = (3,)
Instrutor = geek
kwargs = {'sobrenome': university, 'cargo':instrutor}

print(mostra_info(1,2,3,sobrenome='University', cargo='Instrutor'))
====================================================================================================================
#Desempacotar com o**kwargs
def mostra_nomes (**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"

nomes = {'nome' : 'Felicidade', 'sobrenome': 'jones' }
print(mostra_nomes(**nomes))
====================================================================================================================
def soma_mult_num(a, b, c):
    print(a + b + c)

lista = [1,2,3]
tupla = (1,2,3)
conj = {1,2,3}

soma_mult_num(*lista)
soma_mult_num(*tupla)
soma_mult_num(*conj)

dicionario = dict(a=1, b=2, c=3)
soma_mult_num(**dicionario)

# OBS: os nomes das chaves em um dicionário devem ser os mesmos dos parametros da função
====================================================================================================================
====================================================================================================================
"""
