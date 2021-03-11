def verificaNumero (valor):
    if valor > 0 :
        return 1
    elif valor < 0 :
        return -1
    return 0

numero =  int(input("Entre com o 1 numero  :-> "))

print(verificaNumero(numero))