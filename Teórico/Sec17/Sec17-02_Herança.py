"""
Seção 17 - Herança
*   Herança
    A idéia de herança é reaproveitar o Código e também extender nossas classes.
    Com a herança, à partir de uma classe existente nós extendemos outra classe que passa herdar atributyos e métodos
    da classe Herdada (PAI)
cliente
    _   Nome
    -   Sobrenome
    -   CPF
    -   Renda

Funcionario
    -   Nome
    -   Sobrenome
    -   CPF
    -   Matricula

Perguntar: existe alguma entiudade generica o suficiente apra encapsular os atributos e metodos comuns à outras
    entidades?

OBS: qQuando uma classe herda de outra  classe, ela herda TODOS os Atributos e métodos da classe Herdada.

QUando uma classe(filha) Herda de uma classe(Pai)  a classe que fornece a Herança  é conhecida como
        [PEssoa, em nosso exemplo]
    -   Super Classe;
    -   Classe Mae ;
    -   Classe Pai
    -   Classe Base
    -   Classe Genérica

QUando uma classe(filha) Herda de uma classe(Pai)  a classe que HERDADA (derivada) é conhecida como
    [Cliente, Funcionário]
    -   Sub Classe
    -   Classe Filha
    -   Classe Especifica

Sobrescrita de Metodo ocorre quando reescrevemos um método presente na SuperClasse em classes filhas
====================================================================================================================
# V1
class Cliente:
    def __init__(self, nome, sobrenome, cpf, renda):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self._renda = renda

    def nome_completo (self):
        return f'{self.__nome} {self.__sobrenome}'

class Funcionario:
    def __init__(self, nome, sobrenome, cpf, matricula):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__matricula = matricula

    def nome_completo (self):
        return f'{self.__nome} {self.__sobrenome}'

def main():
    cliente1 = Cliente('Star', 'Fire', '123.456.789-00', 5000)
    funcionario1 = Funcionario('Black', 'Widow', '987.654.321-99', 7500)

    print(cliente1.nome_completo())
    print(funcionario1.nome_completo())


## e é aqui que a brincadeitra começa
if __name__ == '__main__':
    main()
====================================================================================================================
class Pessoa:
    ## é INDEX ou INIT ?!?!?!?!?!!?
    def __init__ (self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo (self):
        return f'{self.__nome} {self.__sobrenome}'

class Cliente(Pessoa):
    # Cliente Herda de Pessoa
    def __init__(self, nome, sobrenome, cpf,renda):
        super().__init__(nome, sobrenome, cpf)
        self.__renda = renda

class Funcionario(Pessoa):
     # Funcionario Herda de Pessoa
    def __init__(self,nome, sobrenome, cpf,  matricula):
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula

def main():
    cliente1 = Cliente('Star', 'Fire', '123.456.789-00', 5000)
    funcionario1 = Funcionario('Black', 'Widow', '987.654.321-99', 7500)

    print(cliente1.nome_completo())
    print(funcionario1.nome_completo())
    print('-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-')
    print(funcionario1.__dict__)
    print(cliente1.__dict__)

## e é aqui que a brincadeitra começa
if __name__ == '__main__':
    main()

====================================================================================================================
====================================================================================================================
====================================================================================================================
====================================================================================================================

"""
class Pessoa:
    ## é INDEX ou INIT ?!?!?!?!?!!?
    def __init__ (self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo (self):
        return f'{self.__nome} {self.__sobrenome}'

class Cliente(Pessoa):
    """Cliente Herda de Pessoa"""
    def __init__(self, nome, sobrenome, cpf,renda):
        super().__init__(nome, sobrenome, cpf)
        self.__renda = renda

class Funcionario(Pessoa):
    """ Funcionario Herda de Pessoa"""
    def __init__(self,nome, sobrenome, cpf,  matricula):
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula

    #Aqui o metodo é sobrescrito
    def nome_completo(self):
        return f'Funcionário :->  {self.__matricula}; NOme :-> {super().nome_completo()}'

def main():
    cliente1 = Cliente('Star', 'Fire', '123.456.789-00', 5000)
    funcionario1 = Funcionario('Black', 'Widow', '987.654.321-99', 7500)

    print(cliente1.nome_completo())
    print(funcionario1.nome_completo())
    print('-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-')
    print(funcionario1.__dict__)
    print(cliente1.__dict__)

## e é aqui que a brincadeitra começa
if __name__ == '__main__':
    main()
