
contador = 1
soma = 0
numero = 0
media =0
while contador <= 10:
    numero = int(input(f"Digite o {contador} º numero -> " ))
    if numero >= 0 :
        soma += numero
        contador += 1
    else:
        print ("Tem que ser positivo . ")

media = soma / 10
print (f"E a soma é :-> {media}")