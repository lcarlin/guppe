"""
Seção 18 :
JSon -> Java Script Object Notation
API ->  Application Programming Interface
São meios de comunicação entre os serviços oferecidos por embresas (Twitter, FB, YoyTube_ e terceirtos (nós, os DEVVS)

====================================================================================================================
def main ():
    print('-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-')
    ret = json.dumps(['Produto', {'Playstation 5':('2TB', 'Zero-bala', 'AutoVolt',5432.10 )}])
    print(type(ret))
    print(ret)
    print('-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-')
    bastian = Gato('Sebastian', 'psudo-Maine coon')
    print(bastian.__dict__)
    print('-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-')
    print('\nJson Pickle')
    ret2 = jsonpickle.encode(bastian)
    print(ret2)

    print('\nPure Json')
    ret = json.dumps(bastian.__dict__)
    print(ret)

    print('\nEscrevendo o Json/Pickle')
    with open ('bastian.json', 'w') as arquivo:
        ret3 = jsonpickle.encode(bastian)
        arquivo.write(ret3)
====================================================================================================================
====================================================================================================================
====================================================================================================================
====================================================================================================================
====================================================================================================================
"""
import json
import jsonpickle

class Gato:
    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca

def le_arquivo(file):
    print('\nLENDO  o Json/Pickle')
    with open(file, 'r') as file:
        ret = jsonpickle.decode(file.read())
        return ret

def grava_arquivo(file, obj):
    print('\nEscrevendo o Json/Pickle')
    with open(file, 'w') as arquivo:
        jsonpickle.encode(obj)
        arquivo.write(jsonpickle.encode(obj))


def main():
    test_file = 'bastian.json'
    bastian = Gato('Sebastian', 'psudo-Maine coon')
    grava_arquivo(test_file, bastian)

    ret = le_arquivo(test_file)

    print('\nApós a leitura do Objecto from disk ')
    print(type(ret))
    print(ret)
    print(ret.nome)
    print(ret.raca)

    print(bastian== ret)


## e é aqui que a brincadeitra começa
if __name__ == '__main__':
    main()
