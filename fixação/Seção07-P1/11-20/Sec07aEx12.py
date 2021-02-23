lista = []
maiorValor = 0
menorValor = 0
soma = 0
totalValores = 5

for i in range(totalValores):
    lista.append(int(input(f"Entre com o numero {i}  :-> ")))

maiorValor = max(lista)
menorValor = min(lista)
soma = sum(lista)
media = soma / totalValores

print("=================================================")
print(lista)

print("=================================================")
print(f"O Maior numero é    :=-> {maiorValor}")
print(f"O menor numero é    :=-> {menorValor}")
print(f"A soma dos numeros  :=-> {soma}")
print(f"A Media dos numeros :=-> {media}")


print("=================================================")
print("EOP ")
