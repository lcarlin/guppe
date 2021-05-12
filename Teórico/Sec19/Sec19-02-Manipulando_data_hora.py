"""
Seção 19 :
Manipulando Data-e-horas com DateTime
Python tem modulos Build-In (iuntegrado) para se trabalhad com data e hora
====================================================================================================================
    print('-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-')
    print(datetime.MAXYEAR)
    print(datetime.MINYEAR)
    print(datetime.datetime.now())

    print (repr(datetime.datetime.now()))

    inicio = datetime.datetime.now()
    print(type(inicio))

    print(inicio)
    print('=====================================')
    inicio = inicio.replace(hour=23, microsecond=999999, second=59, minute=59)
    print(inicio)
    print('=====================================')
    inicio = inicio.replace(year=2036, month=12, day=31)
    print(inicio)

    print('=====================================')
    oEvento = datetime.datetime(2019,1,1)
    print(oEvento)

    print('=====================================')
    nasc = input(f'Informa Vossa dada de Nascimento (dd/mm/yyyy) :-> ')
    print(type(nasc))
    print(nasc)
    nasc = nasc.split('/')
    print(nasc)
    print(type(nasc))
    print('+++++++++++++++++++++++++++++++++++++')
    nasc = datetime.datetime(int(nasc[2]),int(nasc[1]),int(nasc[0]) )
    print(type(nasc))
    print(nasc)
====================================================================================================================
====================================================================================================================
====================================================================================================================
====================================================================================================================
====================================================================================================================
"""
import datetime
def main ():
    print('-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-')
    evento = datetime.datetime.now()
    print('=====================================')
    print(evento.year)
    print(evento.month)
    print(evento.day)
    print(type(evento.year))
    print('+++++++++++++++++++++++++++++++++++++')
    print(evento.hour)
    print(evento.minute)
    print(evento.second)
    print(evento.microsecond)
    print(type(evento.hour))


## e é aqui que a brincadeitra começa
if __name__ == '__main__':
    main()
