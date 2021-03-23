"""
len () :-> retorna o tamanhpo/numero de itens de um Iteravel
# Só pra revisar :
print(len('Geek University'))
print(len([1, 2, 3, 4, 5]))
print(len((1, 2, 3, 4, 5)))
print(len({1, 2, 3, 4, 5}))
print(len({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}))
# Internamente, a funcão len do python faz o seguinte :
# Dunder len
print('Geek University'.__len__( ))
====================================================================================================================
abs() -> retorna o valor absoluto de um numero inteiro ou real , basicamente seria o seu valor real sem o sinal
print (abs(-5))
print (abs(5))
print (abs(3.14))
print (abs(-3.14))
====================================================================================================================
sum() -> recebe como parametyro um iteravel , podemndo ereceber um valor inicial e retorna a som atotal dos elementos
incluindo o valor inicial
print(sum([1,2,3,4,5]))
print(sum([1,2,3,4,5], 5))

print(sum([1, 2, 3, 4, 5]))
print(sum((1, 2, 3, 4, 5)))
print(sum({1, 2, 3, 4, 5}))
print(sum({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}.values()))
====================================================================================================================
round() retornoa um numero arrendodado para N digitos de precisao após a casa decimal
se a rpecisao não for informada, retorna o inteiro + proximo da entrada
====================================================================================================================

"""
# Exemplos de Round
print (round(10.2))
print (round(10.5))
print (round(10.6))
print (round(1.21212121))
print (round(1.21212121, 2))
print (round(1.219999, 2))