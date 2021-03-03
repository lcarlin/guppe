totalValores = 5
vetorA = []
vetorB = []
produtoEscalar = 0

for i in range(totalValores):
    print("**********************")
    vetorA.append(int(input(f"Entre com o numero {i + 1} para o Vetor A  :-> ")))
    vetorB.append(int(input(f"Entre com o numero {i + 1} para o Vetor B  :-> ")))
    produtoEscalar += (vetorA[i] * vetorB[i])

print("=================================================")
print(vetorA)
print("=================================================")
print(vetorB)
print("=================================================")
print(produtoEscalar)
