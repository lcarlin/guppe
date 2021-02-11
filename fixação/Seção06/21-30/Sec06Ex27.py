contador = 1
valor1 = 0
while valor1 <= 0: valor1 = int(input("Entre com o 1 numero  :-> "))
somaHarmonica = 0
while contador <= valor1:
    somaHarmonica += (1 / contador)
    contador += 1

print(f"E a soma Harmonica de {valor1} é {somaHarmonica:.4f}")
