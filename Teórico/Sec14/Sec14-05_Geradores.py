"""
Geradoes
- Geradores (Generators) são Iterators (Iteradores)
OBS: a reciprocla não é verdadeira :-> Nem todo Iterator é um Generator

Outras informnações:
-   Generatods podem ser criados com funçõões geradoras:
-   Funções geradoras utilizam a papavra reservvada yield
-   Generatos podem ser criadops com expressoes geradoras

Diferenças entre funções e Generator Functions


====================================================================================================================
# Exemplo de Generator Function
def conta_ate(valor_maximo) :
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador += 1
# OBS : Uma Generator Function não é um Generator . Ela Gera um Generator

gen = conta_ate(5)

print(type(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
====================================================================================================================
# Exemplo de Generator Function
def conta_ate(valor_maximo) :
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador += 1
# OBS : Uma Generator Function não é um Generator . Ela Gera um Generator

gen = conta_ate(15)

for num in gen:
    print( num)
====================================================================================================================
gen = conta_ate(15)

for num in gen:
    print( num)

====================================================================================================================
====================================================================================================================
====================================================================================================================
====================================================================================================================
====================================================================================================================
====================================================================================================================
--------------------------------------------------------------------------------------------------------------------
| Funções                                                         | Generator Functions                            |
--------------------------------------------------------------------------------------------------------------------
| Utilizam Return                                                 | Utilizam Yield                                 |
--------------------------------------------------------------------------------------------------------------------
| APenas um unico return                                          | Utilizam Yield Multiplas Vezes                 |
--------------------------------------------------------------------------------------------------------------------
| QUando Executada retorna Um valor                               | QUando executada, retorna um Generator         |

"""
# Exemplo de Generator Function
def conta_ate(valor_maximo) :
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador += 1
# OBS : Uma Generator Function não é um Generator . Ela Gera um Generator

gen = list(conta_ate(10))
print(gen)