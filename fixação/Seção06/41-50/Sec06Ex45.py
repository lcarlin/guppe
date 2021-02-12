while True:
    opcao = valor = result  = 0
    print("1 - Converter KM/H -> M/S ")
    print("2 - Converter M/S -> KM/H ")
    print("3 - Sair ")
    while opcao < 1: opcao = int(input("Entre com a Opcao desejada  :-> "))
    if opcao >= 3:
        break

    if opcao == 1:
        valor = float(input("Entre coma velocidade em Km/H  :-> "))
        result = valor / 3.6
    else :
        valor = float(input("Entre coma velocidade em M/S :-> "))
        result = valor * 3.6

    print (f"E o resultado da conversao é -> {result:.2f}")

print("=================================================")
print("Final de O programas")