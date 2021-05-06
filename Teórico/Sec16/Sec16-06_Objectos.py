"""
Progamação Orientada à Objetas - POO
Objetos -> são Intancias das clases ou seja, aopos o mapeamento do Objeto do mundo real para a sua representação
computacional, devemos poder criar quantos objetos forem necessários. Podemos pensar nos Objetos/Instancias de
uma classe como variaveis do tipo definido na classe
====================================================================================================================
lamp1 = Lampada('branca', 110, 60)
cc1 = ContCorrente(5000, 20000)
user1 = Usuario('Christie', 'Monteiro', 'bishoujo@koptobukyia.com', '123456')

print(f'A lampda está ligada ? {lamp1.checa_lampada()}')
lamp1.ligar_desligar()
print(f'A lampda está ligada ? {lamp1.checa_lampada()}')
====================================================================================================================
====================================================================================================================
====================================================================================================================
====================================================================================================================
"""
print('-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-')
from passlib.hash import pbkdf2_sha256 as cripto


class Lampada:
    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False

    def checa_lampada(self):
        return self.__ligada

    def ligar_desligar(self):
        self.__ligada = not self.__ligada


class Cliente:
    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf

    def diz(self):
        print(f'O Cliente {self.__nome} está a dizer : OIÊ !!!')


class ContaCorrente():
    contador = 4999

    def __init__(self, limite, saldo, cliente):
        self.__numero = ContaCorrente.contador + 1
        self.__limie = limite
        self.__saldo = saldo
        self.__cliente = cliente
        ContaCorrente.contador = self.__numero

    def mostra_cliente(self):
        print(f'O cliente é :-> {self.__cliente._Cliente__nome}')


class Usuario():
    contador = 0

    @classmethod
    def conta_usuario(cls):
        print(f'Temos {cls.contador} usuarios ')

    @classmethod
    def ver(cls):
        print('v1.0')

    @staticmethod
    def definicao():
        return 'UXR344'

    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__senha = cripto.hash(senha, rounds=200000, salt_size=16)
        self.__email = email
        Usuario.contador = self.__id
        print(f'Usuário criado : {self.__gera_usuario()}')

    def __correr__(self, metros):
        print(f'{self.__nome} está à correr {metros}  metros')

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    def checa_senha(self, senha):
        if cripto.verify(senha, self.__senha):
            return True
        return False

    def __gera_usuario(self):
        return self.__email.split('@')[0]


cli1 = Cliente('Luizão GarGaMel ', '21278502890')
cc = ContaCorrente(5000, 1000, cli1)

cc.mostra_cliente()
cc._ContaCorrente__cliente.diz() ## essa é uma pessima madeira de fazer acesso ao MEtodo
