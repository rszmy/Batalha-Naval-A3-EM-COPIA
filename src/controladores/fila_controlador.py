from persistencia.fila_db import FilaDB
from jogador_controlador import JogadorControlador
from enum import Enum 

class TopicoControladorErro(Enum):
    JOGADOR_NAO_EXISTENTE = 0 
    #======================================== retorna erro caso o jogador não esteja registrado e tente se inscrever

class FilaControlador:

    @classmethod
    def inscrever_na_fila(nome_jogador: str):
        jogador = None

        if(jogador != None):
            return FilaDB.instance().inscrever_jogador_na_fila(jogador)
        else:
            return TopicoControladorErro.JOGADOR_NAO_EXISTENTE
    
    @classmethod
    def desinscrever_da_fila(nome_jogador: str):    
        jogador = None
        
        if(jogador != None):
            return FilaDB.instance().desinscrever_jogador_na_fila(jogador)
        else:
            return TopicoControladorErro.JOGADOR_NAO_EXISTENTE