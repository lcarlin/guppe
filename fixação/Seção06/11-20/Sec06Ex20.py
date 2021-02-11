valorDigitado = 0
while True:
    valorDigitado = int(input(f"Digite um valorDigitado pra testar-> "))
    if valorDigitado == 1000:
        print("Saindo ... .. . ")
        break
    else:
        if valorDigitado%2 == 0:
            print(f"O Numer  {valorDigitado} par ")
        else:
            print(f"O Numer  {valorDigitado} IMpar ")

