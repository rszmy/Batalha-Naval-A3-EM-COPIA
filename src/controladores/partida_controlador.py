from persistencia.partida_db import PartidaDB
from controladores.tabuleiro_controlador import TabuleiroControlador
from controladores.jogador_controlador import JogadorControlador

class PartidaControlador:

    @classmethod
    def começar_nova_partida(cls, jogador_a: object, jogador_b: object):
        PartidaDB().get_instance().começar_nova_partida(jogador_a, jogador_b)
        id = cls.pegar_id_por_jogador(jogador_a)
        tabuleiro = cls.pegar_tabuleiro_por_id(id)
        TabuleiroControlador.definir_embarcacoes_para_colocar(tabuleiro)

    @classmethod
    def listar_partidas(cls):
        return PartidaDB().get_instance().listar_partidas
    
    @classmethod
    def checar_jogador_em_partida(cls, nome_jogador: str):
        return PartidaDB().get_instance().checar_jogador_em_partida(nome_jogador)

    @classmethod
    def pegar_id_por_jogador(cls, jogador_a: object):
        return PartidaDB.get_instance().pegar_id_por_jogador(jogador_a)
    
    @classmethod
    def pegar_tabuleiro_por_id(cls, id: int):
        return PartidaDB.get_instance().pegar_tabuleiro_por_id(id)
    
    @classmethod
    def pegar_nome_jogador_por_id(cls, id: int, id_jogador: str):
        return PartidaDB.get_instance().pegar_nome_jogador_por_id(id, id_jogador)
    
    @classmethod
    def pegar_status_por_id(cls, id: int):
        return PartidaDB.get_instance().pegar_status_por_id(id)

    @classmethod 
    def atualizar_status_por_id(cls, id: int, novo_status: str):
        return PartidaDB.get_instance().atualizar_status_por_id(id, novo_status)

    @classmethod
    def pegar_turno_por_id(cls, id: int):
        return PartidaDB.get_instance().pegar_turno_por_id(id)

    @classmethod
    def pegar_representacao_tabuleiro_partida(cls, id: int, nome_jogador: str):
        tabuleiro = cls.pegar_tabuleiro_por_id(id)

        rep_list = []

        jogador_a = cls.pegar_nome_jogador_por_id(id, "a")
        jogador_b = cls.pegar_nome_jogador_por_id(id, "b")

        if (jogador_a == nome_jogador):
            rep_tabuleiro = TabuleiroControlador.pegar_tabuleiro_por_parte(tabuleiro, "a")
            rep_camuflado = TabuleiroControlador.pegar_tabuleiro_camuflado_por_parte(tabuleiro, "b")
        elif (jogador_b == nome_jogador):
            rep_tabuleiro = TabuleiroControlador.pegar_tabuleiro_por_parte(tabuleiro, "b")
            rep_camuflado = TabuleiroControlador.pegar_tabuleiro_camuflado_por_parte(tabuleiro, "a")
        else: 
            return {"message": "Jogador não pertence ao jogo"}
        
        rep_list.append(rep_tabuleiro)
        rep_list.append(rep_camuflado)

        return rep_list
    
    @classmethod
    def colocar_embarcacao_tabuleiro(cls, id: int, nome_jogador: str, embarcao: str, coord_x: str, coord_y: int, orientacao: str):
        tabuleiro = cls.pegar_tabuleiro_por_id(id)

        jogador_a = cls.pegar_nome_jogador_por_id(id, "a")
        jogador_b = cls.pegar_nome_jogador_por_id(id, "b")

        if (jogador_a == nome_jogador):
            return TabuleiroControlador.colocar_embarcacoes_no_tabuleiro(tabuleiro, "a", embarcao, coord_x, coord_y, orientacao)
        elif (jogador_b == nome_jogador):
            return TabuleiroControlador.colocar_embarcacoes_no_tabuleiro(tabuleiro, "b", embarcao, coord_x, coord_y, orientacao)
        else: 
            return {"message": "Jogador não pertence ao jogo"}