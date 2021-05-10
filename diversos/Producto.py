## https://www.youtube.com/watch?v=PGXwNophTOQ
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto (self, percentual):
        self.preco = self.preco - (self.preco * (percentual / 100 ))

    # Getters note que o nome do metodo Getter é o mesmo da variavel
    # e por isso, o nome do atributo foi acrescido de _
    @property
    def preco (self):
        print('   *** Acessando o atributo preco de forma INDIRETA')
        return self._preco

    #Setter
    @preco.setter
    def preco(self, valor ):
        if isinstance(valor, str ):
            valor = float(valor.replace('R$',''))

        self._preco = valor

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        self._nome = valor.title()

def main() :
    print('-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-')
    p1 = Produto('camisete',65)
    p1.desconto(15)
    print(p1.nome)
    print(p1.preco)

    print('-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-')
    p2 = Produto('Caneca LInux', 36)
    p2.desconto(17)

    print(p2.nome)
    print(p2.preco)

if __name__ == '__main__':
    main()