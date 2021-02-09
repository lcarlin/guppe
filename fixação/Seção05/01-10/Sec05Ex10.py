altura = float(input("Digite a altura da pessoa :-> "))
sexo = str(input("Digite o Sexo da pessoa (M/F) :-> "))
pesoIdeal = 0

if sexo == 'M':
    pesoIdeal = (72.7 * altura ) - 58
elif sexo == 'F':
    pesoIdeal = (62.1 * altura) - 44.7
else:
    print(f"O Sexo {sexo} é invalido. Faca certo ")

if pesoIdeal > 0:
    print(f"E o peso ideal para a pessoa é de {pesoIdeal} ")


