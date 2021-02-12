numBase = 0
counter = 0
atual = 0
proximo = 1
temp = 0
soma = 0
while True:
    print(atual)
    temp = atual + proximo
    atual = proximo
    proximo = temp
    counter += 1
    soma += atual
    if atual >= 4000000 :
        break


print("=================================================")
print(f" E a soma é :-> {soma}")
print("Final de O programas")