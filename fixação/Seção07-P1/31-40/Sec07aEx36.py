totalNumeros = 10
vetorInicial = []
print("**********************")

for i in range(totalNumeros):
    vetorInicial.append(int(input(f"Entre com o numero {i}  inteiro para o Vetor :-> ")))

print("=================================================")
print("Vetor Inicial ")
print("=================================================")
vetorInicial.sort()
for j in vetorInicial:
    print(j)

