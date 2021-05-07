"""
Crie uma classe Agenda que pode armazenar 10 pessoas e seja capaz de realizar as seguintes operações:

* void armazenaPessoa(String nome, int idade, float altura);                                                     (OK)
* void removePessoa(String nome);                                                                                (OK)
* int buscaPessoa(String nome); // informa em que posição da agenda está a pessoa                                (OK)
* void imprimeAgenda(); // imprime os dados de todas as pessoas da agenda                                        (OK)
* void imprimePessoa(int index); // imprime os dados da pessoa que está na posição "i" da agenda.                (OK)
"""


class Agenda:
    cont = 0
    banco = []

    def __init__(self, nome, idade, altura):
        self.__banco = Agenda.banco
        self.__cont = Agenda.cont + 1
        self.__nome = nome
        self.__idade = idade
        self.__altura = altura
        Agenda.cont = self.__cont
        self.__posicao = 0

    def armazena_pessoa(self):
        user = 'pessoa ' + str(self.__cont)
        pessoa = {user: (self.__nome, self.__idade, self.__altura)}
        self.__banco.append(pessoa)
        return self.__banco

    def remover_pessoa(self, nome):
        """ Separa os dicionários da lista(banco) e acessa os valores, onde estão contido as tuplas. Então,
        por via índice, o nome da pessoa é localizado"""
        self.__banco = Agenda.banco
        indice = 0
        for dicionario in self.__banco:
            if list(dicionario.values())[0][0] == nome:
                break
            else:
                indice += 1
        self.__banco.pop(indice)  # Removendo a pessoa
        self.__banco = Agenda.banco
        print(f'{nome} foi removido')

    def buscar_pessoa(self, nome):
        self.__banco = Agenda.banco
        indice = 0
        compara = 0
        for dicionario in self.__banco:
            if list(dicionario.values())[0][0] == nome:
                compara += 1
                print(f'A Pessoa Está localizada no índice {indice}')
                break
            else:
                indice += 1
        if compara != 1:
            print('Pessoa não encontrada.')

    def imprime_agenda(self):
        self.__banco = Agenda.banco
        for dicionario in self.__banco:
            print(f'nome: {list(dicionario.values())[0][0]}')
            print(f'idade: {list(dicionario.values())[0][1]}')
            print(f'altura: {list(dicionario.values())[0][2]}\n')

    def posicao_pessoa(self, indice):
        self.__banco = Agenda.banco
        self.__posicao = self.__banco[indice]
        nome = list(self.__posicao.values())[0][0]
        idade = list(self.__posicao.values())[0][1]
        altura = list(self.__posicao.values())[0][2]
        print(f'Nome: {nome}\nIdade: {idade}\nAltura: {altura}')


pessoa_1 = Agenda('Luis Gustavo', 21, 1.74)
pessoa_2 = Agenda('Jhenifer Noha', 23, 1.72)
pessoa_3 = Agenda('Larissa Vicente', 42, 1.82)
pessoa_4 = Agenda('Alan Taring', 48, 1.78)
pessoa_5 = Agenda('Cláudia Mendes', 19, 1.59)
pessoa_6 = Agenda('Alice Matos', 28, 1.75)
pessoa_7 = Agenda('Sérgio Vicente', 57, 1.73)
pessoa_8 = Agenda('Alan Silva', 21, 1.92)
pessoa_9 = Agenda('Eulayla Monteiro', 19, 1.70)
pessoa_10 = Agenda('João Pedro', 21, 1.73)

Agenda.armazena_pessoa(pessoa_1)
Agenda.armazena_pessoa(pessoa_2)
Agenda.armazena_pessoa(pessoa_3)
Agenda.armazena_pessoa(pessoa_4)
Agenda.armazena_pessoa(pessoa_5)
Agenda.armazena_pessoa(pessoa_6)
Agenda.armazena_pessoa(pessoa_7)
Agenda.armazena_pessoa(pessoa_8)
Agenda.armazena_pessoa(pessoa_9)
Agenda.armazena_pessoa(pessoa_10)

print(Agenda.banco, '\n')

# Remover Pessoa:
nome_remover = input('Digite o nome da pessoa a ser removida: ')
try:
    Agenda.remover_pessoa(pessoa_10, nome_remover)
    print(Agenda.banco)
except IndexError:
    print('A pessoa não encontra-se no banco de dados.')

# Buscar a posição da agenda da pessoas:
nome_busca = input('Digite o nome da pessoa a ser encontrada: ')
Agenda.buscar_pessoa(pessoa_10, nome_busca)

# Mostrar os dados das Pessoas:
Agenda.imprime_agenda(pessoa_10)

# Imprime os dados da pessoa que está na posição "i" da agenda
Agenda.posicao_pessoa(pessoa_10, 5)