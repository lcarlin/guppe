
# -*- coding: utf-8 -*-
print ("-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=")

def dobro(x):
    return x * 2 

valor = [ 2, 4, 8, 16 ,32, 64 ]

dobrado = map ( dobro, valor )

for d in dobrado: 
    print (d) 
print ("-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=")    
doisDobro = list(dobrado)
print (doisDobro)