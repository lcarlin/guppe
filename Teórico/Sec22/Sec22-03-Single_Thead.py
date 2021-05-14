import time
from threading import Thread
contador = 50000000

def contagem_regressiva(n):
    while n > 0:
        n -= 1

inicio = time.time()
contagem_regressiva(contador)
fim = time.time()

print(f'Temp em Segundos :-> {fim - inicio}')
# Temp em Segundos :-> 2.1152403354644775