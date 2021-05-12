"""
Seção 18 :
Deltas entre dadas e horas
data_inicial
data_final
====================================================================================================================
====================================================================================================================
====================================================================================================================
====================================================================================================================
====================================================================================================================
====================================================================================================================
"""
import datetime

def main ():
    print('-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-')
    aHora = datetime.datetime.now()
    proximo = datetime.datetime(2021,8,25,0 )
    print(f'Calculando O Deltas ')
    tempo = proximo - aHora
    print(type(tempo))
    print(repr(tempo))
    print(tempo)
    print('=====================================')
    print(f'Faltam {tempo.days} pro aniversároi ')
    print('+++++++++++++++++++++++++++++++++++++')
    data_compra =  datetime.datetime.now()
    regra_boleto = datetime.timedelta(days=5)
    print(regra_boleto)
    vecimento = data_compra + regra_boleto
    print(vecimento)
    print(type(vecimento))


## e é aqui que a brincadeitra começa
if __name__ == '__main__':
    main()