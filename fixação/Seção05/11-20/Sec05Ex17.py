baseMaior = float(input("entre com a base Maior:-> "))
baseMenor = float(input("entre com a Base Menor :-> "))
altura = float(input("entre com a Altura :-> "))

if baseMenor > 0 and baseMaior > 0 and altura > 0:
    area = ((baseMenor + baseMaior)* altura)/2
    print("E o valor da área do Trapezio :-> " + str(area))