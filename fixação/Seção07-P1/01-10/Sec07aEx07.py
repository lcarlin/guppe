lista = []
maiorValor = 0

totalValores = 10

for i in range(totalValores):
    lista.append(int(input(f"Entre com o numero {i}  :-> ")))

maiorValor = max(lista)
posicao = lista.index(maiorValor)
print("=================================================")
print(f"O Maior numero é :-> {maiorValor}")
print(f"E a posicao    é :-> {posicao}")
