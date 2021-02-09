def anoBissexto(ano):
    valida1 = ((ano % 400) == 0)
    valida2 = ((ano % 4) == 0) and (ano % 100 != 0)
    ## print(valida1)
    ## print(valida2)
    if valida1 or valida2:
        print(f"O Ano {ano} é Biscesto ")
        return 29
    else:
        print(f"O Ano {ano} NÃO é Biscesto ")
        return 28



dataAValidar = str(input("Entre com a data no formado 'DD/MM/YYYY :-> "))
dataSeparada = dataAValidar.split("/")
dia = int(dataSeparada[0])
mes = int(dataSeparada[1])
ano = int(dataSeparada[2])

diasMeses = {1: 31,
             2: anoBissexto(ano),
             3: 31,
             4: 30,
             5: 31,
             6: 30,
             7: 31,
             8: 31,
             9: 30,
             10: 31,
             11: 30,
             12: 31}

mesValido = False
anoValido = False
diaValido = False

if 0 < ano <= 9999:
    anoValido = True

if 1 <= mes <= 12:
    mesValido = True
    if dia <= int(diasMeses[mes]):
        diaValido = True

if diaValido and mesValido and anoValido:
    print(f"A data {dataAValidar} é Valida" )
else:
    print("TEm coisa errada com essa data ai. da uma olhada")