# -*- coding: utf-8 -*-
a = "Dieguitto"
b = "Mary-Ann"
print (a)

c = a + " " + b + "\n"
print (c)
print ( len(c))

print ( c[6] )
print (c [4:9])

print (c.lower() )

print (c.strip())




minha_string = "O REato roeu a Roupa do Rei de A Romea"
minha_lista = minha_string.split(" ")
print (minha_lista)


busca = minha_string.find("rei ")

print (busca)

print (minha_string[busca:])

print (minha_string.replace("Rei", "Imperator"))