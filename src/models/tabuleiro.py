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
        [ 'XXXXXXXXXX' ], # 0
        [ 'XXXXXXXXXX' ], # 1
        [ 'XXXXXXXXXX' ], # ...
        [ 'XXXXXXXXXX' ],
        [ 'XXXXXXXXXX' ],
        [ 'XXXXXXXXXX' ],
        [ 'XXXXXXXXXX' ],
        [ 'XXXXXXXXXX' ],
        [ 'XXXXXXXXXX' ],
        [ 'XXXXXXXXXX' ]
    ]

    def set_quadrante(self, x, y, val):
        cord_x = self._dict_alphanum[x]
        cord_y = y - 1
        self._matrix[cord_x][cord_y] = val

    def get_quadrante(self, x, y):
        cord_x = self._dict_alphanum[x]
        return self._matrix[cord_x][y-1]
    
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

            for i in range(10):
                cord_x = chr(ord('A') + linha)
                cord_y = coluna + i

                if cord_x not in self._parte_a._dict_alphanum or cord_y >= len(self._parte_a._matrix[0]):
                    return True  # Coordenadas fora dos limites

                if self._parte_a.get_quadrante(cord_x, cord_y) != 'X':
                    return True  # Navio sobrepondo navio

        except IndexError:
            return True  # Índicie fora dos limites do tabuleiro

        return False