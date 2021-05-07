# -*- coding: cp1252 -*-

class Pessoa():
    totalPessoas = 0

    def __init__(self, nome, idade, altura, sexo):
        self.__id = Pessoa.totalPessoas + 1
        self.__nome = nome
        self.__idade = idade
        self.__altura = altura
        self.__sexo = sexo

        Pessoa.totalPessoas = self.__id

    def setNome(self, nome):
        self.__nome = nome

    def setIdade(self, idade):
        self.__idade = idade

    def setAltura(self,altura):
        self.__altura = altura

    def setSexo(self, sexo ):
        self.__sexo = sexo

    def getNome(self):
        return self.__nome

    def getIdade(self):
        return self.__idade

    def getAltura(self):
        return self.__altura

    def getSexo(self):
        return self.__sexo


    def print_pessoa(self):
        return f'{self.__id} ; {self.__nome} ; {self.__idade} ; {self.__altura} ; {self.__sexo} '

print('-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-')
pessoa = Pessoa('Aleister Crowley', 75, 170, 'M', )
print(pessoa.print_pessoa())
print('-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-')
pessoa.setSexo('A')
pessoa.setNome('To Mega Therion')
pessoa.setIdade(666)
print(pessoa.print_pessoa())

print('-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-')
print(pessoa.print_pessoa())
print('-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-')
nova_pessoa = Pessoa('Luiz Carlin', 44, 184, 'M')
print(nova_pessoa.print_pessoa())
