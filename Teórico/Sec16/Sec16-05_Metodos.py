"""
Progamação Orientada à Objetas - POO
- Metodos( funções) -> representam os comportamentos do Objeto ou Seja as ações quye este objeto pode realizar no seu
    Sistema

EmPython, dividimos os metodos 2 2 grupos : MEtodos e instancia e Metodos de classe
# Metodos de Instancia:
# O metodo __init__ é um metodo especial chamado de construtor e a sua função é criar/construir um novo Objeto com
    base nas definiçoes da classe Pai.

Todo elemento em Pyhton que inicia e finaliza com " __ " é chamado de Dunder (Double Under LIne )
Os MEtodos DUNDER em Python são chamados de Métodos Magicos
# Atenção por mais que possamos criar nossas funções Dunder (Inicio e fim) NÃO É ACONHSELHAVE.
Python possui vários metodos com essa forma de nomenclatura e pode ser que mudemos o comportamento dessas funçoes
mágicas internas da LInguagem, Então evite ao máximo . De preferencia nunca crie metodos __Nome__ , talkey ?

# Metodos são escritos em letras minusculas. Se o nome for composto, o Nome tera as palavras separadas por " _ "

# Metodos de classes em Python são conehcidos como Métodos estáticos em outras liunguagens
====================================================================================================================

p1 = Produto('Playstation 5 ', 'Video-Gueime', 8489.00)

print(p1.desconto(50))

print(Produto.desconto(p1, 15))

user1 = Usuario('Emma', 'Frost', 'emmafrost@x-men.com', '123456')
user2 = Usuario('Black', 'Widow', 'natasha@avengers.com', '654324')

print(user1.nome_completo())
print(user2.nome_completo())

====================================================================================================================
====================================================================================================================
====================================================================================================================
====================================================================================================================
"""
print('-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-')


class Lampada:
    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False


class ContCorrente():
    contador = 4999

    def __init__(self, numero, limite, saldo):
        self.__numero = ContCorrente.contador + 1
        self.__limie = limite
        self.__saldo = saldo
        ContCorrente.contador = self.__numero


class Produto():
    imposto = 1.05
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id

    def desconto(self, porcentagem):
        """Retorna o valor do produto com o desconto"""
        return (self.__valor * (100 - porcentagem)) / 100


from passlib.hash import pbkdf2_sha256 as cripto


class Usuario():
    contador = 0
    @classmethod
    def conta_usuario(cls):
        print(f'Temos {cls.contador} usuarios ')

    @classmethod
    def ver(cls):
        print('v1.0')

    @staticmethod
    def definicao() :
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


user3 = Usuario('Snipper', 'Wolf', 'bishoujo@kotobukya.com', '987654')
user5 = Usuario('Snipper', 'Wolf', 'bishoujo@kotobukya.com', '987654')
user6 = Usuario('Snipper', 'Wolf', 'bishoujo@kotobukya.com', '987654')

print(user3._Usuario__senha)

if user3.checa_senha('123456'):
    print('Senha certa')
else:
    print(f'Senha Errada')

Usuario.conta_usuario() ## forma certa e correta
user3.conta_usuario()   ## isso não tá certo

print(Usuario.definicao())

print(user6.definicao())