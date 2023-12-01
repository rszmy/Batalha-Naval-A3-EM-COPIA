from Enum import Enum 

from src.persistencia.TopicoDB import TopicoDB
from src.persistencia.jogador_db import JogadorDB

from src.persistencia.TopicoDB import TopicoDB
from src.persistencia.jogador_db import JogadorDB

class TopicoControladorErro(Enum):
    JOGADOR_NAO_EXISTENTE = 0 
    #======================================== retorna erro caso o jogador não esteja registrado e tente se inscrever


class TopicoControlador:
    
    def listar_topicos():
        pass

    def criar_novo_topico(nome):
        pass

    def remover_topico(nome):
        pass

    def subscribe(nome_topico, nome_jogador):
        jogador : jogador = JogadorDB.get_by_name(nome_jogador)

        if(jogador != None):
            return TopicoDB.subscribe(nome_topico, jogador)
        else:
            return TopicoControladorErro.JOGADOR_NAO_EXISTENTE
    
    def unsubscribe(nome_topico, nome_jogador):    
        jogador : jogador = JogadorDB.get_by_name(nome_jogador)
        if(jogador != None):
            return TopicoDB.unsubscribe(nome_topico, jogador)
        else:
            return TopicoControladorErro.JOGADOR_NAO_EXISTENTE