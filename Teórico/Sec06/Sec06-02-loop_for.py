nome = "Alpa a minha naba adiposa caso possa "
lista = [ 1 , 3 , 5 , 7 ,9  , 11]
numeros =  range (1, 10 )
"""
for letra  in nome :
    print (letra)

for valmor in lista:
    print (valmor)

for doi in numeros:
    print( doi)
    
for indice, letra in enumerate(nome):
    print (f"{indice} - {letra}" )

for valor in enumerate(nome):
    print (valor  )

qtd = int(input("QUantas Vezes ? :-> "))
soma = 0
for n in range (1,qtd + 1 ):
    print(f"Imprimindo N:-> {n}")
    numero =  int (input(f'Informe o {n}/{qtd} valor: '))
    soma += numero

print (soma)

for letra in nome:
    print(letra, end='')

# Original 	U+1F61C
# Novo      U0001F61C

emoji = 'U0001F61C'
for num in range (1,11):
    print('\U0001F61D' * num)
"""
emoji = '\U0001F64F'
for _ in range(3):
    for num in range (1,11):
        print( emoji * num)