totalNumeros = 10
vetorInicial = []
print("**********************")

for i in range(totalNumeros):
    numero = 0
    while numero in vetorInicial: numero = int(input(f"Entre com o numero {i}  inteiro para o Vetor :-> "))

    vetorInicial.append(numero)


print("=================================================")
print("Vetor Inicial ")
print(vetorInicial)