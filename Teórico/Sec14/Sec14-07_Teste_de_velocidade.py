"""
TEste de velocidade com ex0pressões geradoras
====================================================================================================================
# Geberatos(GEradoresa)
def nums():
    for num in range(1,10):
        yield num

ge1 = nums()
print(ge1)
print(next(ge1))
print(next(ge1))
print('-----------------------------------------------')

ge2 = (num for num in range(1,10 ))
print(ge2)
print(next(ge2))
print(next(ge2))
====================================================================================================================
"""
# realizando o teste de velocidade
import time
# Generator xPression
gen_inicio = time.time()
print (sum (num for num in range(0,100000000)))
gen_tempo = time.time() - gen_inicio

list_inicio = time.time()
print(sum([num for num in range(0,100000000)]))
list_tempo = time.time() - list_inicio

print(f'Generator xPression -> {gen_tempo}')
print(f'list ComprHension   -> {list_tempo}')