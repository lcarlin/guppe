
def validarLados (l1, l2, l3 ):
    valida1 = (lado1 < (lado2 + lado3))
    valida2 = (lado2 < (lado1 + lado3))
    valida3 = (lado3 < (lado1 + lado2))
    return valida1 and valida2 and valida3

def deternimaTipo (l1, l2, l3 ):
    tipoTriangulo = ""
    if l1 == l2 and l2 == l3:
        tipoTriangulo = "Equilátero"
    elif ( l1 == l2 and l1 != l3)  or ( l2 == l3 and l2 != l1) or ( l1 == l3 and l3 != l2 ):
        tipoTriangulo = "Isóceles"
    elif lado1 != lado2 and lado2 != lado3:
        tipoTriangulo = "Escaleno"
    else:
        tipoTriangulo = "Que tipo foi esse ?"
    return "E o tipo de triangulo é :-> " + tipoTriangulo

lado1 = float(input("Digite 1º Lado :-> "))
lado2 = float(input("Digite 2º Lado :-> "))
lado3 = float(input("Digite 3º Lado :-> "))
if validarLados(lado1, lado2, lado3):
    print("Os lados são válidos, pode ser um triangulo ")
    print(deternimaTipo(lado1, lado2, lado3))
else:
    print("Dados de lados invalidos, ")