def calculaConsumo(distancia, litros):
    consumo = (distancia / litros)
    msg = ""
    if consumo < 8:
        msg = "Venda essa merda"
    elif (consumo >= 8) and (consumo <= 14):
        msg = "Carrinho economico, continua"
    else:
        msg = " esso non exciste"

    return f"E o consumo foi de {consumo} ; veredito: {msg}"


lonjura = float(input("Distancia Percorrida :-> "))
gazoza = float(input("Quantidade de litros :-> "))
print(calculaConsumo(lonjura, gazoza))
