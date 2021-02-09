from switchcase import switch

print("-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-")
print(" Operações de Médias  :")
print("1 - Geométrica")
print("2 - Ponderada ")
print("3 - Harmônica ")
print("4 - Aritmética ")
operacao = int(input("entre com a Operacao "))
print("")
valorX = int(input("entre com Valor A :-> "))
valorY = int(input("entre com Valor B :-> "))
valorZ = int(input("entre com Valor C :-> "))
resultado = 0
for case in switch(operacao):
    if case(1):
        resultado = (valorX*valorY*valorZ) **(1/3)
        break
    if case(2):
        resultado =  (valorX + 2 + valorY + 3 + valorZ) / 6
        break
    if case(3):
        resultado = 1 / (1/valorY)+(1/valorY) + (1/valorZ)
        break
    if case(4):
        resultado = (valorX + valorY + valorZ) / 3
        break
else:
    print( "Operacao Iválida")

print(f"E o resultado é {resultado} " )
