"""
39) Escreva um programa que leia um número inteiro positivo N e em seguida imprima N linhas do chamado Triângulo de Pascal:

1
1  1
1  2  1
1  3  3  1
1  4  6  4  1
1  5  10 10 5  1
"""

# Programa desenvolvido com base na relação de Stifel, que deve ser a mais prática para se implementar um algoritmo.
# Nessa relação, cada número do triângulo é igual a soma do que está acima e o antecessor do número cima.

# O algoritmo é feito por meio de somente 2 listas, que são calculadas a cada ciclo de repetição:
vetor_aux_1 = [1, 1]
vetor_aux_2 = [1, 1]

# Lista auxiliar para posterior junção através de espaços:
vetor_string = []

# Variável para servir de posição a cada nova inserção de elemento:
posicao_na_linha = 1

# Variável para limitação do número de linhas no decorrer do loop while (é inicializada em 2 pois até a quantidade de 2
# linhas, ainda é feita a impressão "manual"):
cont_linhas = 2

# Entrada da quantidade de linhas desejada:
N = int(input("Digite o número de linhas para impressão do Triângulo de Pascal: "))

# Tratamento de entrada inválida (menor do que 0), em que é feito um loop até que seja inserido um valor maior ou igual a 1:
if N <= 0:
    while N <= 0:
        N = int(input("Por favor, digite uma quantidade válida (maior ou igual a 1): "))

# Impressões manuais até a segunda linha:
if N == 1:
    print("1")
elif N == 2:
    print("1")
    print("1 1")

# Caso contrário,
else:
    print("1")  # Imprime-se a primeira e
    print("1 1")  # segunda linhas
    while cont_linhas < N:  # Seguindo com um loop enquanto a quantidade de linhas impressas for menor do que a solicitada
        vetor_aux_2 = [1, 1]  # Reinicia-se o vetor_aux_2 com os valores das extremidades, que nunca mudam
        posicao_na_linha = 1  # Reinicia-se a variável que serve de referência para a posição na linha atual
        for itera in range(len(vetor_aux_1) - 1):  # Para um iterável no range do último elemento do vetor,
            numero_novo = vetor_aux_1[itera] + vetor_aux_1[
                itera + 1]  # Calcula-se o número novo com base na relação de Stifel, em que o outro vetor auxiliar possui os números necessários
            vetor_aux_2.insert(posicao_na_linha,
                               numero_novo)  # Através do número insert, o número novo é "encaixado" no vetor que está sendo modificado
            posicao_na_linha += 1  # É incrementada a posição na linha para a próxima inserção
        if cont_linhas < N:  # Caso a quantidade de linhas ainda seja menor que N,
            for elemento in vetor_aux_2:  # Para cada elemento no vetor atual
                elemento = str(elemento)  # Transforma-o em string
                vetor_string.append(elemento)  # Para adicionar ao vetor auxiliar de string
            linha = ' '.join(
                vetor_string)  # Associa a uma variável a junção dos elementos do vetor string separados por espaço
            print(linha)  # Imprime-se a linha (string)
            vetor_string.clear()  # Limpeza do vetor de string
            cont_linhas += 1  # Incremento do número de linhas
        # Rotina idêntica, porém com a inversão dos vetores:
        vetor_aux_1 = [1, 1]
        posicao_na_linha = 1
        for itera in range(len(vetor_aux_2) - 1):
            numero_novo = vetor_aux_2[itera] + vetor_aux_2[itera + 1]
            vetor_aux_1.insert(posicao_na_linha, numero_novo)
            posicao_na_linha += 1
        if cont_linhas < N:
            for elemento in vetor_aux_1:
                elemento = str(elemento)
                vetor_string.append(elemento)
            linha = ' '.join(vetor_string)
            print(linha)
            vetor_string.clear()
            cont_linhas += 1
