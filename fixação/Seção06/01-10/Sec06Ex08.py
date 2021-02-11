
contador = 1
soma = 0
numero = 0
menor = 999
maior = 0
while contador <= 10:
    numero = int(input(f"Digite o {contador} º numero -> " ))
    if numero >= 0 :
        soma += numero
        contador += 1
        if numero > maior :
            maior = numero
        if numero < menor :
            menor = numero
    else:
        print ("Tem que ser positivo . ")

print(f"E o maior é :-> {maior}")
print(f"E o menor é :-> {menor}")