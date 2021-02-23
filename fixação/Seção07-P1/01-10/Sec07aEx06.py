lista = []
maiorValor = 0
menorValor = 99999999
totalValores = 10

for i in range(totalValores):
    lista.append(int(input(f"Entre com o numero {i}  :-> ")))

maiorValor = max(lista)
menorValor = min(lista)

print("=================================================")
print(f"O Maior numero é {maiorValor}")
print(f"O menor numero é {menorValor}")


