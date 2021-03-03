totalNumeros = 10
vetorInicial = []
print("**********************")

for i in range(totalNumeros):
    vetorInicial.append(int(input(f"Entre com o numero {i}  inteiro para o Vetor :-> ")))
    vetorInicial.sort()

print("=================================================")
print("Vetor Inicial ")
print("=================================================")

for j in vetorInicial:
    print(j)

