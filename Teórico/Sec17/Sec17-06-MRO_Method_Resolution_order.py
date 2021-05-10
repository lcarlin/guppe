"""
Seção 17 -
*   Method Resolution Order
Resolução de Ordem de Metodos é a ordem de execução dos Metodos , ou seja, quem será executado 1º
Em Python podemos conferir a ordem de execução dos Methods de 3 formas
    -   Via Propriedade da classe __mro__
    -   Via Metodo mro()
    -   Via Help
====================================================================================================================
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
    pengu = Pinguim('Pen-Pen')
    print(pengu.nadar(), '\n', pengu.nadar(), '\n', pengu.cumprimentar())  ## Method Resolution Order
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
