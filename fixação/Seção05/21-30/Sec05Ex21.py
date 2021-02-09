from switchcase import switch

print("-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-")
print(" Operações :")
print("1 - Soma de 2 numeros ")
print("2 - Diferenca entre 2 numeros (Maior pelo Menor)  ")
print("3 - Produto entre 2 numeros ")
print("4 - Divisao entre 2 numeros (o denominador nao pode ser zero )  ")
operacao = int(input("entre com a Operacao "))
if 0 < operacao < 5:
    print("Talkey - operacaovalida")
    nota1 = float(input("Numero 1 :-> "))
    nota2 = float(input("Numero 2 :-> "))
    resultado = 0
    for case in switch(operacao):
        if case(1):
            resultado = nota1 + nota2
            break
        if case(2):
            if nota1 > nota2:
                resultado = nota1 - nota2
            else:
                resultado = nota2 - nota1
            break
        if case(3):
            resultado = nota1 * nota2
            break
        if case(4):
            if nota2 > 0:
                resultado = nota1 / nota2
            else:
                print ("ERROR - FATAL - FAIL ")
                print("O denominador nao pode ser zero ")
            break

    print("E o resultado da operacao -e :-> " + str(resultado))
else:
    print ("ERROR - FATAL - FAIL : Operacao invalida")
