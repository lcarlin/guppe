"""
Any e All - funççoes Integradas Buit In
all () -> função Booleana que retornar True se todos os Elementos do Ityerável são verdadeioros ou ainda se o Iterávesl está vazio
====================================================================================================================
# Exemplo all
# False, por conta do zero que tem valor booleano falso
print(all([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))  # todos os numeros são verdadeiros ?!?!?!?

# True, pois todos valores > 0 são True
print(all([1, 2, 3, 4, 5, 6, 7, 8, 9]))  # todos os numeros são verdadeiros ?!?!?!?
print(all([]))
print(all((1,2,3)))
print(all({1,2,3,4}))
print(all('Geek'))

nomes = ['Cassiano','Camilo','Compostella', 'Jyraya', 'JAspion']
print (all([nome[0] == 'C' for nome in nomes]))
====================================================================================================================
# OBS: Uniterável vazio comnvertido em Boolean é false, mas o All() entende iteraveis vazios com true
print (all([letra for letra in 'fgh' if letra in 'aeiou']))

print (all([num for num in [4,2,10,6,8] if num % 2 == 0 ]))
====================================================================================================================
Any () -> retorna True se quaoquer elemento do Iterável for verdadeiro, se for vazio, retorna falso
====================================================================================================================

"""
print(any([0, 1, 2, 3, 4]))

print(any([0, False, {}, (), {}, 'A']))

nomes = ['CAssiano','CAmilo','Compostela','Frater','Rosa-cruz', 'Monge']
print(any([nome[0] == 'C' for nome in nomes ]))