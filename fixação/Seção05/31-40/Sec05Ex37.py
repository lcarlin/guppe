def validarHora(hora):
    horaSeparada = hora.split(":")
    if 0 <= int(horaSeparada[0]) < 24 and 0 <= int(horaSeparada[0]) < 60:
        return True
    else:
        return False


Entrada = input("Entre com a hora de entrada no formado HH24:MM :-> ")
Saida = input("Entre com a hora de saida no formado HH24:MM :-> ")
tempoAbsoluto = 0
totalFull = 0
valorAPagar = 0
if validarHora(Entrada) and validarHora(Saida):
    tempoEntrada = int(Entrada.split(':')[0]) * 60 + int(Entrada.split(':')[1])
    tempoSaida = int(Saida.split(':')[0]) * 60 + int(Saida.split(':')[1])
    print(f"{tempoEntrada} - {tempoSaida}")
    if Saida <= Entrada:
        tempoAbsoluto = (1440 - tempoEntrada) + tempoSaida
    else:
        tempoAbsoluto = tempoSaida - tempoEntrada

    totalHoras = int(tempoAbsoluto / 60)
    totalMinutos = int(tempoAbsoluto % 60)
    totalFull = totalHoras
    if totalMinutos >= 1: totalFull = totalHoras + 1

    print(f"Tempo total em minutos :-> {tempoAbsoluto}")
    if totalFull == 1:
        valorAPagar == 1.00
    elif totalFull == 2:
        valorAPagar = 2.00
    elif totalFull == 3:
        valorAPagar = 2 + 1.4
    elif totalFull == 4:
        valorAPagar = 2 + 2.8
    elif totalFull >= 5:
        valorAPagar = totalFull * 2

    print(f"Total de horas : {totalFull}  ; Valor a se pagar : {valorAPagar:.2f}")
else:
    print("Alguma das horas estão erradas. Verificar !")
