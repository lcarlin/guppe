from random import randint
counter = 0
continua = True
aleatorio = randint(1, 1001)
print(aleatorio)
print("=================================================")
while continua :
    numero = int(input('Adivinhe o numero aleatório! \n Digite um numero  '))
    if numero == aleatorio:
        print("PArabéns, você acertou !")
        print(f" Você conseguiu adivinhar em {counter} tentativas")
        continua =  False
    else:
        print("Tente outra vez!")
        counter += 1

print("=================================================")
print("Final de O programas")