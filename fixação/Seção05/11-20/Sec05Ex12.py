base = int(input("Entre com a Base :-> "))
loga = int(input("Entre com o LOgaritmando :-> "))
if base > 1 and loga > 0:

    novo=loga
    log1=0
    while novo != 1:
        novo = novo / base
        log1 = log1 + 1

    print (f"o LOG de {loga}  na base {base} é :-> {log1} ")

else:
    print("A base tem quie ser maior que 1 e o Lgaritimando maior que 0 ")