valor1 = 0
valor2 = 0
qtd = 0
while qtd <= 0: qtd = int(input("Quantidade de numeros   :-> "))
while valor1 <= 0: valor1 = int(input("Entre com o 1 numero  :-> "))
while valor2 <= 0: valor2 = int(input("Entre com o 2 numero  :-> "))
lista = []
for i in range(1, qtd + 1):
    if (valor1 % i == 0) or (valor2 % i == 0):
        lista.append(i)

lista.sort()
print(lista[0:qtd])
