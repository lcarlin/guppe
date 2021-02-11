contador = 1
valor1 = int(input("Entre com o 1 numero  :-> "))
while True:
    multi11 = valor1%11 == 0
    multi13 = valor1%13 == 0
    multi17 = valor1%17 == 0
    if multi11 or multi13 or multi17:
        print(f"O Numero {valor1} é um multiplo de 11 {multi11} ; 13 {multi13} ; 17 {multi17}")
        break

    valor1 += 1