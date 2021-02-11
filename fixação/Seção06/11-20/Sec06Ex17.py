numero = 0
soma = 0
while True:
    numero = int(input(f"Digite o  numero -> "))
    if numero > 0:
        break
    else:
        print("Digita uum numero Positivo e maior que zero  !!!")

for i in range(0, numero+1):
    print (i)
    soma += i

print (f"E a soma é :-> {soma}")