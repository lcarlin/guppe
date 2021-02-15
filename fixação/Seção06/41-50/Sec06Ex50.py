alturaChico = 1.50
crescimentoChico = 0.02

alturaZe = 1.10
crescimentoZe = 0.03

atingiuAltura = False
counterAno = 0

while not atingiuAltura:

    alturaChico += crescimentoChico
    alturaZe += crescimentoZe

    counterAno += 1

    atingiuAltura = alturaZe >= alturaChico

    print(" --- debug")
    print(f" --- > Atingiu a Meta           : {atingiuAltura}")
    print(f" --- > Quantidade de anos atual : {counterAno:.2f}")
    print(f" --- > Altura Atual Chico       : {alturaChico:.2f}")
    print(f" --- > Altura Atual Zé          : {alturaZe:.2f}")

print("=================================================")
print(
    f"A altura atual do Zé -> {alturaZe:.2f} superou a altura do Chico :-> {alturaChico:.2f} \n  em {counterAno} anos " )
print("Final de O programas")
