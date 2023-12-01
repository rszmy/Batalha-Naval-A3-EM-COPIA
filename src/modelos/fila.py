from modelos.jogador import Jogador

class Fila():
    _jogadores : list[Jogador]

    def __init__(self):
        self._jogadores = []
    
    def __str__(self):
        contagem = len(self._jogadores)
        return f"Quantidade de jogadores na fila: {contagem}"
    
    def inscrever_jogador(self, jogador: Jogador):
        self._jogadores.append(jogador)
    
    def desinscrever_jogador(self, jogador: Jogador):
        self._jogadores = [j for j in self._jogadores if j._nome != jogador._nome]

    def mostrar_jogadores_inscritos(self):
        return self._jogadores