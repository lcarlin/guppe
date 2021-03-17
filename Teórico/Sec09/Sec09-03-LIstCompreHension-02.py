"""
LIst CompreHension - 02
Nós podemos adicionar estruturas condicionais lógicas às nossas listCompreHensions
====================================================================================================================
"""
print("=================================================")
# Exemplo 01
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
pares = [numero for numero in numeros if numero % 2 == 0]
impares = [numero for numero in numeros if numero % 2 != 0]
print(pares)
print(impares)
# Better Way ?!?!?
# QUalquer numero par modulo de 2 é 0,
#    0 em Python é False
#    not False = True
pares = [numero for numero in numeros if not numero % 2]
# Qualquer numero impar % 2 = 1 ; 1 em Python = True
impares = [numero for numero in numeros if numero % 2]

print(pares)
print(impares)

res = [ numero * 2  if numero %2==0 else numero/2 for numero in numeros]
print(res)