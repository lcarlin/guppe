def convertEmSegundos(horas, minutos, segundos):
    return (horas*360) + (minutos * 60 ) + segundos

numHor = int(input("Entre com as Horas    :-> "))
numMin = int(input("Entre com os Minutos  :-> "))
numSec = int(input("Entre com os Segundos :-> "))
convertido = convertEmSegundos(numHor, numMin, numSec)

print(f'PAra o "Tempo" {numHor}:{numMin}:{numSec} , a quantidade absoluta de segundos é:-> {convertido} ')