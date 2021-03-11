def operacoes (num1, num2, opera):
    result = 0
    if opera == '+':
        result = num1 + num2
    elif opera == '-':
        result = num1 - num2
    elif opera == '*':
        result = num1 * num2
    elif opera == '/':
        result = num1 / num2
    return  result

valor1 = int(input("Digite o 1º Numero :-> "))
valor2 = int(input("Digite o 2º Numero :-> "))
trabalho = input('Entre com a Operacao desejada: \n + :-> Adição\n - :-> Subtração\n * :-> Multiplicacao\n \ :-> Divisao\n')

print(operacoes(valor1, valor2, trabalho))
