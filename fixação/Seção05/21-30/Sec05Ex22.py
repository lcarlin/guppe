idade = int(input("Digite a idade :-> "))
tempoTrabalho = int(input("Tempo de TRabalho :-> "))

if idade >= 65:
    print ("Ja pode se aposentar por idade")
else:
    if tempoTrabalho > 30:
        print("Ja pode se aposentar por tempo de trabalho")
    else:
        if (idade > 60 ) and (tempoTrabalho > 25):
            print ("Pode ser aposentar pela Idade e pelo Tempo de Trabvalho ")
        else:
            print("Não atendeu aos requisitos ")

print ("EOP")
