"""
O Block Try/Except
Utilizamos o bloco Try/Excep para tratar erros que podem ocorrer no nosso código, privinindo assim que o programa páre
de funcionar e o usuário receba mensagens dew erro inesperadas

A forma geral + simples é :
try:
    // execução problematica
except:
    // o que deve ser feito em caso de problemas

====================================================================================================================
# exemplo 1 - tratantdo um erro generico
try:
    geek()
except:
    print('Vixe, deu pau')
OBS: tratar erro de forma generia não é a melhor forma de tratamento de errros. O ideal é sempre tratar de forma
especifica
====================================================================================================================
Tratanto um erro especifico

try:
    geek()
except NameError:
    print('Tentou usar uma função que nOn Ecxiste' )
====================================================================================================================
try:
    len(5)
except TypeError as err:
    print(f'Vixe, deu Pau :-> {err}')

====================================================================================================================
#Podemos efetuar diversos tratamento de errors de uma vez
try:
    print('Geek'[9])
    # len(4)
    # geek()
except NameError as nameErr :
    print (f'Deu Names Error :-> {nameErr}')
except TypeError as typeErr :
    print (f'Deu Names Error :-> {typeErr}')
except :
    print(f'QUe tiro foi esse ::->  ? ')
====================================================================================================================

"""
def pegaValor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError as dois:
        return None
    except TypeError as tipeErr:
        return None

dic = {'nome' : 'Geek'}
print(pegaValor(dic,'PPK'))