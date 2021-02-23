lista = []
lista2 = []
for i in range(10):
    lista.append(int(input(f"Entre com o numero {i + 1}  :-> ")))
    lista2.append(lista[i] ** 2)

print(lista)
print(lista2)
