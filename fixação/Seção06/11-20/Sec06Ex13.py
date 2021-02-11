while True:
    numero = int(input(f"Digite o  numero -> "))
    if numero%2 == 0:
        break
    else:
        print ("Digita um par, porra !!!")

for i in range (0,numero +1, 2 ):
    print (i)