"""
LIstas Aninhadas (nESTED lISTS)
    *   Algumas linguagens de programação possuem uma estrutura de dados chamadas de Arrys:
        - Unidimensionais (Array/VEtores)
        - Multidimensionais (matrizes)
    *   Em python NAO EXISTE ARRAY, MATRIZES apenas LISTAS
====================================================================================================================
print("=================================================")
listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Analogo à uma Matriz 3x3
print(listas)
print(type(listas))
# Como fazemos para cessar os ados ?
print(listas[0])
print(listas[0][1])
print("=================================================")
for lista in listas:
    # cprint(lista)
    for numero in lista:
        print(numero)
print("=================================================")
[[print(valor) for valor in lista] for lista in listas]
====================================================================================================================

"""
#


# Gerando um Tabuleiro/Matriz 3x3
tabuleiro = [[numero for numero in range(1, 4)] for valor in range(1, 4)]
print(tabuleiro)

# Gerando jogaddas pro jogo da velha
velha = [['X' if numero % 2 == 0 else 'O' for numero in range(1, 4)] for valor in range(1, 4)]
print(velha)

# Gerando valores 9niciais
print([['*' for i in range(1, 4)] for j in range(1, 4)])
