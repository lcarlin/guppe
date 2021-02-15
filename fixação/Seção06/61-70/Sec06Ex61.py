final = inicio = soma = 0
while inicio < 100 or inicio > 999:
    inicio = int(input("Entre com o 1 numero  :-> "))
while final < inicio or final > 999:
    final = int(input("Entre com o 2 numero  :-> "))

maior = 0

for i in range(inicio, final + 1):
    for j in range(inicio, final + 1):
        isPalindromo = i * j
        if str(isPalindromo) == str(isPalindromo)[::-1]:
            print(f"Uia : Achei um Palindromo :-> {isPalindromo}")

            if isPalindromo > maior:
                maior = isPalindromo

print("=================================================")

print(f'O maior palíndromo gerado a partir do produto de dois números de três digitos é {maior}')

print("Final de O programas")
