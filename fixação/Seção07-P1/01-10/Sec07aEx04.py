lista = []
totalValores = 8
valorX = 0
valorY = 0

for i in range(totalValores):
    lista.append(int(input(f"Entre com o numero {i}  :-> ")))

print("=================================================")
print(lista)
print("=================================================")
valorX = int(input(f"Entre com a Posicao X :-> "))
valorY = int(input(f"Entre com a Posicao Y :-> "))
print("=================================================")
print(f"O Valor encontrado na posicao X é {lista[valorX]} ")
print(f"e o valor          na posicao Y é {lista[valorY]}")
print(f"E a soma dos valores é {lista[valorX] + lista[valorY]  } ")
print("=================================================")