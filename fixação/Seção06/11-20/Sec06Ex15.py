while True:
    numero = int(input(f"Digite o  numero -> "))
    if numero%2 == 1:
        break
    else:
        print ("Digita um IMpar, porra !!!")

for i in range (0,numero +1, 2 ):
    print (i)