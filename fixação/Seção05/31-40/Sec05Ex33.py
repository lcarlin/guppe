precoAntigo = float(input("Digite o preco antigo que será reajustado :->"))

if precoAntigo < 50:
    percentAumento = 5
elif 50 <= precoAntigo <= 100:
    percentAumento = 10
elif precoAntigo > 100:
    percentAumento = 15

novoPreco = (precoAntigo) + (( precoAntigo * percentAumento  ) / 100 )
if novoPreco <=80:
    msg = "Tá Barato"
elif 80 <= novoPreco <= 120:
    msg = " ta dentro "
elif 120 < novoPreco <= 200:
    msg = " Meio caro "
elif novoPreco > 120 :
    msg = "Sai fora. tá caro "

print(f"E o novo preço é {novoPreco} e o diagnostico é :{msg}")