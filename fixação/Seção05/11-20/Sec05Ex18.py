from switchcase import switch

print("-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-")
print(" Uma pequena calculadora rudimentar")
print(" ")
print(" Operações :")
print("a - Soma ")
print("b - Subtração ")
print("c - divisão ")
print("d - multiplicacao ")
operacao = str(input("entre com a Operacao "))
if '`' < operacao < 'e':
    print("Talkey - operacaovalida")
    nota1 = float(input("Numero 1 :-> "))
    nota2 = float(input("Numero 2 :-> "))
    resultado = 0
    for case in switch(operacao):
        if case("a"):
            resultado = nota1 + nota2
            break
        if case("b"):
            resultado = nota1 - nota2
            break
        if case("c"):
            resultado = nota1 / nota2
            break
        if case("d"):
            resultado = nota1 * nota2
            break

    print("E o resultado da operacao -e :-> " + str(resultado))
else:
    print ("ERROR - FATAL - FAIL : Operacao invalida")
