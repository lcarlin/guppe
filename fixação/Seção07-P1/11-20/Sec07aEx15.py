lista = []
totalValores = 20

for i in range(totalValores):
    lista.append(int(input(f"Entre com o numero {i}  :-> ")))

semRepetidos = set(lista)
print("=================================================")
print(lista)
print(semRepetidos)
print("=================================================")
print("EOP ")