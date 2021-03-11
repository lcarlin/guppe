def qualEhOMaior(num1, num2):
    if num1 > num2:
        print(f'O Numero 1 {num1} é Maior que o numero 2 {num2}')
    elif num2 > num1:
        print(f'O Numero 2 {num2} é Maior que o numero 1 {num1}')
    else:
        print(f'Os numeros {num1} e {num2} são iguais ')



valor1 = int(input("Entre com o 1º numero :-> "))
valor2 = int(input("Entre com o 2º numero :-> "))

qualEhOMaior(valor1, valor2)