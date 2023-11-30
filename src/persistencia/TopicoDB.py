from src.modelos.jogador import Jogador
from src.modelos.Topicos import Topico

class TopicoDB():
    _instance : "TopicoDB" = None
    _topico: Topico
    _jogadores_no_topico: list[Jogador]
    
    def __init__(self: "TopicoDB"):
        self._topicos =[]
    
    @classmethod
    def instance(cls):
        if(cls._instance is None):
            cls._instance = TopicoDB()
        return cls._instance