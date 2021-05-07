class Televisao:

    def __init__(self, canal=0, volume=10):
        self.canal = canal
        self.volume = volume

    def controle_volume(self, valor):
        self.volume += valor

    def controle_canal(self, valor):
        if valor > 1:
            self.canal = valor
        else:
            self.canal += valor


class ControleRemoto:

    def __init__(self, televisao):
        self.televisao = televisao

    def alterar_volume(self, valor):
        self.televisao.controle_volume(valor)
        print(f'O volume da TV agora é {self.televisao.volume}')

    def alterar_canal(self, valor):
        self.televisao.controle_canal(valor)
        print(f'O canal da TV agora é {self.televisao.canal}')


tv = Televisao()

cr = ControleRemoto(tv)

cr.alterar_volume(1)
cr.alterar_volume(1)
cr.alterar_volume(-1)

cr.alterar_canal(1)
cr.alterar_canal(1)
cr.alterar_canal(-1)
cr.alterar_canal(5)