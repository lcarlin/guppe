vetInicial = []
vetorPar = []
vetorImpar = []
totalNumeros = 6

# Faze 01 - ler os 10 numeros;
for n in range(totalNumeros):
    numero = 0
    while numero <= 0: numero = int(input(f"Entre com o numero {n + 1}  inteiro e maior que Zero  :-> "))
    vetInicial.append(numero)
    """
    Se quiser jáfazer otimizado, aproveitiando o Loop e as comparações, faz aaqui ó
    if numero%2 == 0 :
        vetorPar.append(numero)
    else:
        vetorImpar.append(numero)
"""
vetorPar = [i for i in vetInicial if i % 2 == 0] # Tecnica ninja pra preencher um vetor com base num If
vetorImpar = [i for i in vetInicial if i % 2 != 0]
print("=================================================")
print("Vetor de Pares ")
print(vetorPar)
print(f'E a soma dos numeros PARES é :-> {sum(vetorPar)}')
print("=================================================")
print("Vetor de imPares ")
print(vetorImpar)
print(f'E a soma dos numeros imPARES é :-> {sum(vetorImpar)}')