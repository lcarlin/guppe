salario = float(input("Digite o salario do Cabra :-> "))
prestacao = float(input("Digite o valor da parcela do emprestimo :-> "))

porcentPrest = (prestacao/salario) * 100

if porcentPrest >= 20:
    print(f"A prestacao consome {porcentPrest} do salario do cabra . Nao da pra conceder. ")
else:
    print(f"A prestacao consome {porcentPrest} . Emprestimo concedido" )

