from random import randint

tentativas = 0
while tentativas <= 0: tentativas = int(input("Entre com o numero de vezes  :-> "))
while tentativas > 0:
    dado1 = randint(1, 6)
    dado2 = randint(1, 6)

    print(f"E o resultado do dado 1 é :-> {dado1}")
    print(f"E o resultado do dado 2 é :-> {dado2}")
    if dado1 > 1:
        print("O resultado do dado 1 é Maior que o do dado 2 ")
    elif dado1 == dado2:
        print("O resultado do dado 1 é igual ao  dado 2 ")
    else:
        print("O resultado do dado 1 é Menor  que o do dado 2 ")

    tentativas -= 1
    print("=================================================")
    empty = input("Tecle enter pra continuar")
