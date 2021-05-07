class Televisao:
    def __init__(self, canal=1, volume=1):
        self.canal = canal
        self.volume = volume

    def get_canal(self):
        return self.canal

    def set_canal(self, valor):
        self.canal = valor

    def controla_volume(self, valor):
        if self.volume + valor <= 10 and self.volume + valor >= 0:
            self.volume += valor
        elif self.volume + valor > 10:
            self.volume = 10
        else:
            self.volume = 0
        print(self.volume)

    def controla_canal(self, valor):
        if self.canal + valor >= 1 and self.canal + valor <= 8:
            self.canal += valor
        elif self.canal + valor > 8:
            self.canal = 1
        else:
            self.canal = 8
        print(self.canal)


class ControleRemoto():
    def __init__(self, televisao):
        self.televisao = televisao

    def aumenta_volume(self):
        self.televisao.controla_volume(+1)

    def diminui_volume(self):
        self.televisao.controla_volume(-1)

    def aumenta_canal(self):
        self.televisao.controla_canal(+1)

    def diminui_canal(self):
        self.televisao.controla_canal(-1)

    def troca_canal(self, valor):
        if valor > 0 and valor < 20:
            print(valor)
            self_canal = valor
            Televisao.set_canal(self, valor)
        else:
            print(f'ERRO')