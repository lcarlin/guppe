totalNumeros = 15
vetorInicial = []
vetorFinal = []

print("**********************")

for n in range(totalNumeros):
    vetorInicial.append(int(input(f"Entre com o numero {n + 1}  inteiro para o Vetor :-> ")))

vetorFinal = vetorInicial.copy()
for i in range (len(vetorFinal)):
    if vetorFinal[i] == 0:
        retirado = vetorFinal.pop(i+1) # retira o elemento à frente do elemento zero
        vetorFinal.append(retirado)  # move o elemento retirado para o final do Vetor ( ? )

print("=================================================")
print("Vetor Inicial ")
print(vetorInicial)
print("**********************")
print("Vetor Final ")
print(vetorFinal)
