""""
nomes: list = ['Geek', 'University']
versoes: tuple = [3,4,7]
opcoes: dict = {'ar': True, 'banco_couro': True}
valores: set = {2,3,4,5,6}
print(__annotations__)

from typing import Dict, List, Tuple, Set
nomes: List[str] = [ 'Geek' , 'University']
versoes: Tuple[int, int, int] = [3,4,7]
opcoes: Dict[str, bool] = {'ar': True, 'banco_couro': True}
valores: Set[int] = {2,3,4,5,6}
print(nomes)
print(versoes)
print(opcoes)
print(valores)
print(__annotations__)
https://www.alt-codes.net/suit-cards.php
"""
import random
NAIPES = '♠ ♡ ♣ ♢'.split()
CARTAS  = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

def criar_baralho (aleatorio: bool = False) -> list:
    """Criar um baraleo de 52 cards"""
    baralho = [(n, c) for c in CARTAS for n in NAIPES]
    if aleatorio:
        random.shuffle(baralho)
    return baralho

def distribuir_cartas(baralho: list) -> tuple:
    """Gerencia a mão de cartas de acordo com o caralho gerado """
    return (baralho[0::4],baralho[1::4], baralho[2::4], baralho[3::4])

def jogar():
    """Iniciar um jogo de cartas pra  4 players"""
    cartas: list = criar_baralho(aleatorio=True)
    jogadores: list = 'P1 P2 P3 P4'.split()
    maos: dict = {J: m for J, m in zip (jogadores, distribuir_cartas(cartas))}
    for jogador, cartas in maos.items():
        carta = ' '.join(f"{j}{c}" for (j, c) in cartas)
        print(f'{jogador}: {carta}')

#baraio = criar_baralho()
#print(distribuir_cartas(baraio))

if __name__ == '__main__' :
    jogar()

