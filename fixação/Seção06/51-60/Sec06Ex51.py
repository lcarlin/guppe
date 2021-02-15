from datetime import date

anoAtual = 1995
salarioAtual = 2000
percentAumento = 0.015
dataAtual = date.today()
anoReal = dataAtual.year
while anoAtual <= anoReal:

    salarioAtual = salarioAtual + ((salarioAtual*percentAumento))
    print("----------------------------------------")
    print(" --- debug")
    print(f" --- > Ano Atual            : {anoAtual}")
    print(f" --- > Salario Atual        : {salarioAtual:.2f}")
    print(f" --- > Percente de Aumento  : {percentAumento:.4f}")
    anoAtual += 1
    percentAumento *= 2

print("=================================================")
print("Final de O programas")