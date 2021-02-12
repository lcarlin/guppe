numBase = 0
counter = 0
atual = 0
proximo = 1
temp = 0
while numBase <= 0: numBase = int(input("Entre com o 1 numero  :-> "))
while True :
    print(atual)
    temp = atual + proximo
    atual = proximo
    proximo = temp
    counter += 1
    if atual > numBase:
        break

print("=================================================")
print("Final de O programas")