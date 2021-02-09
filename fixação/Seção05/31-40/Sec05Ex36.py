vendasMesais = float(input("Entre com o valor total de vendas :-> "))

porcentVendas = 14
bonusAdicional = 0
valorComissao = 0
if vendasMesais >= 100000:
    porcentVendas = 16
    bonusAdicional = 700
elif 80000 <= vendasMesais < 100000:
    bonusAdicional = 650
elif 60000 <= vendasMesais < 80000:
    bonusAdicional = 600
elif 40000 <= vendasMesais < 60000:
    bonusAdicional = 550
elif 20000 <= vendasMesais < 40000:
    bonusAdicional = 500
elif 20000 < vendasMesais:
    bonusAdicional = 400

valorComissao = ((vendasMesais * porcentVendas) / 100 ) + bonusAdicional

print(f"E o valor total de comissoes é :-> {valorComissao:.2f} ")