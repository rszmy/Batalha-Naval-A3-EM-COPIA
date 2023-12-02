from modelos.embarcacao import Embarcacao

class TabuleiroParte():

    _coord_x = None
    _coord_y = None
    _area_tabuleiro : list
    _lista_embarcacoes_para_colocar : list[Embarcacao]
    _lista_embarcacoes_colocadas : list[Embarcacao]
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

    def __init__(self):
        self._coord_x = "ABCDEFGHIJ"
        self._coord_y = range(10)
        self._area_tabuleiro = [["X" for x in range(10)] for x in self._coord_y]

    def devolver_parte_tabuleiro(self):
        return self._area_tabuleiro
    
    def definir_embarcacoes_parte_tabuleiro(self, lista : list[Embarcacao]):
        self._lista_embarcacoes_para_colocar = lista

    def devolver_embarcacoes_parte_tabuleiro(self):
        return self._lista_embarcacoes_para_colocar
    
    def definir_embarcacao_viva(self, embarcacao : Embarcacao):
        self._lista_embarcacoes_colocadas.append(embarcacao)
        
        
class Tabuleiro():
    
    _parte_a : TabuleiroParte = None
    _parte_b : TabuleiroParte = None

    def __init__(self):
        self._parte_a = TabuleiroParte()
        self._parte_b = TabuleiroParte()

    def devolver_tabuleiro_por_parte(self, parte: str):
        if (parte == "a"):
            return self._parte_a.devolver_parte_tabuleiro()
        elif (parte == "b"):
            return self._parte_b.devolver_parte_tabuleiro()
        else:
            return False

    def definir_embarcacoes_tabuleiro (self, lista: list[Embarcacao]):
        self._parte_a.definir_embarcacoes_parte_tabuleiro(lista)
        self._parte_b.definir_embarcacoes_parte_tabuleiro(lista)

    def delvover_embarcacoes_por_parte(self, parte: str):
        if (parte == "a"):
            return self._parte_a.devolver_embarcacoes_parte_tabuleiro()
        elif (parte == "b"):
            return self._parte_b.devolver_embarcacoes_parte_tabuleiro()
        else:
            return False
        
    def definir_embarcacao_viva_na_parte(self, embarcacao: Embarcacao, parte  str):
        if (parte == "a"):
            return self._parte_a.definir_embarcacao_viva(embarcacao)
        elif (parte == "b"):
            return self._parte_b.definir_embarcacao_viva(embarcacao)
        else:
            return False