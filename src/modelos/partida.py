from modelos.tabuleiro import Tabuleiro
from modelos.jogador import Jogador
import itertools

class Partida():

    _id : int
    _jogador_a : Jogador
    _jogador_b : Jogador
    _tabuleiro : Tabuleiro
    _turno : int

    id_obj = itertools.count(1)

    def __init__(self, jogador_a: Jogador, jogador_b: Jogador):
        self._id = next(Partida.id_obj)
        self._jogador_a = jogador_a
        self._jogador_b = jogador_b
        self._tabuleiro = Tabuleiro()
        self._turno = 1