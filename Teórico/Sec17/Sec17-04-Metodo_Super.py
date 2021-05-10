"""
Seção 17 -
*   Metodo Super()
Refere-se à superClasse que dá a herança aos
====================================================================================================================
====================================================================================================================
====================================================================================================================
====================================================================================================================
====================================================================================================================
====================================================================================================================

"""
class Animal:
    def __init__(self,nome, especie):
        self.__nome = nome
        self.__especie = especie

    def faz_som(self,som ):
        print(f'O {self.__nome} faz {som}')

class Gato(Animal):
    def __init__(self, nome, especie , raca ):
        #Animal.__init__(self, nome, especie)  # possiverl, porem não recomendado
        super().__init__(nome, especie)  # esse é o quente , recomendado 1
        # com super() consigo fazer aceso aà qualquer elemento da classe PAI
        self.__raca = raca


def main ():
    print('-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-')
    felix = Gato('Felix', 'Felino', 'Agorá')
    felix.faz_som('mi-au')


## e é aqui que a brincadeitra começa
if __name__ == '__main__':
    main()
