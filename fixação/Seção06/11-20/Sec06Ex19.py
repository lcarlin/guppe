numero = 0
while True:
    numero = int(input(f"Digite um numero entre 100 e 999 -> "))
    if 100 <= numero <= 999:
        break
    else:
        print("Digite um numero nointervalo  !!!")

cadeia = str(numero)

for i in range (0,len(cadeia) ):
    print(cadeia[i])