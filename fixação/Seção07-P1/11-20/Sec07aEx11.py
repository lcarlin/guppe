lista = []

totalNotas = 10
qtdNeg = 0
somaPositivo = 0

for i in range(totalNotas):
    lista.append(int(input(f"Entre com o numero {i}  :-> ")))

for num in lista:
    if num > 0:
        somaPositivo += num
    elif num <= 0 :
        qtdNeg += 1


print("=================================================")
print(lista)
print(f"SOma dos positivos :-> {somaPositivo}")
print(f"Quantidade Neghativos :-> {qtdNeg}")

print("=================================================")
print("EOP ")