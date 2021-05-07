# 3 - ELEVADOR
"""
Crie uma classe denominada Elevador para armazenar as informações de um elevador dentro de um prédio. A classe dever
armazenar o andar atual (térreo = 0), total de andares no prédio, excluindo o térreo, capacidade do elevador,
e quantas pessoas presentes nele

    @ A classe deve também disponibilizar os seguintes métodos:

 # Inicializa: que deve receber como parâmetros a capacidade do elevador e o
   total de andares no prédio (os elevadores sempre começam no térreo e vazio);

 # Entra: para acrescentar uma pessoa no elevador (só deve acrescentar se ainda
   houver espaço);

 # Sai: para remover uma pessoa do elevador (só deve remover se houver alguém dentro dele);

 # Sobe: para subir um andar (não deve subir se já estiver no último andar);

 # Desce: para descer um andar (não deve descer se já estiver no térreo);

 # Encapsular todos os atributos da classe (criar os métodos set e get).

"""


class Elevador:

    def __init__(self, total_andares, capacidade):
        self.__total_andares = total_andares
        self.__capacidade = capacidade
        self.__andar_atual = 0
        self.__presentes = 0

    def enta(self):
        if self.__presentes < self.__capacidade:
            self.__presentes += 1
        else:
            print('Capacidade máxima atingida!')

    def sai(self):
        if self.__presentes > 0:
            self.__presentes -= 1
        else:
            print('Elevador vázio!')

    def sobe(self):
        if self.__andar_atual < self.__total_andares:
            self.__andar_atual += 1
        else:
            print('O elevador encontra-se no último andar')

    def desce(self):
        if self.__andar_atual > 0:
            self.__andar_atual -= 1
        else:
            print('O elevador encontra-se no térreo')

    # Getters
    def get_andar_atual(self):
        return self.__andar_atual

    def get_total_andares(self):
        return self.__total_andares

    def get_capacidade(self):
        return self.__capacidade

    def get_presentes_elevador(self):
        return self.__presentes

    # Setters
    def set_andar_atual(self, andar):
        self.__andar_atual = andar

    def set_total_andares(self, total):
        self.__total_andares = total

    def set_capacidade(self, capacidade):
        self.__capacidade = capacidade

    def set_presentes_elevador(self, presentes):
        self.__presentes = presentes