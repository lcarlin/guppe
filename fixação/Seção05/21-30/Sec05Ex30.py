list = []  # Cria uma lista em branco

list.append(int(input("coloque o primeiro numero ")))  # Aplica o primeiro numero a lista
list.append(int(input("coloque o segundo numero ")))  # Aplica o segundo numero a lista
list.append(int(input("coloque o terceiro numero ")))  # Aplica o terceiro numero a lista

list.sort()  # Coloca os numeros em ordem com o .sort

print(list)


print ("CVersão 02")
list = [int(input("Numero 1: ")), int(input("Numero 2: ")), int(input("Numero 3: "))]
list.sort()
print(list)