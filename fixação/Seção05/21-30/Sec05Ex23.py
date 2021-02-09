ano = int(input("Digite o ano para validação:-> "))
valida1 = ((ano % 400) == 0)
valida2 = ((ano % 4) == 0) and (ano % 100 != 0)
print(valida1)
print(valida2)
if valida1 or valida2:
    print(f"O Ano {ano} é Biscesto ")
else:
    print(f"O Ano {ano}     NÃO é Biscesto ")
