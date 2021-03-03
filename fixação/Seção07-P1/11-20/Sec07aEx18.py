lista = []
totalValores = 10
numero = 0
conta = 0
listaNova = []
for i in range(totalValores):
    lista.append(int(input(f"Entre com o numero {i+1}  :-> ")))

print("=================================================")
print(lista)
numero = int(input("Entre com o numero a ser verificado :-> "))

for chave, valor in enumerate(lista):
    if valor%numero == 0 :
        conta += 1
        listaNova.append(valor)

print("=================================================")
print(listaNova)
print(f'Total de numeros multiplos :-> {conta}')