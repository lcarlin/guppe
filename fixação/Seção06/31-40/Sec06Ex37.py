inicio = 1000
final = 9999
lista = []

for j in range(inicio, final + 1):
    print (j)
    string = str(j)
    baixa = int(string[0:2])
    alta = int(string[2:4])
    valor = (baixa + alta) ** 2
    if valor == j:
        lista.append(j)

print("===========================================")
lista.sort()
print(lista)
