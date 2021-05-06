"""
Progamação Orientada à Objetas - POO
Abstração e o Encapsulamento de coisas
O Grande objetivo da POO é encapsular nosso codigo dentro deum grupo logico e hierárcico utilizando classes.
Encapsular -> Capsula
====================================================================================================================
           classe
----------------------------------
|        atributos e metodos     |
----------------------------------
# Relembrando : atributos/metodos privados em Python
IMagine que temos uma classe que se chama pessoa, contendo um atributo privado __Nome e um metodo
   privado chamado __falar()
esses elementos privados somente deveriam ser acessados atraves da claasse. Mas python NÃO bloqueia este acesso fora
da classe. COm python acontece um fenomeno chamado Name Mangling que faz uma aloteração na forma de se acessar
os elementos privados conforme:
_Classe__elemento
exemplo  Acessando elementos privados fora da classe - ISSO É RUIM
instacia._Pessoa__nome
instancia_Pessoa__falar()

Abstração em POO é o ato de expor apenas dados relevantes de uma classe, escondendo atributos e metodos privados
de usuário .
====================================================================================================================

class Conta:
    contador = 400
    def __init__(self, titular, saldo, limite):
        self.numero = Conta.contador + 1
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        Conta.contador = self.numero

    def extrato(self) :
        print(f'E o saldo do titular {self.titular} com limite de {self.limite} é de  {self.saldo}')

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        self.saldo -= valor

# Testando
conta1 = Conta('Geek', 150.00, 10000)
print(conta1.titular)
print(conta1.saldo)
print(conta1.limite)
print(conta1.numero)
conta1.extrato()
conta1.saldo = 150000
conta1.limite = 150000
conta1.numero = 4
conta1.titular = 'XuXa'

conta1.extrato()

print(conta1.__dict__)

====================================================================================================================
conta1 = Conta('Geek', 150.00, 10000)
print(conta1.__dict__)
conta1._Conta__titular = 'Jaspion'
print(conta1.__dict__)
====================================================================================================================
conta1 = Conta('Geek', 150.00, 10000)
print(conta1.__dict__)
conta1.depositar(500)
conta1.sacar(36987)

print(conta1.__dict__)
====================================================================================================================
====================================================================================================================
====================================================================================================================
"""
print('-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-')


class Conta:
    contador = 400
    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador = self.__numero

    def extrato(self) :
        print(f'E o saldo do titular {self.__titular} com limite de {self.__limite} é de  {self.__saldo}')

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print(f'O valor tem que ser > 0 ')

    def sacar(self, valor):
        if self.__saldo >= valor:
            if valor > 0:
                self.__saldo -= valor
            else:
                print(f'O valor tem que ser > 0 ')
        else:
            print('Saldo Insulficintes')

    def transferir(self, valor, destino):
        # 1 remover o valor da conta de origem
        self.__saldo -= valor
        self.__saldo -= 10 # taxa de transferencia para pelo solicitante

        destino.__saldo += valor




conta1 = Conta('Geek', 15000, 10000)
conta1.extrato()

conta2 = Conta('Jaspion ', 810, 10000)
conta2.extrato()
print('-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-')
conta2.transferir(100, conta1)
conta1.extrato()
conta2.extrato()