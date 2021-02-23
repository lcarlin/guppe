lista = []

totalNotas = 15

for i in range(totalNotas):
    lista.append(int(input(f"Entre com o numero {i}  :-> ")))


print("=================================================")
media = sum(lista) / totalNotas

print(f"E a média é :-> {media}")