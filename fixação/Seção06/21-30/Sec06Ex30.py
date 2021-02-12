contador = 1
valor1 = 0
while valor1 <= 0: valor1 = int(input("Entre com o 1 numero  :-> "))
soma1 = 0
soma2 = 0
soma3 = 0

for i in range(1, valor1 + 1):
    soma1 += i

for j in range(1, 2 * valor1):
    print (j)
    if (j % 2 == 0):  # É PAR, então subtrai
        j *= -1
    else:  # é IMPAR, então soma
        soma3 += j

    soma2 += j

print(f"E o resultado da 1ª Soma é :-> {soma1}")
print(f"E o resultado da 2ª Soma é :-> {soma2}")
print(f"E o resultado da 3ª Soma é :-> {soma3}")
