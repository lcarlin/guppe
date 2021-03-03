lista = []
totalValores = 50
for i in range(totalValores):
    lista.append((i + 5 * i) % (i + 1))

print("=================================================")
print(lista)