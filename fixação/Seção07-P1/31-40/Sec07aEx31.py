vetorUm = []
vetorDois = []
vetorIntersec = []
totalNumeros = 6

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

# Aqui, pra usar a funcionalidade SET, tem que converter a lista em COnjunto
conjUm = set(vetorUm)
conjDois = set(vetorDois)
conjUnion  = conjUm.union(conjDois)

print("=================================================")
print("E a União dos dois vetores é  ")
print(conjUnion)