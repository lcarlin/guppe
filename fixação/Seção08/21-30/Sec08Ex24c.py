def triangulo_vertical(altura=6):
    cont_espaco = 0
    base = 2 * altura + 1

    # Como sabemos que o triângulo sempre aumentará em 2, o número de
    # asteriscos da linha seguinte, defini o incremento do for
    # no valor 2
    for i in range(1, base, 2):
        # Fórmula para determinar a quantidade de espaços
        # inseridos em cada linha, que será o valor altura
        # menos o valor atual de cont_espaco
        espacamento = altura - cont_espaco

        # Imprimindo os espaços, mas sem avançar a linha
        print(' ' * espacamento, end='')
        # Imprimindo os asteriscos da linha atual
        print('*' * i)
        # Incrementando o cont_espaço para a próxima linha
        # ter menos espaços
        cont_espaco += 1


print(triangulo_vertical())
