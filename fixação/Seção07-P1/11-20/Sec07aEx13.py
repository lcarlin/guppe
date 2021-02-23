lista = []
maiorValor = 0
menorValor = 0
soma = 0
totalValores = 5

for i in range(totalValores):
    lista.append(int(input(f"Entre com o numero {i}  :-> ")))

maiorValor = max(lista)
menorValor = min(lista)

posMax = lista.index(maiorValor)
posMin = lista.index(menorValor)

print("=================================================")
print(lista)

print("=================================================")
print(f"O Maior numero é      :=-> {maiorValor}")
print(f"O menor numero é      :=-> {menorValor}")
print(f"A posição do Maior é  :=-> {posMax}")
print(f"A posição do Menor é  :=-> {posMin}")

print("=================================================")
print("EOP ")