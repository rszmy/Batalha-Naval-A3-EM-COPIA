from modelos.embarcacao import Embarcacao

class TabuleiroParte():

    _lista_embarcacoes : list[Embarcacao]
    
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
        ['X','X','X','X','X','X','X','X','X','X'],
        ['X','X','X','X','X','X','X','X','X','X'],
        ['X','X','X','X','X','X','X','X','X','X'],
        ['X','X','X','X','X','X','X','X','X','X'],
        ['X','X','X','X','X','X','X','X','X','X'],
        ['X','X','X','X','X','X','X','X','X','X'],
        ['X','X','X','X','X','X','X','X','X','X'],
        ['X','X','X','X','X','X','X','X','X','X'],
        ['X','X','X','X','X','X','X','X','X','X'],
        ['X','X','X','X','X','X','X','X','X','X']
       
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

    def __init__(self):
        self._parte_a = TabuleiroParte()
        self._parte_b = TabuleiroParte()

    