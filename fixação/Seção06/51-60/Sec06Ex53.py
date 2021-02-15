valor = int(input('Digite o valor para o Triangulo: '))
linhaAtual = 1
counter = 1
qtdPorLInha = 1

while linhaAtual <= valor:
    for i in range (1,qtdPorLInha  + 1 ):
        print(f"{counter} " ,end="")
        counter += 1

    print("")
    qtdPorLInha += 1
    linhaAtual += 1
