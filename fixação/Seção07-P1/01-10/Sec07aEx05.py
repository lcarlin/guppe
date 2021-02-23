lista = []
listaPar = []
totalValores = 10
totalPares = 0


for i in range(totalValores):
    lista.append(int(input(f"Entre com o numero {i}  :-> ")))
    if lista[i] %2 == 0 :
        listaPar.append(lista[i])
        totalPares += 1

print("=================================================")
print(f"A quantidade de numeros pares é {totalPares}")
print(listaPar)