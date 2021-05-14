class Robo:
    def __init__(self, nome, bateria=100, habilidades = []):
        self.__nome = nome
        self.__bateria = bateria
        self.___habilidades = habilidades

    @property
    def nome (self):
        return self.__nome

    @property
    def bateria(self):
        return self.__bateria

    @property
    def habilidades(self):
        return self.___habilidades

    def carregar(self):
        self.__bateria = 100

    def diz_nome (self):
        if self.__bateria > 0 :
            self.__bateria -= 1
            return f'BEEP BOOP BEEP BOOP EU SO O {self.__nome.upper()}'
        else:
            return 'Bateria Fraca. Por favor recarrega e tente novamente'

    def aprender_habilidade (self, nova_habilidade, custo):
        if self.__bateria > custo:
            self.__bateria -= custo
            self.___habilidades.append(nova_habilidade)
            return f'Uau! Eu aprendi algo novo: `{nova_habilidade.upper()}'
        return 'Bateria Insuficiente. Por favor recarrege e tenta divovo '
