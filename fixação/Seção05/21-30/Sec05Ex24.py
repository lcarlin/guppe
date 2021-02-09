from switchcase import switch
valorProduto = float(input("Digite o Valor de O Produto:-> "))
estadoVenda = str(input("Digite o estado de destino :-> ")).upper()
precoFInal = 0

resultado = 0
icms = 0
for case in switch(estadoVenda):
    if case("MG"):
        icms=7
        break
    if case("SP"):
        icms=12
        break
    if case("RJ"):
        icms=15
        break
    if case("MS"):
        icms=8
        break
else:
    print ("Estado é iválido" )

if icms > 0 :
    precoFInal = valorProduto + ( ( valorProduto * icms) / 100 )
    print ("E o valor final é :-> " + str(precoFInal))
