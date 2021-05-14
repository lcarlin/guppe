"""
Seção 20: TEste com Python
    02 - Por que Testar os Cóodigos ??? ?? ?
    Testes automátizados

====================================================================================================================
----------------------------------
/       Frontend e BackEnd       |
---------------------------------
|     TEstes automatizados      |
--------------------------------
====================================================================================================================
Porque Testar nosso codigo?
    -   Reduzir BUGUES no cóodigo que existe
    -   Garantem que novos recursos de vossa aplicação não quebrem (alterem) recursos antigos
    -   Garantem que Bugues qur foram corrigidos anteriormente continuem corrigidos
    -   Garantem que a ReFatoração que costumamos a fazer não tragam novos problemas
====================================================================================================================
TDD -   Test Driven Development (Desenvolvimento Guiado por Testes)
    com TDD é utilizados estagios de desenvolvimento
        -   Primeiro é escrito o cenário minimo de teste
        -   Então é escritoo código com o minimo suficiente para fazer o testes passar (executar com sucesso)
        -   O Código é refatorado para realizar a funcionalidade de modo completo
        -   Uma vez que o testes passe, op recurso é considerado completo

Estes estágios de dewsenvolvimento de TDDD são quase como um mantra entre os DEVs, conhecidos como
    -   RED
    -   GREEN
    -   REFACTOR
====================================================================================================================
====================================================================================================================
====================================================================================================================
====================================================================================================================
====================================================================================================================
====================================================================================================================
====================================================================================================================
====================================================================================================================
====================================================================================================================
====================================================================================================================
====================================================================================================================
"""
class Gato:
    def __init__(self, nome ):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def miar(self):
        print(f'{self.__nome} is miando ')


def main():
    print('-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-')
    felix = Gato('felix')
    felix.miar()
    print(felix.nome)
    print('===========================================================')
    print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    print('-----------------------------------------------------------')
    print('***********************************************************')

## e é aqui que a brincadeitra começa
if __name__ == '__main__':
    main()
