lado1 = float(input("Digite 1º Lado :-> "))
lado2 = float(input("Digite 2º Lado :-> "))
lado3 = float(input("Digite 3º Lado :-> "))

valida1 = (lado1 < (lado2 + lado3))
valida2 = (lado2 < (lado1 + lado3))
valida3 = (lado3 < (lado1 + lado2))
tipoTriangulo = ""
if valida1 and valida2 and valida3:
    print("Os lados são válidos, pode ser um triangulo ")
    if lado1 == lado2 and lado2 == lado3:
        tipoTriangulo = "Equilátero"
    elif lado1 == lado2 or lado2 == lado3:
        tipoTriangulo = "Isóceles"
    elif lado1 != lado2 and lado2 != lado3:
        tipoTriangulo = "Escaleno"
    else:
        tipoTriangulo = "Que tipo foi esse ?"

    print("E o tipo de triangulo é :-> " + tipoTriangulo)
else:
    print("Dados de lados invalidos, ")