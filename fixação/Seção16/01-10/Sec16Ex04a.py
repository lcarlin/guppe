class Televisao:

    def __init__(self):
        self.__canal = 1  # atributo privado
        self.volume = 0  # atributo público


class ControleRemoto:

    def __init__(self):
        pass

    def aumentarVolume(self):
        self.volume += 1  # Repare que o self sempre chama o atributo do Objeto! e não da classe, nessa linha eu tofalando #Objeto vai no seu atributo volume e atualize ele.

    def diminuirVolume(self):
        self.volume -= 1

    def aumentarCanal(self):
        # self.__canal += 1 # Se eu chamar assim vai dar erro, por quê ? porque eu estou querendo modificar um atributo,
        # mas eu não to na mesma classe do objeto, o python vai e bloqueia, por isso vou ter que usar o Name Mangling
        self._Televisao__canal += 1

    def diminuirCanal(self):
        self._Televisao__canal -= 1

    def mudarCanal(self, canal):
        self._Televisao__canal = canal

    def consultarVolume(self):
        print(f'O volume da tv é {self.volume}')  # lembrando atributo público é mais fácil referenciar em outra classe

    def consultarCanal(self):
        print(f'O canal da tv é {self._Televisao__canal}')


# Testando
televisao = Televisao()

ControleRemoto.aumentarVolume(televisao)

print(televisao.__dict__)

ControleRemoto.diminuirVolume(televisao)
print(televisao.__dict__)

ControleRemoto.aumentarCanal(televisao)
print(televisao.__dict__)

ControleRemoto.diminuirCanal(televisao)
print(televisao.__dict__)

ControleRemoto.mudarCanal(televisao, 35)
print(televisao.__dict__)

ControleRemoto.consultarVolume(televisao)
ControleRemoto.consultarCanal(televisao)