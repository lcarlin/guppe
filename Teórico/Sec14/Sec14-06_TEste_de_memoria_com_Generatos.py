"""
TEste de Memória com Generatos
====================================================================================================================
"""
# função usand olistas 449MB
def fib_lista(max):
    nums = []
    a, b = 0, 1
    while len(nums) < max:
        nums.append(b)
        a, b = b, a + b

    return nums

def fibo_gen(max):
    a, b, contador =0 , 1, 0
    while contador < max:
        a, b = b, a + b
        yield a
        contador += 1
# tetse
#for n in fib_lista(100):
#    print(n)

for m in fibo_gen(100):
    print(m)