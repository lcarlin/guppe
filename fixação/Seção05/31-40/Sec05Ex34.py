nota = float(input("Entre com a nota de A Pessoa :-> "))
faltas = int(input("Entre com as faltas da pessoa:-> "))

if nota >= 9 and nota <= 10 :
    if faltas <= 20:
        conceito = "A"
    else:
        conceito = "B"
elif nota >= 7.5 and nota < 9:
    if faltas <= 20:
        conceito = "B"
    else:
        conceito = "C"
elif nota >= 5 and nota < 7.5:
    if faltas <= 20:
        conceito = "C"
    else:
        conceito = "D"
elif nota >= 4 and nota < 5:
    if faltas <= 20:
        conceito = "D"
    else:
        conceito = "E"
elif nota >= 0 and nota < 3.9:
    if faltas <= 20:
        conceito = "E"
    else:
        conceito = "E"

print("Diante dos dados apresentados, o conceito é :-> " + conceito)