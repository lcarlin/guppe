"""
Decorators com diferentes assinaturas
# para resolver vários paramentros utilizamos o decorator Pattern
# A assinutara de uma função é representada pelo seu retorno , nome e parametros de entrada
====================================================================================================================
#relembrando
def grita(funcao):
    def aumentar (nome):
        return funcao(nome).upper()

    return aumentar  ### é aqui que é chamada a função AUMENTAR!

@grita
def saudacao(nome):
    return f'olá, eu sou :-> {nome}'

@grita
def ordenar(principal, aconpanhamento ):
    return f'Holla que tal, eu gostaria de {principal}, acompanhado de {aconpanhamento}, por obséquio !'

#testando
print(saudacao('Christie Monteiro'))
#print(ordenar('Bolsetes', 'Tetias'))
====================================================================================================================

# Refatorando com a Decorator Pattern
def gritar(funcao):
    def aumentar(*args, **kwargs):
        return funcao(*args, **kwargs).upper()
    return aumentar

@gritar
def saudacao(nome):
    return f'olá, eu sou :-> {nome}'

@gritar
def ordenar(principal, aconpanhamento ):
    return f'Holla que tal, eu gostaria de {principal}, acompanhado de {aconpanhamento}, por obséquio !'

@gritar
def lol():
    return 'lol'

print(saudacao('Christie Monteiro'))
print('-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-')
print(ordenar('Bolsetes', 'Tetias'))

print('-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-')
print(lol())
print('-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-')
# OBS: vale lembrar que podemos utilizar parametros nomeados:
print(ordenar(principal='Bolsetas', aconpanhamento='TETAS'))
====================================================================================================================

"""
#Decorator com argumentos
def verifica_primeiro_argumento(valor):
    def interna(funcao):
        def outra(*args, **kwargs):
            if args and args[0] != valor:
                return f'Valor incorreto, primeiro argumento precisa ser {valor}'
            return funcao(*args, **kwargs)
        return  outra
    return interna

@verifica_primeiro_argumento('pizza')
def comida_favorita(*args):
    print(args)

@verifica_primeiro_argumento(10)
def soma_dez(num1, num2 ):
    return num1 + num2

print('-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-')
print(soma_dez(10, 12))

print('-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-')
print(soma_dez(11, 12))


print('-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-')
print(comida_favorita(',Xerecas', 'pizza', 'bolsetas'))