soma = 0
contador = 1

while contador < 1000:
    if ( (contador%3 == 0 ) or (contador%5== 0 )):
        soma += contador

    contador += 1


print (f"E a soma de multiplos de 3 ou 5 é {soma}")