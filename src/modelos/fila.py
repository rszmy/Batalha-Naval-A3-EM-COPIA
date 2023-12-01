from modelos.jogador import Jogador

class Fila():
    _jogadores : list[Jogador]

    def __init__(self):
        self._jogadores = []
    
    def __str__(self):
        contagem = len(self._jogadores)
        return f"Quantidade de jogadores na fila: {contagem}"
    
    def inscrever_jogador(self, jogador: Jogador):
        pass
    
    def desinscrever_jogador(self, jogador: Jogador):
        pass
    