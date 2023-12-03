from persistencia.partida_db import PartidaDB
from controladores.tabuleiro_controlador import TabuleiroControlador
from controladores.jogador_controlador import JogadorControlador

class PartidaControlador:

    @classmethod
    def listar_partidas(cls):
        return PartidaDB().get_instance().listar_partidas

    @classmethod
    def começar_nova_partida(cls, jogador_a: object, jogador_b: object):
        PartidaDB().get_instance().começar_nova_partida(jogador_a, jogador_b)
        id = cls.pegar_id_por_jogador(jogador_a)
        tabuleiro = cls.pegar_tabuleiro_por_id(id)
        TabuleiroControlador.definir_embarcacoes_para_colocar(tabuleiro)

    @classmethod
    def pegar_id_por_jogador(cls, jogador_a: object):
        return PartidaDB.get_instance().pegar_id_por_jogador(jogador_a)
    
    @classmethod
    def pegar_tabuleiro_por_id(cls, id: int):
        return PartidaDB.get_instance().pegar_tabuleiro_por_id(id)