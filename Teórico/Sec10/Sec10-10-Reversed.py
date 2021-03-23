"""
Reversed
OBS: não confunda com a funsão Reverse () que estudamos nas listas
o Metodo é intrinsico à listas
ja a função Reversed() funciona com qualquer iterável
A função reversed retorna um Iteravel chamado ListReversedIterator
====================================================================================================================
"""
lista = [4, 7, 3, 8, 1, 4, 2]
res = reversed(lista)
print(type(res))

# Podemos converter o elemento retornado para uma lista, tupoa ou conjunto
print(list(reversed(lista)))
print(tuple(reversed(lista)))
# OBS em conjuntos não definimos a ordem dos elementos
print(set(reversed(lista)))

# podemos iterar sobre o reversed
for letra in reversed('Geek University'):
    print(letra, end='')
print("\n **********************")
# Podemos fazer o mesmo sem o uso do For
print(''.join(list(reversed('Geek University'))))
print("\n **********************")
# Ja vimos como fazer isso umais fácil ainda usando o Slice Strings
print('Geek University'[::-1])
# Pode-se também utilizar o reversed para fazer  Loop For reverso
for n in reversed(range(0, 10)):
    print(n)

#Porem sabemos fazer isso usando o range
for n in range(10, -1, -1):
    print(n)