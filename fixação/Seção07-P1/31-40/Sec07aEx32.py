vetorUm = []
vetorDois = []
vetorIntersec = []
vetorSoma = []
vetorMult = []
vetorDif = []
totalNumeros = 5

for n in range(totalNumeros):
    print("**********************")
    numero = 0
    while numero <= 0: numero = int(
        input(f"Entre com o numero {n + 1}  inteiro e maior que Zero para o Vetor 01   :-> "))
    vetorUm.append(numero)

    numero = 0
    while numero <= 0: numero = int(
        input(f"Entre com o numero {n + 1}  inteiro e maior que Zero para o Vetor 02   :-> "))
    vetorDois.append(numero)

    vetorSoma.append(vetorUm[n] + vetorDois[n])
    vetorMult.append(vetorUm[n] * vetorDois[n])
    # vetorDif.append(vetorUm[n] - vetorDois[n])

conjUm = set(vetorUm)
conjDois = set(vetorDois)
confDiff = conjUm.difference(conjDois)
conjIntersect = conjUm.intersection(conjDois)
conjUnion = conjUm.union(conjDois)

print("=================================================")
print('O Vetor soma resultante ')
print(vetorSoma)

print("**********************")
print('O Vetor multiplicacao resultante ')
print(vetorMult)

print("**********************")
print('O Vetor Difereça resultante ')
print(confDiff)

print("**********************")
print('O Vetor Intersecção resultante ')
print(conjIntersect)

print("**********************")
print('O Vetor União resultante ')
print(conjUnion)

print("**********************")