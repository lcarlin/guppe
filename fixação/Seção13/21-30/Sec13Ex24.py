despensa = []
codigo = 0
sair = "n"

print("===" * 30)
while sair != "s":
    produto = []
    produto.append(str(input("Insira o nome do produto: ")))
    produto.append(codigo)
    produto.append(int(input("Insira a quantidade: ")))
    codigo += 1
    despensa.append(produto)
    sair = str(input("Deseja sair? s/n\n").lower())

print()
print("========ITENS ATUALMENTE NA DESPENSA========")
for i in range(len(despensa)):
    print(despensa[i])

print("============================================")
print("O que deseja fazer agora?")
comando = 0
while comando != 4:
    comando = int(input("Adicionar itens na despensa - digite 1\n"
                        "Remover itens da despensa - digite 2\n"
                        "Verificar despensa - digite 3\n"
                        "Finalizar e gravar em arquivo - digite 4\n"))

    if comando == 1:
        print("===========ADICIONAR PRODUTOS===========")
        controle = str(input("O produto a ser adicionado já existe na despensa? s/n\n").lower())
        if controle == "s":
            codigo = int(input("Qual o codigo do produto?\n"))
            despensa[codigo][2] += int(input(f"Insira a quantidade de novos produtos do tipo {despensa[codigo][0]}: "))
        if controle == "n":
            codigo = despensa[-1][-2]
            produto = []
            produto.append(str(input("Insira o nome do produto: ")))
            produto.append(codigo + 1)
            produto.append(int(input("Insira a quantidade: ")))
            despensa.append(produto)
        print("=========================================")
        print("===========DESPENSA===========")
        for item in despensa:
            print(item)
        print("========================================")

    elif comando == 2:
        print("===========REMOVER PRODUTOS===========")
        codigo = int(input("Qual o código do produto?\n"))
        despensa[codigo][2] -= int(
            input(f"Insira a quantidade de produtos a serem removidos de {despensa[codigo][0]}: "))
        print("======================================")
        print()
        if despensa[codigo][2] <= 0:
            despensa[codigo][2] = 0
            print(f"ATENÇÃO: O produto {despensa[codigo][0]} está em falta!")
            print("========================================")
        print("===========DESPENSA===========")
        for item in despensa:
            print(item)
        print("========================================")

    elif comando == 3:
        print("===========VERIFICAR DESPENSA===========")
        for item in despensa:
            print(item)
        print("========================================")
        print()

    elif comando == 4:
        print("============GRAVANDO EM ARQUIVO==============")
        print("============PROCESSO FINALIZADO==============")

with open("despensa.txt", mode='r+', encoding='UTF-8') as desp:
    for x in despensa:
        for y in x:
            if y == x[0]:
                desp.write(f"Produto: {y}, ")
            elif y == x[1]:
                desp.write(f"Código: {y}, ")
            elif y == x[2]:
                desp.write(f"Quantidade: {y}\n")