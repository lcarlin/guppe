# Exercicio 2
class Pessoa:
    def __init__(self, nome, idade, altura):
        self.__nome = nome
        self.__idade = idade
        self.__altura = altura

    def get_nome(self):
        return self.__nome

    def get_idade(self):
        return self.__idade

    def get_altura(self):
        return self.__altura

    def set_nome(self, nome):
        self.__nome = nome

    def set_idade(self, idade):
        self.__idade = idade

    def set_altura(self, altura):
        self.__altura = altura

    def mostrar_valores(self):
        print(f"Olá {self.__nome} sua idade é {self.__idade} e sua altura é {self.__altura}")


class Agenda:
    __contatos = []

    def armazenar_pessoa(self, pessoa):
        if len(self.__contatos) < 10:
            self.__contatos.append(pessoa)
        else:
            print("Não é possivel adicionar mais nenhuma pessoa")

    def remover_pessoa(self, nome):
        for pessoa in self.__contatos:
            if pessoa.get_nome() == nome:
                self.__contatos.remove(pessoa)
                print("Pessoa removida")
                return True
        print("Pessoa não encontrada")
        return False

    def buscar_pessoa(self, nome):
        for pessoa in self.__contatos:
            if pessoa.get_nome() == nome:
                print(f"Pessoa encontrada está na posição {self.__contatos.index(pessoa)}")
                return True
        print("Pessoa não encontrada")
        return False

    def imprimir_agenda(self):
        for pessoa in self.__contatos:
            print(f"------------  {self.__contatos.index(pessoa)}  ------------")
            print(f"Nome: {pessoa.get_nome()}")
            print(f"Idade: {pessoa.get_idade()}")
            print(f"Altura: {pessoa.get_altura()}")

    def imprimir_pessoa(self, posicao):
        if 0 <= posicao < len(self.__contatos):
            print(f"Nome: {self.__contatos[posicao].get_nome()}")
            print(f"Idade: {self.__contatos[posicao].get_idade()}")
            print(f"Altura: {self.__contatos[posicao].get_altura()}")
            return True
        else:
            print("Posição não existente")
            return False