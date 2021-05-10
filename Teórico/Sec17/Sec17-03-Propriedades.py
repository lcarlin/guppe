"""
Seção 17 -
*   Propriedades
Em linguagens como Java, ao declarar atributos privados nas classes, costummos criar metodos publicos para a
minipulacao desses atributos. Esses metodos são conhecidos como Getters e Setters ( Get -> Pega Valor; Set -> Altera)
Sempre criar os atributos de forma privada e criar os Gettters e setters ( no formato de PROPERTY e não funçoes analogas
a java )
====================================================================================================================
class Conta:
    contador = 0
    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador = self.__numero

    def extrato (self):
        return f'Saldo de {self.__saldo} do cliente {self.__titular}'

    def depositar (self, valor):
        self.__saldo += valor

    def sacar (self,valor):
        self.__saldo -+ valor

    def transferir(self, valor, destino ):
        self.__saldo -= valor
        destino.__saldo += valor

    def get_numero (self):
        return  self.__numero

    def get_titular (self):
        return self.__titular

    def get_saldo (self):
        return self.__saldo

    def get_limite(self):
        return self.__limite

    def set_titular (self, novo_titular ):
        self.__titular = novo_titular

    def set_limite(self, novo_limite):
         self.__limite = novo_limite

def main ():
    print('-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-')
    conta1 = Conta('Bat Girl', 3100, 5000 )
    conta2 = Conta('HArley Quinn', 2200,4000)

    print(conta1.extrato())
    print(conta2.extrato())
    print('-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-')
    # soma_total = conta1._Conta__saldo + conta2._Conta__saldo
    soma_total = conta1.get_saldo() + conta2.get_saldo()
    print(f' Soma dos saldos das 2 contas :-> {soma_total}')

    print('-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-')
    print(conta1.__dict__)
    conta1.set_limite(9999)
    print(conta1.__dict__)



## e é aqui que a brincadeitra começa
if __name__ == '__main__':
    main()

====================================================================================================================
====================================================================================================================
====================================================================================================================
====================================================================================================================
====================================================================================================================
"""
class Conta:
    contador = 0
    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador = self.__numero + 1

    def extrato (self):
        return f'Saldo de {self.__saldo} do cliente {self.__titular}'

    def depositar (self, valor):
        self.__saldo += valor

    def sacar (self,valor):
        self.__saldo -+ valor

    def transferir(self, valor, destino ):
        self.__saldo -= valor
        destino.__saldo += valor

    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, novo_limite):
        self.__limite = novo_limite

    @titular.setter
    def titular(self, novo_titular):
        self.__titular = novo_titular

    @property
    def valor_total(self):
        return self.__saldo + self.__limite



def main ():
    print('-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-')
    conta1 = Conta('Bat Girl', 3100, 5000 )
    conta2 = Conta('HArley Quinn', 2200,4000)

    print(conta1.extrato())
    print(conta2.extrato())
    print('-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-')
    # soma_total = conta1._Conta__saldo + conta2._Conta__saldo
    soma_total = conta1.saldo + conta2.saldo
    print(f' Soma dos saldos das 2 contas :-> {soma_total}')

    print('-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-')
    print(conta1.__dict__)
    conta1.limite = 76543
    print(conta1.__dict__)
    print(conta1.valor_total)






## e é aqui que a brincadeitra começa
if __name__ == '__main__':
    main()
