lista = []

valor = 0

while len(lista) < 6 :
    valor = int(input("Entre com um valor :-> "))
    if valor%2 == 0:
        lista.append(valor)


print("=================================================")
print(lista[::-1])