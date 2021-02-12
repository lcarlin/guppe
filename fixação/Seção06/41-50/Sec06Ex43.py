soma = 0
contador = 0
while True:
    numero = int(input(f"Entre com a {contador+1}º idade :-> "))
    if numero <= 0:
        break

    soma += numero
    contador += 1

print("=================================================")
print(f" E a média das idades é {soma/contador} ")
print("Final de O programas")
