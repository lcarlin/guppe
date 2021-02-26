"""
    Modulo Collections -> DeQue
    pode-se dizer que o Deque é uma lista de Alta PErformace

====================================================================================================================
====================================================================================================================
====================================================================================================================
====================================================================================================================
====================================================================================================================
https://docs.python.org/3/library/collections.html#collections.deque
====================================================================================================================

"""
#mportar
from collections import deque

deq = deque('geek')
print(deq)
print(type(deq))

print ("**********************")
# Adicionando elementos do DeQue
deq.append('Y') # Adiciona no final
print(deq)

print ("**********************")
# Adicionando elementos do DeQue
deq.appendleft('K') # adiciona no inicio da fila
print(deq)

print ("**********************")
deq.pop() # remove e retorna item removido do final
print(deq)

print ("**********************")
deq.popleft() # removoe e retorna o item removido do inicio
print(deq)