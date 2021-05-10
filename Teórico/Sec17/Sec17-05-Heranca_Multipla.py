"""
Seção 17 -
*   Heranca Multipla
H.M. nada mais é do quye a possibilidade de uma classe herdade de multiplcas classes, fazendo com quye a classe filha
herde todos os atributos e metodos de todas as classes herdadas.
A H.M pode ser feito de duas Maneiras:
    -   Por multidericação direta
    -   Por Multiderivação Indireta
Não importa de a derivação é direta ou indireta. A classe que realizazr a herança herdará todos os metodos e atributos
das SuperClasses.
====================================================================================================================
# Exemplo 01 - Multiderivação DIRETA
class Base1:
    pass

class Base2:
    pass

class Base3:
    pass

class MultiDerivada(Base1, Base2, Base3)

# Exemplo 02 - MUltiDerivação Indireta
class Base4:
    pass

class Base5(Base4):
    pass

class Base6(Base5)
    pass
====================================================================================================================
====================================================================================================================
====================================================================================================================
====================================================================================================================
====================================================================================================================

"""
class Animal:
    def __init__(self, nome ) :
        self.__nome = nome

    def cumprimentar(self):
        return f'Ola eu sou o {self.__nome}'

class Aquatico(Animal):
    def __init__(self, nome ):
        super().__init__(nome)

    def nadar(self):
        return f'{self._Animal__nome} is swimming'

    def cumprimentar(self):
        return f'HOla que tal Yo soy {self._Animal__nome} del mar'

class Terrestre(Animal):
    def __init__(self, nome ):
        super().__init__(nome)

    def andar(self):
        return f'{self._Animal__nome} is Keep Walking  '

    def cumprimentar(self):
        return f'Animel de Terra :->  {self._Animal__nome} from Ground '

class Pinguim ( Aquatico, Terrestre):
    def __init__(self, nome ):
        super().__init__(nome)

def main ():
    print('-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-')
    baleia = Aquatico('Wally')
    print(baleia.nadar(), '\n', baleia.cumprimentar())
    print('-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-')
    tatu = Terrestre('Xim')
    print(tatu.andar(),'\n', tatu.cumprimentar())
    print('-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-')
    pengu = Pinguim('Pen-Pen')
    print(pengu.nadar(),'\n', pengu.nadar(),'\n', pengu.cumprimentar()) ## Method Resolution Order
    print('-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-')
    # Para se verificar se um objeto é instancia de algo a mais :
    print(f'{pengu._Animal__nome} é instancia de Pinguim  ? {isinstance(pengu, Pinguim)}')
    print(f'{pengu._Animal__nome} é instancia de Aquatico ? {isinstance(pengu, Aquatico)}')
    print(f'{pengu._Animal__nome} é instancia de Terrestre? {isinstance(pengu, Terrestre)}')
    print(f'{pengu._Animal__nome} é instancia de Animal   ? {isinstance(pengu, Animal)}')
    print(f'{pengu._Animal__nome} é instancia de Object   ? {isinstance(pengu, object)}')

## e é aqui que a brincadeitra começa
if __name__ == '__main__':
    main()
