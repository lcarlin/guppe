totalValores = 10
vetorA = []
vetorB = []
vetorC = list(range(totalValores*2))
for i in range(totalValores):
    print("**********************")
    vetorA.append(int(input(f"Entre com o numero {i + 1} para o Vetor A  :-> ")))
    vetorB.append(int(input(f"Entre com o numero {i + 1} para o Vetor B  :-> ")))

for j in range(0, totalValores * 2, 2):
    vetorC[j] = vetorA[int(j / 2)]
    vetorC[j + 1] = vetorB[int(j / 2)]

print("=================================================")
print(vetorA)
print("=================================================")
print(vetorB)
print("=================================================")
print(vetorC)
