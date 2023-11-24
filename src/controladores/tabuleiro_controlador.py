from modelos.tabuleiro import TabuleiroParte, Tabuleiro
from controladores.embarcacao_controlador import EmbarcacoesControlador

class TabuleiroControlador():
    _instance = None 
    _tabuleiro = Tabuleiro
    
    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = TabuleiroControlador()
        return cls._instance

    @classmethod
    def checar_espaco(cls, linha, coluna):
        return linha + coluna

    @classmethod
    def sobreposicao_embarcacao(cls, linha, coluna):
        
        try:
            if not cls.get_instance().checar_espaco(linha, coluna):
                return True  
    # Embarcação não cabe no tabuleiro
            for i in range(10):
                coord_x = chr(ord('A') + linha)
                coord_y = coluna + i
    # Coordenadas fora dos limites
                if coord_x not in cls.get_instance()._tabuleiro._parte_a._dict_alphanum or coord_y >= len(cls.get_instance()._tabuleiro._parte_a._matrix[0]):
                    return True 
    # Navio sobrepondo navio
                if cls.get_instance()._tabuleiro._parte_a.get_quadrante(coord_x, coord_y) != 'X':
                    return True 
    # Índicie fora dos limites do tabuleiro
        except IndexError:
            return True
        return False

    @classmethod
    def representacao_tabuleiro(cls):
        representacao = ""
        for linha in cls.get_instance()._tabuleiro._parte_a._matrix:
             representacao += " ".join(linha) + "\n"
        return representacao

    @classmethod
    def enviar_tabuleiro(cls, jogador):
        bytes_data = bytes(cls.get_instance().representacao_tabuleiro(), 'utf-8')
        jogador.sendall(bytes_data)

 