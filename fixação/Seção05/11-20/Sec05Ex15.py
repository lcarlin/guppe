from switchcase import switch


num1 = int(input("Digite o numedo do dia da semana  :-> "))
diaDaSemana= ""
if num1 > 1 and num1 < 8 :
    for case in switch(num1):
        if case(1):
            diaDaSemana = "Domingo"
            break
        if case(2):
            diaDaSemana = "Segunda-feira"
            break
        if case(3):
            diaDaSemana = "Terça-feira"
            break
        if case(4):
            diaDaSemana = "Quarta-feira"
            break
        if case(5):
            diaDaSemana = "Quinta-Feira"
            break
        if case(6):
            diaDaSemana = "Sexta-Feira"
            break
        if case(7):
            diaDaSemana = "Sabado."
            break
        
    
    print ("E o dia da semana é :-> " + diaDaSemana)
else:
    print ("Valor fora do escopo ")
