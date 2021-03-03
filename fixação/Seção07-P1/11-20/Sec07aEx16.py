vetor = []
for i in range(1, 6):
    vetor.append(int(input(f"Informe valor {i} para o vetor :-> ")))
print("**********************")
codigo = int(input("Informe um codigo : "))

if codigo == 1:
    print(vetor)
elif codigo == 2:
    vetor.reverse()
    print(vetor)
elif codigo == 0:
    print("Nada a se fazer")
else:
    print("Codigo Invalido ")
