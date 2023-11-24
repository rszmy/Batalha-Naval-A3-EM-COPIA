# from modelos.embarcacao import Embarcacao, FabricaEmbarcacao

class TabuleiroParte():

    _dict_alphanum = {
        "A" : 0,
        "B" : 1,
        "C" : 2,
        "D" : 3,
        "E" : 4,
        "F" : 5,
        "G" : 6,
        "H" : 7,
        "I" : 8,
        "J" : 9
    }

    _matrix = [
        [ 'XXXXXXXXXX' ],
        [ 'XXXXXXXXXX' ],
        [ 'XXXXXXXXXX' ],
        [ 'XXXXXXXXXX' ],
        [ 'XXXXXXXXXX' ],
        [ 'XXXXXXXXXX' ],
        [ 'XXXXXXXXXX' ],
        [ 'XXXXXXXXXX' ],
        [ 'XXXXXXXXXX' ],
        [ 'XXXXXXXXXX' ]
    ]

    def set_quadrante(self, x, y, val):
        coord_x = self._dict_alphanum[x]
        coord_y = y - 1
        self._matrix[coord_x][coord_y] = val

    def get_quadrante(self, x, y):
        coord_x = self._dict_alphanum[x]
        return self._matrix[coord_x][y-1]
    
class Tabuleiro():
    
    _parte_a : TabuleiroParte = None
    _parte_b : TabuleiroParte = None

    def __init__(self, area=10):
        self._parte_a = TabuleiroParte(area)
        self._parte_b = TabuleiroParte(area)

    def representacao_tabuleiro(self):
        representacao = ""
        for linha in self._parte_a._matrix:
            representacao += " ".join(linha) + "\n"
        return representacao
    
    def enviar_tabuleiro(self, jogador):
        bytes_data = bytes(self.representacao_tabuleiro(), 'utf-8')
        jogador.sendall(bytes_data)
    
    def checar_espaco(linha, coluna):
        return linha + coluna 
    
    def sobreposicao_embarcacao(self, linha, coluna):
        try:
            if not self.checar_espaco(linha, coluna):
                return True  # Embarcação não cabe no tabuleiro
    # Embarcação não cabe no tabuleiro
            for i in range(10):
                coord_x = chr(ord('A') + linha)
                coord_y = coluna + i
    # Coordenadas fora dos limites
                if coord_x not in self._parte_a._dict_alphanum or coord_y >= len(self._parte_a._matrix[0]):
                    return True 
    # Navio sobrepondo navio
                if self._parte_a.get_quadrante(coord_x, coord_y) != 'X':
                    return True 
    # Índicie fora dos limites do tabuleiro
        except IndexError:
            return True
        return False

    def numero_embarcacao():

        embarcacoes = [
            FabricaEmbarcacao.instance().create('Submarino')
            FabricaEmbarcacao.instance().create('Submarino')
            FabricaEmbarcacao.instance().create('Submarino')
            FabricaEmbarcacao.instance().create('Navio Pequeno')
            FabricaEmbarcacao.instance().create('Navio Pequeno')
            FabricaEmbarcacao.instance().create('Navio Medio')
            FabricaEmbarcacao.instance().create('Navio Grande')
            FabricaEmbarcacao.instance().create('Porta Aviões')
    ]: