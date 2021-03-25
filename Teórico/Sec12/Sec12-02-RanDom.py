"""
Módulo RamDom
o que são os Moduloes ??
*   Em python nada mais são do que outros arquivos Pyrthon
Modulo RaNDOM -> possui várias funções para gerar de numeros Pseudo-aleatórios (???)
#OBS : existem 2 formas de se utilizar um módulo função deste
====================================================================================================================
# forma 01 - importando TODO o módulo
# import random
# Ao realizar o Import de todo o módulo, todas as funções, atributos, classe e propriedades que estão dentro do modulo
# estarão " disponiveis" isso é : em memória. - NÃO RECOMENDADO
# AGora, caso você saiba quais fun~~oes precisa utilizar desse modulo, essa não é a forma ideal de Import
# print(random.random())
# Gera um numero real aleatório entre 0 e 1
# para utilzar a função random() do pacote random, colocamos o nome do pacote e o nome da função separado por " . "
# OBS : não confunda a função Random com o Pacote Random,

====================================================================================================================

# forma 02 - importando uma função especifica de um módulo :
# na linha abaixo, estamos espeficando qual a função que deve ser importada de qual módulo
from random import random

for i in range(10):
    print(random())
====================================================================================================================
from random import uniform
# uniform -> Gerar um numero real Pseudo-Aleatório entre os valores estabelecidos:
for i in range(10):
    print(uniform(3,7)) # não incluido

====================================================================================================================
# randint() -> gera valores pseudo-aleatórios entre o intervalo estabelecido
from random import randint
# gerador de apostas as megaSennna
for i in range(6):
    print(randint(1,61), end = ', ')
====================================================================================================================
from random import choice
# Mostra um valor aleatório entre um iterável ( ???? )
jopgadas = ['pedra', 'papel', 'tesoura', 'Spock', 'lagarto']
print(choice(jopgadas))

print (choice('Geek University'))
====================================================================================================================
"""
# shuffle() -> tem a função de embaralhar dados
from random import shuffle
cartas = ['K', 'Q', 'J', 'A', '2','3', '4', '5', '6', '7', '8', '9', '10']
print(cartas)
while len(cartas) > 0 :
    shuffle(cartas)
    print(cartas)
    print(f'E a sua carta é :-> {cartas.pop()}')

