from collections import  defaultdict
lista = []
totalValores = 10

for i in range(totalValores):
    lista.append(int(input(f"Entre com o numero {i}  :-> ")))

print("=================================================")
print(lista)
print (len(sorted(set(lista))))

chaves = defaultdict(list)
for key, valor in enumerate(lista):
    chaves[valor].append(key)

for valor in chaves:
    if len(chaves[valor]) > 1:
        print(f"Numero repetido :=-> {valor}")
print("=================================================")
print("EOP ")