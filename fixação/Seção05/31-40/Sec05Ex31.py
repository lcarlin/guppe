altura = float(input("Entre com a altura de A Pessoa :-> "))
peso = float(input("Entre com o peso de A Pessoa :-> "))
classificacao = ""

if altura < 1.20:
    if peso < 60:
        classificacao = "A"
    elif 60 <= peso <= 90:
        classificacao = "D"
    elif peso > 90:
        classificacao = "G"
elif altura >= 1.2 and altura <= 1.7:
    if peso < 60:
        classificacao = "B"
    elif 60 <= peso <= 90:
        classificacao = "E"
    elif peso > 90:
        classificacao = "H"
elif altura > 1.7:
    if peso < 60:
        classificacao = "C"
    elif 60 <= peso <= 90:
        classificacao = "F"
    elif peso > 90:
        classificacao = "I"

print("E a classificacao para essa pessoa é :-> " + classificacao)
