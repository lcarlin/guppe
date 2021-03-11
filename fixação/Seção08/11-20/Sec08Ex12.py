def somaPartes(numero):
    matriz = str(num1)
    soma = 0
    tamanhoString = matriz.__len__()
    index = 0
    while index < tamanhoString:
        print(matriz[index])
        soma = soma + int(matriz[index])
        index = index + 1
    return soma


num1 = int(input("Digite o  Numero :-> "))
if num1 <= 0:
    print("Numero invalido")
else:
    valor = somaPartes(num1)
    print("E a soma dos digitos é de :-> " + str(valor))
