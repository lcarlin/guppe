# -*- coding: cp1252 -*-

class Pessoa():
    totalPessoas = 0

    def __init__(self, nome):
        self.__nome = nome

        @property ## Getter para o nome
        def nome(self):
            return self.__nome

        @nome.setter ## Setter para o nome
        def nome(self, novo_nome):
            self.__nome = novo_nome

    def print_pessoa(self):
        return f'{self.__nome} ; ' # {self.__idade} ; {self.__altura} ; {self.__sexo} ; {self.__genero} ; {self.__idade}'

print('-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-')
pessoa = Pessoa('Aleister Crowley')
print(pessoa.print_pessoa())
print(pessoa.nome )
pessoa.nome = 'NovoNOme'
print(pessoa.print_pessoa())


print('-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-')







