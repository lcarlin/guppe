lista1 = ["avocaddo", "abuceta", "doguinho fiadaputa", "Luiz ConZê"]
lista2 = [ 2, 4, 8, 16  ]
lista3 = [2.99, 4.89, 5.66, 99.99]

for numero , nome, valor in zip (lista2, lista1, lista3 ):
    print (numero, valor, nome )
