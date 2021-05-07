# 3 - Elevador

class Elevador:

    def __init__(self, capacidade, andares):
        self.capacidade = capacidade
        self.andares = andares
        self.pessoas = 0
        self.andar = 0

    @property
    def capacidade(self):
        return self._capacidade

    @capacidade.setter
    def capacidade(self, valor):
        if isinstance(valor, str):
            valor = int(valor.replace('', ''))

        self._capacidade = valor

    @property
    def andares(self):
        return self._andares

    @andares.setter
    def andares(self, valor):
        if isinstance(valor, str):
            valor = int(valor.replace('', ''))

        self._andares = valor

    def entrar(self):
        if self.capacidade > self.pessoas:
            self.pessoas += 1
            print(f'Uma pessoa entrou. A quantidade de pessoas no elevador é {self.pessoas}.')
        else:
            print(f'ERRO: O elevador já está cheio.')

    def sair(self):
        if self.pessoas != 0:
            self.pessoas -= 1
            print(f'Alguém saiu. A quantidade de pessoas no elevador é {self.pessoas}.')
        else:
            print(f'O elevador já está vazio.')

    def subir(self):
        if self.andares > self.andar:
            self.andar += 1
            print(f'O elevador subiu 1 andar. Estamos no andar {self.andar}.')
        else:
            print('Já estamos no último andar...')

    def descer(self):
        if self.andar != 0:
            self.andar -= 1
            print(f'O elevador desceu 1 andar. Estamos no andar {self.andar}.')
        else:
            print('Já estamos no terréo...')