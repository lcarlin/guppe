"""
Seção 17 -
*   Polimofismo
Poli -> Multas
Morfis -> Formas

Objetios que podem possuir muitas formas OU podem comportar de formas diferentes

Quando a gente re-implemneta um metodo presente na classe Pai em classes filhas ,estamos realizando
 uma sobrescrita de método (Overriding)

 o Overriding é a melhor representação do PoliMorfismos
====================================================================================================================
====================================================================================================================
====================================================================================================================
====================================================================================================================
====================================================================================================================
====================================================================================================================

"""


class Animal(object):
    def __init__(self, nome):
        self.__nome = nome

    def falar(self):
        raise NotImplementedError('A classe filha é que precisa implementar isso aqui ')

    def comer(self):
        print(f'{self.__nome} is comendo ')


class Cachorro(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} fala Au A Au ')


class Gato(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} fala Me-Au Me-Au Me-Au ')


class Rato(Animal):
    def falar(self):
        print(f'{self._Animal__nome} fala Ah Ah Ah  ')


    def __init__(self, nome):
        super().__init__(nome)


def main():
    print('-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-')
    # testando
    feliz = Gato('Felix')
    feliz.comer()
    feliz.falar()

    puto = Cachorro('Puto')
    puto.comer()
    puto.falar()

    miquei = Rato('Miquei')
    miquei.comer()
    miquei.falar()


# e é aqui que a brincadeitra começa
if __name__ == '__main__':
    main()
