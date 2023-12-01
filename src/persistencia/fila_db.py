from modelos.fila import Fila

class FilaDB():

    _instance : "FilaDB" = None
    _fila: Fila
    
    def __init__(self: "FilaDB"):
        self._fila = []
    
    @classmethod
    def instance(cls):
        if(cls._instance is None):
            cls._instance = FilaDB()
        return cls._instance
    
    @classmethod
    def inscrever_jogador_na_fila(cls, jogador):
        cls.instance()._fila.inscrever_jogador

    @classmethod
    def desinscrever_jogador_na_fila(cls, jogador):
        cls.instance()._fila.desinscrever_jogador