from functools import reduce

def somar (x, y ):
    return x + y 

lista = [1,3,5,7,9 , 11, 13  ]
soma = reduce (somar , lista)
print(soma)