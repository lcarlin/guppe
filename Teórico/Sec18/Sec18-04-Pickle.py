# -*- coding: cp1252 -*-
"""
Seção 18 :
    Conhecendo o Pickle

A função do Pickle é realizar o seguine processo:
Objeto Python -> binárização
binárização -> Objeto Python
Esse processo é chamado de Serialização/Desserialização
OBS O Modulo  Pickle não é segurocontra dados maliciosos, dessa forma não é recomendado trabalhad com arquivos
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




## e é aqui que a brincadeitra começa
if __name__ == '__main__':
    main()