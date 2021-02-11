numero = int(input(f"Digite o  numero -> "))
contador = numero
while True:
    if contador%2 != 0 :
        print (f"O numero {contador} é Primo !")

    contador += 1
    if contador > (numero*2 ) :
        break

