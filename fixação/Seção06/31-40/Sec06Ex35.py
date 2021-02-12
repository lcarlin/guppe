valor1 = 0
valor2 = 0
somatoria = 0
while valor1 <= 0: valor1 = int(input("Entre com o 1 numero  :-> "))
while valor2 <= valor1: valor2 = int(input("Entre com o 2 numero  :-> "))
while valor1 <= valor2:
    if (valor1 % 2 != 0):
        somatoria += valor1

    valor1 += 1
    
print(f"Somatoria dos impares no intervalo :-> {somatoria}")
