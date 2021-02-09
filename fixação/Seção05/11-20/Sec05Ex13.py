nota1 = float(input("Digite a 1º nota :-> "))
nota2 = float(input("Digite a 2º nota :-> "))
nota3 = float(input("Digite a 3º nota :-> "))
if (nota1 >=0 and nota1 <=100) and (nota2 >=0 and nota2 <=100)  and (nota3 >=0 and nota3 <=100):
    mediaPonderada = ((nota1 * 1 ) + ( nota2 * 1 ) + (nota3 * 2) )/ (1 + 1 + 2)
    if mediaPonderada >= 60:
        print (f"A media foi {mediaPonderada} e ele esta aprovado" )
    else:
        print(f"A media foi {mediaPonderada} e ele esta reprovado")
else:
    print ("Valores de notas fora do Escopo")