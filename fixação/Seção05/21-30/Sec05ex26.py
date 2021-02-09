distancia = float(input("Distancia Percorrida :-> "))
litros = float(input("Quantidade de litros :-> "))
consumo = (distancia / litros)
msg = ""
if consumo < 8:
    msg = "Venda essa merda"
elif (consumo >= 8) and (consumo <= 14):
    msg = "Carrinho economico, continua"
else:
    msg = " esso non exciste"

print(f"E o consumo foi de {consumo} ; veredito: {msg}")
