print("Determina se um número n > 0 é primo\n")

# leia o valor de n
n = int(input("Digite o valor de n (n > 0): "))

# n é primo até que se prove o contrário
é_primo = True

# procure por um divisor de n entre 2 e n-1
divisor = 2
while divisor < n and é_primo:  # equivalente a "div... and é_primo == True:"
    if n % divisor == 0:
        é_primo = False
    divisor += 1

if é_primo and n != 1:  # 1 não é primo
    print(n, "é primo")
else:
    print(n, "não é primo")