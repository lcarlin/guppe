lista = []
totalValores = 10
listaNova = []
for i in range(totalValores):
    numero = -1
    while numero < 0 or numero > 50:
        numero = int(input(f"Entre com o numero {i + 1}  :-> "))

    lista.append(numero)

    if numero % 2 != 0:
        listaNova.append(numero)

print("=================================================")
print(lista)
print(listaNova)

print("=================================================")
for k in range(0, totalValores - 1):

    if k < len(listaNova):
        msg = str(listaNova[k])
    else:
        msg = "-"

    String = str(k) + " -> " + str(lista[k]) + " | " + msg

    print(String)
