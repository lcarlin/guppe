from switchcase import switch

opcao = 0

while opcao < 5:
    print("-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-")
    print("Uma pequena calculadora rudimentar")
    print(" ")
    print(" Menu de Operações :")
    print("1 - Soma ")
    print("2 - Subtração ")
    print("3 - divisão ")
    print("4 - multiplicacao ")
    print("5 - Sair ")
    while opcao == 0 or opcao > 5:
        opcao = int(input("entre com a Operacao :-> "))
    print("Talkey - operacaovalida")
    if opcao == 5 :
        break
        
    numero1 = float(input("Numero 1 :-> "))
    numero2 = float(input("Numero 2 :-> "))
    resultado = 0
    msg = ""
    for case in switch(opcao):
        if case(1):
            resultado = numero1 + numero2
            msg = "Soma"
            break
        if case(2):
            resultado = numero1 - numero2
            msg = "Subtracao"
            break
        if case(3):
            resultado = numero1 / numero2
            msg = "Divisao"
            break
        if case(4):
            resultado = numero1 * numero2
            msg = "Multiplicacao"
            break
        else:
            pass
    opcao = 0 
    print(f"E o Resultado da {msg} é :-> {resultado:.2f}")

print("=================================================")
print("Final de O programas")
