totalValores = 10
vetorA = []
vetorB = []
vetorC = []
for i in range(totalValores):
    print("**********************")
    vetorA.append(int(input(f"Entre com o numero {i + 1} para o Vetor A  :-> ")))
    vetorB.append(int(input(f"Entre com o numero {i + 1} para o Vetor B  :-> ")))
    vetorC.append(vetorA[i] - vetorB[i])

print("=================================================")
print(vetorA)
print("=================================================")
print(vetorB)
print("=================================================")
print(vetorC)