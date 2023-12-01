from persistencia.fila_db import FilaDB
from controladores.jogador_controlador import JogadorControlador
from enum import Enum 

class FilaControladorErro(Enum):
    JOGADOR_NAO_EXISTENTE = 0 
    #======================================== retorna erro caso o jogador não esteja registrado e tente se inscrever

class FilaControlador:

    @classmethod
    def inscrever_na_fila(cls, nome_jogador: str):
        lista_de_jogadores = JogadorControlador.listar_todos_os_jogadores()
        jogador = None
        
        for j in lista_de_jogadores:
            print (j)
            if j['nome'] == nome_jogador:
                jogador = j

        if(jogador != None):
            return FilaDB.instance().inscrever_jogador_na_fila(jogador)
        else:
            return FilaControladorErro.JOGADOR_NAO_EXISTENTE
    
    @classmethod
    def desinscrever_da_fila(cls, nome_jogador: str):    
        lista_de_jogadores = JogadorControlador.listar_todos_os_jogadores()
        jogador = None
        
        for j in lista_de_jogadores:
            if j['nome'] == nome_jogador:
                jogador = j
        
        if(jogador != None):
            return FilaDB.instance().desinscrever_jogador_na_fila(jogador)
        else:
            return FilaControladorErro.JOGADOR_NAO_EXISTENTE
        
    @classmethod
    def mostrar_jogadores_na_fila(cls):
        return FilaDB.instance().mostrar_jogadores_na_fila()