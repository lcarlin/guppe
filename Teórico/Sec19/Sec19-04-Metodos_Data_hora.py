"""
Seção 19 :
Metoos de Data/Horas
now() e today() s´~ao semelhantes, porem no now() é possivel especificar uma TimeZone
====================================================================================================================
    aHora = datetime.datetime.now()
    print(aHora)
    print(type(aHora))
    print(repr(aHora))
    print('=====================================')
    hoje = datetime.datetime.today()
    print(hoje)
    print(type(aHora))
    print(repr(hoje))
    print('+++++++++++++++++++++++++++++++++++++')
====================================================================================================================
    print('-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-')
    manuTencao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=2)), datetime.time())
    print(manuTencao)
    print(type(manuTencao))
    print(repr(manuTencao))
    print('=====================================')
    print('Achar agora o dia da semana')
    # Os dias da semana do método WeekDay começam em ZERO = segunda e terminam em 6 = domingo
    print(manuTencao.weekday())

    print('+++++++++++++++++++++++++++++++++++++')
    print('-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-')
====================================================================================================================
   dictDiasSemans = {0:'Segunda-Feira',
                      1:'Terça-feira',
                      2:'Quarta-Feira',
                      3:'Quinta-Feira',
                      4:'Sexta-Feira',
                      5:'Sabado',
                      6:'Domingo' }
    nasc = input(f'Informa Vossa dada de Nascimento (dd/mm/yyyy) :-> ')
    print(type(nasc))
    print(nasc)
    nasc = nasc.split('/')
    print(nasc)
    print(type(nasc))
    nasc = datetime.datetime(int(nasc[2]), int(nasc[1]), int(nasc[0]))
    print('=====================================')
    print(f'Você nasceu em um(a) {dictDiasSemans[nasc.weekday()]}')
    print('+++++++++++++++++++++++++++++++++++++')
====================================================================================================================
 #Formatando datas/horas co strftime() - String Format Time()
    hoje = datetime.datetime.today()
    print(hoje)
    print('===========================================================')
    hoje_formatado = hoje.strftime('%d/%m/%Y') # Y -> YYYY ; y -> yy; B nomne do mes em Ingles ; b Iniciais do mes em ingles - POracle
    print(hoje_formatado)
    print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    print(formata_data(hoje))

    print('-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-')
    print(formata_data2(hoje))
    print('===========================================================')
    # isso aqui converte a String pra DateTime
    # presta atençãno nome que é STR P TIME e não STR F TIME
    nascimento = datetime.datetime.strptime('10/04/1998', '%d/%m/%Y')
    print(type(nascimento))
    print(repr(nascimento))
    print('-----------------------------------------------------------')
    almoco = datetime.time(12,30,0)
    print(type(almoco))
    print(repr(almoco))
    print(almoco)
    print('***********************************************************')
====================================================================================================================
    print('Tempo de processamento com data-horas')
    ## loop for
    tempo1 = timeit.timeit('"-".join(str(n) for n in range (100))', number=10000)

    # list CompreHension
    tempo2 = timeit.timeit('"-".join([str(n) for n in range (100)])', number=10000)

    # Maps
    tempo3 = timeit.timeit('"-".join(map(str,range (100)))', number=10000)

    print(f'Tempo 1 {tempo1}')
    print(f'Tempo 2 {tempo2}')
    print(f'Tempo 3 {tempo3}')
====================================================================================================================
====================================================================================================================
====================================================================================================================
====================================================================================================================
https://docs.python.org/3/library/datetime.html
https://textblob.readthedocs.io/en/dev/
"""
import datetime
from textblob import TextBlob
import timeit, functools


def teste(n):
    soma = 0
    for num in range(n * 200):
        soma += (num ** num + 4)

    return soma


def formata_data2(data):
    return f"{data.day} de {TextBlob(data.strftime('%B')).translate(to='pt-br')} de {data.year} "


def formata_data(data):
    __dictMeses = {1: 'Janeiro',
                   2: 'Fevereiro',
                   3: 'Marco',
                   4: 'Abril',
                   5: 'Maio',
                   6: 'Junho',
                   7: 'Julho',
                   8: 'Agosto',
                   9: 'Setembro',
                   10: 'Outubro',
                   11: 'Novembro',
                   12: 'Dezembro'}
    __dictSemana = {0: 'Segunda-Feira',
                    1: 'Terça-feira',
                    2: 'Quarta-Feira',
                    3: 'Quinta-Feira',
                    4: 'Sexta-Feira',
                    5: 'Sabado',
                    6: 'Domingo'}

    return f'Hoje é {__dictSemana[data.weekday()]} , {data.day} de {__dictMeses[int(data.month)]} de {data.year}'


def main():
    print('-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-')
    print(timeit.timeit(functools.partial(teste, 2), number=10000))


## e é aqui que a brincadeitra começa
if __name__ == '__main__':
    main()
