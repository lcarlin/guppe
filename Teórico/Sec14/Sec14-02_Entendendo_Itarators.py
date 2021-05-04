"""
Entendendo Itarators e Iterables
Iterator ->
    -   uM OBJETO que pode ser iterado
    -   Um objeto que retorna um dado, sendo um elemento por vez quando uma finção Next() é chamado

Iterable -> Um Objeto que irá re3tornar um Iterator quanto a função iter() for chamada
====================================================================================================================
nome = 'Geek'  # É um iterable, mas não é um Iterator
numeros = [1,2,3,4,5,6,7,8,9,0] # É um iterable, mas não é um Iterator
print((nome))
print(numeros)

it1 = iter(nome)
it2 = iter(numeros)

print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))
====================================================================================================================

"""
nome = 'Geek'
for letra in nome :
    print(f'{letra}')