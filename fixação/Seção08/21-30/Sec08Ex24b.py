'Ex24'
print('Este programa recebe um inteiro n e retorna um triângulo vertical de base 2n - 1 e altura n.')


def linha_vazio(lista, m):  # função para incluir m caracteres em branco no início de lista
    for _ in range(m, 0, -1):
        lista.insert(0, ' ')

    return ''.join(lista)


def triang(n):
    for i in range(1, n + 1):
        entrada = ['*'] * (2 * i - 1)  # há 2i - 1 '*'s na i-ésima linha, caracterizada por uma lista chamada 'entrada'

        print(linha_vazio(entrada, n - i))  # há n - i espaços vazios na i-ésima linha, dado n


x = int(input('Número: '))

if x > 0:
    print('')
    triang(x)
else:
    print('Número inválido.')