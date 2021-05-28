"""
Argumentos Somente Posicionais
"""

# valor = '67.3'
# print(float(valor))

# def cumprimenta_v1(nome):
#     return f'Olá {nome}'
#
# print(cumprimenta_v1('Geek'))
# print(cumprimenta_v1(nome='Geek'))


# def cumprimenta_v2(nome, /):
#     return f'Olá {nome}'
#
# print(cumprimenta_v2('Geek'))
# print(cumprimenta_v2(nome='Geek'))

# def cumprimenta_v3(nome, /, mensagem='Olá'):
#     return f'{mensagem} {nome}'
#
# print(cumprimenta_v3('Geek'))
# print(cumprimenta_v3('University', mensagem='Hello'))
# print(cumprimenta_v3('Felicity', 'Bem-vinda'))

# def cumprimenta_v4(nome, mensagem='Olá', /):
#     return f'{mensagem} {nome}'
#
# print(cumprimenta_v4('Geek'))
# print(cumprimenta_v4('Felicity', 'Bem-vinda'))
# print(cumprimenta_v4('University', mensagem='Hello'))

# def cumprimenta_v5(*, nome):
#     return f'Olá {nome}'
#
# print(cumprimenta_v5(nome='Geek'))
# print(cumprimenta_v5('Geek'))

def cumprimentar_v6(nome, /, mensagem1='Olá', *, mensagem2):
    return f'{mensagem1} {nome} {mensagem2}'

print(cumprimentar_v6('Geek', mensagem1='Hello', mensagem2='tenha um bom dia'))
print(cumprimentar_v6('Geek', mensagem2='tenha um bom dia'))
print(cumprimentar_v6('Geek', 'Oi', mensagem2='Vamos?'))

