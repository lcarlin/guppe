# -*- coding: cp1252 -*-
"""
Se��o 18 :
    Conhecendo o Pickle

A fun��o do Pickle � realizar o seguine processo:
Objeto Python -> bin�riza��o
bin�riza��o -> Objeto Python
Esse processo � chamado de Serializa��o/Desserializa��o
OBS O Modulo  Pickle n�o � segurocontra dados maliciosos, dessa forma n�o � recomendado trabalhad com arquivos
Pickles de terceiros desconhecidos

====================================================================================================================
====================================================================================================================
====================================================================================================================
====================================================================================================================
====================================================================================================================
====================================================================================================================
"""
import pickle
class Animal:
    def __init__(self, nome ):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome


    def comer (self):
        print(f'{self.nome} is eating' )

class Gato(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def mia(self):
        print(f'{self.nome} ME-AU ME-AU' )

class Cachorro(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def late(self):
        print(f'{self.nome} AU - AU - AU - AU ' )


def main ():
    #print('-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-')
    # Escrita de arquivo
    #felix = Gato('felix')
    #puto = Cachorro('puto')
    #with open('animais.pickle', 'wb') as arquivo:
    #    pickle.dump((felix, puto), arquivo)

    print('-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-')
    # Leitura de arquivos Pickle
    with open('animais.pickle', 'rb') as arquivo:
        gato, cachorro = pickle.load(arquivo )
        print(f'O gato chama-se {gato.nome} ')
        gato.mia()
        print(type(gato))
        print('-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-')
        print(f'O cachorro chama-se {cachorro.nome} ')
        cachorro.late()
        print(type(cachorro))




## e � aqui que a brincadeitra come�a
if __name__ == '__main__':
    main()