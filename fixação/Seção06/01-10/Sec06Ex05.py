
contador = 1
soma = 0
numero = 0
while contador <= 10:
    numero = int(input(f"Digite o {contador} º numero -> " ))
    soma += numero
    contador += 1

print (f"E a soma é :-> {soma}")