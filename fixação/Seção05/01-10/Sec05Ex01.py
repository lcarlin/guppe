num1 = int(input("Digite o 1º Numero :-> "))
num2 = int(input("Digite o 2º numero :-> "))

if num1 > num2:
    print(f"O Numero {num1}  é maior que o {num2} ")
else:
    if num2 > num1:
        print(f"O Numero {num2}  é maior que o {num1} ")
    else:
        print("Os numeros são iguais !!!")
