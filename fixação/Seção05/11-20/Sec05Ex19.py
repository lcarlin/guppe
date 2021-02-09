num1 = int(input("Digite um numero qualquer  :-> "))
dividePor3 = ((num1 % 3) == 0)
dividePor5 = ((num1 % 5) == 0)

if dividePor3 ^ dividePor5:
    print("O numero É dividido por 5 OU por 3 mas não ambos")
    if dividePor3:
        print("É divisivel por 3")
    else:
        print("É divisivel por 5")
else:
    if dividePor3 and dividePor5:
        print("é divisivel por 3 e 5 o mesmo tempo")
    else:
        print("Ele não é dividido nem por 3 nem por 5")

