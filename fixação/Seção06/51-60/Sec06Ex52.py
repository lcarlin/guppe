valorSacar = int(input('Digite o valor a Ser Sacado '))
valorAtual = valorSacar
conta100 = conta50 = conta20 = conta10 = conta5 = conta2 = conta1 = 0
totalNotas = 0
contaTeste = 0
while valorAtual > 0:
    if valorAtual >= 100:
        valorAtual -= 100
        conta100 += 1
    else:
        if valorAtual >= 50:
            valorAtual -= 50
            conta50 += 1
        else:
            if valorAtual >= 20:
                valorAtual -= 20
                conta20 += 1
            else:
                if valorAtual >= 10:
                    valorAtual -= 10
                    conta10 += 1
                else:
                    if valorAtual >= 5:
                        valorAtual -= 5
                        conta5 += 1
                    else:
                        if valorAtual >= 2:
                            valorAtual -= 2
                            conta2 += 1
                        else:
                            if valorAtual >= 1:
                                valorAtual -= 1
                                conta1 += 1

print ("======================================")
print (f"Total de notas para o Valor inteiro {valorSacar}")
print (f"Notas de 100 {conta100}")
print (f"Notas de  50 {conta50}")
print (f"Notas de  20 {conta20}")
print (f"Notas de  10 {conta10}")
print (f"Notas de   5 {conta5}")
print (f"Notas de   2 {conta2}")
print (f"Notas de   1 {conta1}")
print("Final de O programas")
