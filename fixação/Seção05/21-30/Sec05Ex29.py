from random import randint

vezes = 5
while vezes > 0 :
    resultadoDigitado = 0
    numero1 = randint(1, 100)
    numero2 = randint(1, 100)
    resultado = numero1 + numero2
    print(f"Primeiro Numero :-> {numero1}")
    print(f"Segundo  Numero :-> {numero2}")
    resultadoDigitado = int(input("Digite a soma dos dois numeros acima :-> "))
    if resultado == resultadoDigitado:
        print("Parabéns, vc Acerto ")
    else:
        print(f"Tente Outra vez ")

    vezes = vezes - 1
    print(f"Tentativas restantes :-> {vezes}")
