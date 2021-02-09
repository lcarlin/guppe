from switchcase import switch

def mesesAno(mes):
    for case in switch(mes):
        if case(1):
            mesDoAno = "Janeiro"
            break
        if case(2):
            mesDoAno = "Fevereiro"
            break
        if case(3):
            mesDoAno = "Março"
            break
        if case(4):
            mesDoAno = "Abril"
            break
        if case(5):
            mesDoAno = "Maio"
            break
        if case(6):
            mesDoAno = "Junho"
            break
        if case(7):
            mesDoAno = "Julho"
            break
        if case(8):
            mesDoAno = "Agosto"
            break
        if case(9):
            mesDoAno = "Setembro"
            break
        if case(10):
            mesDoAno = "Outubro"
            break
        if case(11):
            mesDoAno = "Novembro"
            break
        if case(12):
            mesDoAno = "Dezembro"
            break

    return mesDoAno


mes = int(input("Digite o numero de O Mes :-> "))

if 1 < mes < 13:
    print("E o mes é :-> " + mesesAno(mes))
else:
    print("Valor fora do escopo ")
