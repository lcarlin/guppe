nota1 = float(input("Digite a 1º nota :-> "))
nota2 = float(input("Digite a 2º nota :-> "))
nota3 = float(input("Digite a 3º nota :-> "))
pesoNota1 = 2
pesoNota2 = 3
pesoNota3 = 5
thrsholdMaior = 10
reprovado = 3
exameFinal = 5
mensagem = ""
if (nota1 >= 0 and nota1 <= thrsholdMaior) and (nota2 >= 0 and nota2 <= thrsholdMaior) and (
        nota3 >= 0 and nota3 <= thrsholdMaior):
    mediaPonderada = ((nota1 * pesoNota1) + (nota2 * pesoNota2) + (nota3 * pesoNota3)) / (pesoNota1 + pesoNota2 + pesoNota3)
    if mediaPonderada < 3:
        mensagem = "Reprovado"
    else:
        if mediaPonderada < 5:
            mensagem = "em Recuperacao"
        else:
            mensagem = "Aprovado, Para-Bens "

    print(f"A media foi {mediaPonderada} e ele esta {mensagem}")
else:
    print("Valores de notas fora do Escopo")
