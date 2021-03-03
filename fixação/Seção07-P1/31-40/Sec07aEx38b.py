totalNumeros = 10
vetorInicial = []
print("**********************")
# Agora usando o BubbleSort na medida em que se inserimos os valores
# Na boa , isso não é performatico 
for i in range(totalNumeros):
    numero = int(input(f"Entre com o numero {i}  inteiro para o Vetor :-> "))
    vetorInicial.append()
    for j in range(len(vetorInicial)):
        if vetorInicial[j] > vetorInicial[j+1]:
            tmp = vetorInicial[j]
            vetorInicial[j] = vetorInicial[j+1]
            vetorInicial[j+1] = tmp

print("=================================================")
print("Vetor Inicial ")
print("=================================================")

for j in vetorInicial:
    print(j)

