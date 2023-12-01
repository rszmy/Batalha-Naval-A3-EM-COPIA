from modelos.tabuleiro import Tabuleiro
from controladores.embarcacao_controlador import EmbarcacoesControlador

class TabuleiroControlador():
    
    #Criando embarcacoes pro tabuleiro
    @classmethod
    def definir_embarcacoes(cls, tabuleiro: Tabuleiro):
        lista : list = EmbarcacoesControlador.criar_embarcacoes()
        tabuleiro.definir_embarcacoes_tabuleiro(lista)
    
    @classmethod
    def pegar_embarcacoes(cls, tabuleiro: Tabuleiro):
        return tabuleiro.delvover_embarcacoes_por_parte("a")
    
    # Colocando embarcacoes no tabuleiro
    # @classmethod
    # def colocar_embarcacoes_no_tabuleiro(cls, tabuleiro: Tabuleiro, parte: str, embarcacao: str, coord_x: int, coord_y: int, orientacao: str):

    #     if not(0 <= coord_x < 10 and 0 <= coord_y < 10):
    #         raise ValueError('Coordenadas invalidas')
        

        
    #     for i in range(cls._tabuleiro._parte_a._lista_embarcacoes[embarcacao]):
    #         if orientacao == 'horizontal':
    #             if coord_y + i >= 10 or cls._tabuleiro._parte_a[coord_x][coord_y + i] != 'X':
    #                 raise ValueError('Outra embarcação aqui irmão')
    #             cls._tabuleiro._parte_a[coord_x][coord_y + i] = embarcacao
    #         elif orientacao == 'vertical':
    #             if coord_x + i >= 10 or cls._tabuleiro._parte_a[coord_x + i][coord_y] != 'X':
    #                 raise ValueError('Outra embarcação aqui irmão')
    #             cls._tabuleiro._parte_a[coord_x + i][coord_y] = embarcacao
    #         else:
    #             raise ValueError('Orientação errada')
        
        
    # @classmethod
    # def checar_espaco(cls, linha, coluna):
    #     return linha + coluna

    # @classmethod
    # def sobreposicao_embarcacao(cls, linha, coluna):
    #     try:
    #         if not cls.get_instance().checar_espaco(linha, coluna):
    #             return True  
    # # Embarcação não cabe no tabuleiro
    #         for i in range(10):
    #             coord_x = chr(ord('A') + linha)
    #             coord_y = coluna + i
    # # Coordenadas fora dos limites
    #             if coord_x not in cls.get_instance()._tabuleiro._parte_a._dict_alphanum or coord_y >= len(cls.get_instance()._tabuleiro._parte_a._matrix[0]):
    #                 return True 
    # # Navio sobrepondo navio
    #             if cls.get_instance()._tabuleiro._parte_a.get_quadrante(coord_x, coord_y) != 'X':
    #                 return True 
    # # Índicie fora dos limites do tabuleiro
    #     except IndexError:
    #         return True
    #     return False

    @classmethod
    def representacao_tabuleiro(self, tabuleiro: Tabuleiro):
        tabuleiro_parte = tabuleiro.devolver_tabuleiro_por_parte("a")
        representacao = []
        for linha in tabuleiro_parte:
           representacao.append(''.join(linha)) 
        return representacao