custoFabrica = float(input("Entre com o custo de Fabrica do Veiculo :-> "))


distribuidor = 0
impostos = 0
if custoFabrica <= 12000:
    distribuidor = 5
    impostos =  0
elif 12001 <= custoFabrica <= 25000:
    distribuidor = 10
    impostos = 15
elif custoFabrica > 25000:
    distribuidor = 15
    impostos = 20

valorFinal = custoFabrica + ((custoFabrica*distribuidor)/100) +((custoFabrica*impostos)/100)

print(f"E o valor final é  :-> {valorFinal:.2f}")

