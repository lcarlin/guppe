nota1 = float(input("Digite a 1º nota :-> "))
nota2 = float(input("Digite a 2º nota :-> "))
media = 0

nota1Valida = (nota1 >= 0) and (nota1 <= 10)
nota2Valida = (nota2 >= 0) and (nota2 <= 10)

if nota1Valida and nota2Valida:
    media = (nota1 + nota2) / 2
    print(f"E a média entre a Nota 1 : \"{nota1}\" e a nota 2 \"{nota2}\" é de \"{media}\" ")
else:
    print("Impossivel de se calcular a media")
    if not nota1Valida:
        print(f"A nota 1 \"{nota1}\" não é valida")

    if not nota2Valida:
        print(f"A nota 2 \"{nota1}\" não é valida")
