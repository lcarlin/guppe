"""
Média Aritmética Ponderada
A média aritmética ponderada é calculada multiplicando cada valor do conjunto de dados pelo seu peso.

Depois, encontra-se a soma desses valores que será dividida pela soma dos pesos.
"""
def calculaMedia (nota1, nota2, nota3, metodo):
    media = 0
    if metodo.upper() == 'A':
        media =  (nota1+nota2+nota3)/3
    elif metodo.upper() == 'P':
        media = ((nota1*5) + (nota2*3) + (nota3*2))/(5+3+2)

    return  media



valor1 = int(input("Entre com o 1º nota :-> "))
valor2 = int(input("Entre com o 2º nota :-> "))
valor3 = int(input("Entre com o 3º nota :-> "))
tipo = input("Entre com o tipo de calculo  A/P :-> ")

result = calculaMedia(valor1, valor2,valor3, tipo)

print(f'E a media calculada é :-> {result}')