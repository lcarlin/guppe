lista = []
totalValores = 10

for i in range(totalValores):
    lista.append(int(input(f"Entre com o numero {i+1}  :-> ")))

print("=================================================")
print(lista)

for chave, valor in enumerate(lista):
    if valor < 0:
        lista[chave] = 0

print("=================================================")
print(lista)
