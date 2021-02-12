numero = quadrado = cubo = raiz = 0

while True:

    numero = int(input("Entre com o 1 numero  :-> "))
    if numero <= 0:
        break
    quadrado = numero ** 2
    cubo = numero ** 3
    raiz = numero ** (1 / 2)
    print(f"Quadrado :-> {quadrado}")
    print(f"Cubo     :-> {cubo}")
    print(f"raix     :-> {raiz}")

    print("=================================================")

print("Final de O programas")
