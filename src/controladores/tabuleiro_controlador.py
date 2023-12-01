from modelos.tabuleiro import Tabuleiro
from controladores.embarcacao_controlador import EmbarcacoesControlador

class TabuleiroControlador():

    _instance = None 
    _tabuleiro = Tabuleiro()
    
    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = TabuleiroControlador()
        return cls._instance
    
    #Criando embarcacoes pro tabuleiro
    @classmethod
    def definir_embarcacoes(cls):
        lista : list = EmbarcacoesControlador.criar_embarcacoes()
        cls.get_instance()._tabuleiro.definir_embarcacoes_tabuleiro(lista)
    
    @classmethod
    def teste_embarcacao(cls):
        cls.get_instance().definir_embarcacoes()
        return cls.get_instance()._tabuleiro._parte_a._lista_embarcacoes
    
    #Colocando embarcacoes no tabuleiro
    # @classmethod
    # def tabuleiro_embarcacoes(cls, embarcacao, coord_x, coord_y, orientacao):
        
    #     if not(0 <= coord_x < 10 and 0 <= coord_y < 10):
    #         raise ValueError('Coordenadas invalidas')
        
    #     for i in range(cls._tabuleiro._parte_a._lista_embarcacoes[]):
    #         if orientacao == 'horizontal':
    #             if coord_y + i >= 10 or cls._tabuleiro._parte_a[coord_x][coord_y + i] != 'X':
    #                 raise ValueError('Outra embarcação aqui irmão')
    #             cls._tabuleiro._parte_a[coord_x][coord_y + i] = 
    #         elif orientacao == 'vertical':
    #             if coord_x + i >= 10 or cls._tabuleiro._parte_a[coord_x + i][coord_y] != 'X':
    #                 raise ValueError('Outra embarcação aqui irmão')
    #             cls._tabuleiro._parte_a[coord_x + i][coord_y] = 
    #         else:
    #             raise ValueError('Orientação errada')
        
        
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
    def representacao_tabuleiro(self):
        representacao = []
        for linha in self._tabuleiro._parte_a._matrix:
           representacao.append(''.join(linha)) 
        return representacao
       
    @classmethod
    def enviar_tabuleiro(cls, jogador):
        bytes_data = bytes(cls.get_instance().representacao_tabuleiro(), 'utf-8')
        jogador.sendall(bytes_data)

 