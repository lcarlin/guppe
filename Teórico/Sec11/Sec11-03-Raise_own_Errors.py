"""
Levantando proproios errors com Raise
raise -> Lança Excessoes
OPBS: não é uma função, é uma palavra reservada assim como def ou quyalquer outra em python
Para simpliuficar, pense no raise ocmo util para criar nossas proxias excessoes e mensagens de erro
A forma geral de utilização é :
raise TipoDoErro('Mensagem de erro')
====================================================================================================================
# Exemplo reqal
def colore(texto, cor):
    if type(texto) is not str:
        raise TypeError('texto precisa ser uma estrigue')
    if type(cor) is not str:
        raise TypeError('cor precisa ser uma estingue')
    print(f'O Texto {texto} será impresso na cor {cor}')

colore('Azzul',1 )

    raise TypeError('cor precisa ser uma estingue')
TypeError: cor precisa ser uma estingue

Process finished with exit code 1

====================================================================================================================

def colore(texto, cor):
    cores = ('vermelho', 'azul', 'verde', ',branco','amarelo')
    if type(texto) is not str:
        raise TypeError('texto precisa ser uma estrigue')
    if type(cor) is not str:
        raise TypeError('cor precisa ser uma estingue')
    if cor not in cores:
        raise ValueError(f'Tipo invalido de core. PErmitidos :-> {cores}')
    print(f'O Texto {texto} será impresso na cor {cor}')

colore('Azzul','tres' )

====================================================================================================================
O Raise, assim como o return, finaliza a funçao, ou seja, nada apos o raise é executado
====================================================================================================================
"""
def colore(texto, cor):
    cores = ('vermelho', 'azul', 'verde', ',branco','amarelo')
    if type(texto) is not str:
        raise TypeError('texto precisa ser uma estrigue')
    if type(cor) is not str:
        raise TypeError('cor precisa ser uma estingue')
    if cor not in cores:
        raise ValueError(f'Tipo invalido de core. PErmitidos :-> {cores}')
    print(f'O Texto {texto} será impresso na cor {cor}')

colore('Azzul','tres' )
