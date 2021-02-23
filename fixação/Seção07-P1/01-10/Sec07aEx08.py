lista = []

totalValores = 10

for i in range(totalValores):
    lista.append(int(input(f"Entre com o numero {i}  :-> ")))


print("=================================================")
print(lista[::-1])