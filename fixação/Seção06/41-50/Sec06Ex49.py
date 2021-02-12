salCarlos = 10000
salJoao = (salCarlos * 0.3333)  # um terço do salario do João, optei por usar 4 Digitos.

percentCarlos = 0.02  # 2%
percentJoao = 0.05  # 5%

valorAplicaCarlos = 0
valorAplicaJoao = 0

countMeses = 0
atingiuMeta = False
while not atingiuMeta:
    valorAplicaJoao += ((valorAplicaJoao + salJoao) * percentJoao) + salJoao
    valorAplicaCarlos += ((valorAplicaCarlos + salCarlos) * percentCarlos) + salCarlos
    countMeses += 1
    atingiuMeta = valorAplicaJoao >= valorAplicaCarlos

    print(" --- debug")
    print(f" --- > Atingiu a Meta            : {atingiuMeta}")
    print(f" --- > Quantidade de meses Atual : {countMeses}")
    print(f" --- > Valor aplicacao Joao      : {valorAplicaJoao}")
    print(f" --- > Valor Aplicacao Carlos    : {valorAplicaCarlos}")

print("=================================================")
print(
    f"O Patrimonio de João :  {valorAplicaCarlos:.2f}  igualou ou ficou maior \n  ao patrimonio de CArlos {valorAplicaJoao:.2f}   \n  em {countMeses} meses")
print("Final de O programas")
