from modelos.jogador import Jogador

class Topico():
    _nome : str
    _jogadores : list[Jogador]

    def __init__(self, nome: str):
        self._nome = nome
        self._jogadores = []
    
    def __str__(self):
        contagem = len(self._jogadores)
        return f"{self.nome}: {contagem}"
    
    def subscribe(self, jogador: Jogador):
        pass
    
    def unsubscribe(self, jogador: Jogador):
        pass
    