from switchcase import switch


def mesesAno(mes):
    mesesDoAno = {1: "Janeiro",
                  2: "Fevereiro",
                  3: "Março",
                  4: "Abril",
                  5: "Maio",
                  6: "Junho",
                  7: "Julho",
                  8: "Agosto",
                  9: "Setembro",
                  10: "Outubro",
                  11: "Novembro",
                  12: "Dezembro"
                  }
    return mesesDoAno[mes]


dataAValidar = str(input("Entre com a data no formado 'DD/MM/YYYY :-> "))
dataSeparada = dataAValidar.split("/")
dia = int(dataSeparada[0])
mes = int(dataSeparada[1])
ano = int(dataSeparada[2])

mesExtenso = mesesAno(mes)

dataExtenso = f'dia {dia} de {mesExtenso} de {ano} !'
print(dataExtenso)
