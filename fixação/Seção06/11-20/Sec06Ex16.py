numero = 0
while True:
    numero = int(input(f"Digite o  numero -> "))
    if numero % 2 == 1:
        break
    else:
        print("Digita um Impar, porra !!!")

for i in range(numero, 0, -2):
    print(i)