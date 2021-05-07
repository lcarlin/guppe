class Elevador:
    pessoas = 0
    andar_atual = 0

    def __init__(self, andares, capacidade):
        self.__andares = andares
        self.__capacidade = capacidade

    def entra(self):
        if Elevador.pessoas < self.__capacidade:
            Elevador.pessoas += 1
            return f'Entrou uma pessoa no elevador.\nHá agora {Elevador.pessoas} pessoas no elevador'
        else:
            return 'ELEVADOR LOTADO!!'

    @classmethod
    def sai(cls):
        if cls.pessoas > 0:
            cls.pessoas -= 1
            return f'Saiu uma pessoa no elevador.\nHá agora {cls.pessoas} pessoas no elevador'
        else:
            return 'ELEVADOR VAZIO!!'

    def sobe(self):
        if Elevador.andar_atual < self.__andares:
            Elevador.andar_atual += 1
            return f'O elevador subiu um andar.\nAgora o elevador está no andar nº {Elevador.andar_atual}'
        else:
            return 'ESTAMOS NO ÚLTIMO ANDAR'

    @classmethod
    def desce(cls):
        if cls.andar_atual > 0:
            cls.andar_atual -= 1
            return f'O elevador desceu um andar.\nAgora o elevador está no andar nº {cls.andar_atual}'
        else:
            return 'ESTAMOS NO TÉRREO'


elevador = Elevador(20, 6)