import pandas as pd
import fundamentus
import matplotlib.pyplot as plt

dados = fundamentus.get_resultado()
filtro = dados[(dados.pl < 16) & (dados.dy > 0.08) & (dados.pvp < 1.16) & (dados.roe > 0.09) & (dados.liq2m > 100000)]
filtro.sort_values('dy', ascending = False, inplace = True)

#precisa de outro filtro....
#acoes repetidas com finais 3, 4 e 11....
#Prioridade só deixar o 11, caso nao tenha o 11, escolher o final 4

plt.figure(figsize = (18,8))
plt.bar(filtro.index, filtro.dy)
plt.xticks(rotation = 45)
plt.title("As melhores Ações para se aposentar !!!")