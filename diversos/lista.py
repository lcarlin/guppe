# -*- coding: utf-8 -*-
lista0 = [1,2,3,4,5,6]
lista1 = ["Olá que tal", "dois"]
lista2 = [0, "ola", "bixcoito", 99.99, False ]

for i in lista2:
    print (i)

print ("============================")
for j in range (10,20,2):
    print (" E o J -e :-> " + str (j) )
    
print (len(lista0))
print (len(lista2))
print (len(lista1))
print ("============================")

lista0.append(7)
lista1.append("TRexto")
lista1.append("gato")
print ("============================")
for k in lista1:
    print (k)

print (len(lista0))
print (len(lista2))
print (len(lista1))
print ("============================")
Achar = "gato"
if Achar in lista1:
    print ("O Numero " + str (Achar) + " Esta na lista ")
else:
    print ("Nao foi dessa vez ")


print ("============================")
del lista0[3:]
print (lista0)