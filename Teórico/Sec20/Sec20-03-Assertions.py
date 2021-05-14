"""
Seção 20: TEste com Python
    03 - Checagens, qustionamentos, afirmações:
Empyhton utilizamos a plavra reservada Assert para realizar simples afirmações utilizados nnos testes

utilizamos o Assert numa explressão que que queremos checar se é valida ou não
se a explressão for verdadeira, o Assert retorna NONE, caso seja falsa levanta um erro do tipo AssertionError

Podemos especificar opcionalmente um segundo argumento ou mesmo uma mensagem de erro persolnalizada

A Palavra Assert pode ser utilizada em qualquer funcao ou codigo nosso .. não precisa ser exlusivamente nos testes

====================================================================================================================
ALERTA cuidado ao utilzar Asserts -
Se um porgrama Python for executado utilizando o parametro " -o " nenhum assertion será validado , ou seja
todas as suas validações com assertions serão ignoradas
====================================================================================================================
====================================================================================================================
====================================================================================================================
====================================================================================================================
====================================================================================================================
====================================================================================================================
====================================================================================================================
====================================================================================================================
====================================================================================================================
====================================================================================================================
====================================================================================================================
====================================================================================================================
====================================================================================================================
"""
def soma_numeros_positivos(a, b):
    assert a > 0 and b > 0, 'Ambos tem que ser > 0 '
    return a + b

def comer_fast_food(comida):
    assert  comida in ['pizza'
        , 'doces'
        , 'sorvete'
        , 'batata-fritas'
        , 'cachorro-quente'], 'A cominda tem que ser fas food'

    return f'Estou a comer {comida}'

def main():
    print('-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-')
    print(soma_numeros_positivos (1,2))
    print('===========================================================')
    # print(soma_numeros_positivos(-3, 0 ))
    print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    comida = input('informa a comida :-> ')
    print(comer_fast_food(comida))
    print('-----------------------------------------------------------')
    print('***********************************************************')

## e é aqui que a brincadeitra começa
if __name__ == '__main__':
    main()
