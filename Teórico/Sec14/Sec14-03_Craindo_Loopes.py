"""
criando a sua propria versão de Lupe

====================================================================================================================
for num in [1,2,3,4,5,6]:
    print(num)

for letra in 'Geek University':
    print(letra)
====================================================================================================================

"""


def meu_for (iteravel):
    it = iter(iteravel)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break

numeros = [0,0,1,2,3,4,5,6,7,8,9]
meu_for('Apalpa a minha naba adiposa caso possa')

meu_for(numeros)