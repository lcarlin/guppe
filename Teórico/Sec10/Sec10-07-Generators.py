"""
Generators
Em aulas anterioresm foi visto
-   LIst CompreHensions
-   Dictionary CompreHension
-   Set CompreHensions

Não vimos
-   Tuple CompreHensions .. pórque se chamavam Generators
====================================================================================================================
nomes = ['CAssiano','CAmilo','Compostela','Frater','Rosa-cruz', 'Monge']
print(any([nome[0] == 'C' for nome in nomes ]))
====================================================================================================================
nomes = ['CAssiano', 'CAmilo', 'Compostela', 'Frater', 'Rosa-cruz', 'Monge']
# Poderiamos ter usado o Generatos
print(any(nome[0] == 'C' for nome in nomes))

# List CompreHension
res = [nome[0] == 'C' for nome in nomes]
print (type(res))

#Generator
res = (nome[0] == 'C' for nome in nomes)
print(type(res))
# Se for pra escolher entre um dos dois,escolha o Generator, pois consome Menos recurso em memória

====================================================================================================================
#QUal é a utilizade de GetSizeOf ? -> Retorna a quantidade de Bytes em memoria do elemento passado como parametro
from sys import getsizeof

#Mostra quantos Bytes a String ocupa em memoria
print(getsizeof('Geek'))
print(getsizeof('University'))
# Quanto > a String, + espaco ocupa

print(getsizeof(9))
print(getsizeof(91))
print(getsizeof(92345668823))
print(getsizeof(True))
====================================================================================================================
#QUal é a utilizade de GetSizeOf ? -> Retorna a quantidade de Bytes em memoria do elemento passado como parametro
from sys import getsizeof

#Gerando uma lista de Numeros com o LIst COmpreHension
list_compre = getsizeof([x * 10 for x in range(1000)])

#Gerando uma lista de Numeros com o Set COmpreHension
set_compre = getsizeof({x * 10 for x in range(1000)})

#Gerando uma lista de Numeros com o Dict COmpreHension
dict_compre = getsizeof( {x : x * 10 for x in range(1000)} )

#Gerando uma lista de Numeros com o Generator
gen = getsizeof(x * 10 for x in range(1000))
print('Gasto de memoria para fzer a mesma tafera : ')
print(f'List CompreHension :-> {list_compre}')
print(f'Set  CompreHEnsion :-> {set_compre} ' )
print(f'Dict CompreHension :-> {dict_compre}')
print(f'Generators         :-> {gen}') # note que aqui os valores AINDA NÃO EXISTEM, só existyirãoquando vc usa-los
                                       # efetivamente, por isso que consome menos espaçõ em bytes
====================================================================================================================
"""
# É possiel ityerar no generator expression? SIM !!!!
gen = ( x * 10 for x in range(1000))
print(gen)
print(type(gen))

for num in gen:
    print(num)
