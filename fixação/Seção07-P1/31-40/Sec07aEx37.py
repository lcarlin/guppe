print('----------')
print('Questão 37')
lista = [1, 2, 345, 1, 0, 12, 0, 12, 5, 7, 0, 3, 0]
lista.sort()
a1 = (lista[0:5]).copy()
lista.sort(reverse=True)
a1.extend(lista[0:5])
print(a1)