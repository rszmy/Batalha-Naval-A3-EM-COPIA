from persistencia.jogador_db import JogadorDB

class JogadorControlador:

    _instance = None
    _db = None

    def __init__(self):
        self._db = JogadorDB()

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = JogadorControlador()
        return cls._instance
    
    def filtrar_lista_de_jogadores(self):
        jogadores = self._db.listar_todos_os_jogadores()
        
        jogadores_dto = []
        for jogador in jogadores:

            jogadores_dto.append({
                "nome": jogador._nome,
                "pontuacao": int(jogador._pontuacao_acumulada),
                "email": jogador._email
            })

        lista_filtrada : [] = jogadores_dto

        return lista_filtrada
    
    def listar_todos_os_jogadores(self):
        return self.filtrar_lista_de_jogadores()
    
    def listar_ranking(self):
        lista_de_jogadores = self.filtrar_lista_de_jogadores()

        def criterio(lista_de_jogadores):
            return - lista_de_jogadores["pontuacao"]

        ranking_ordenado = sorted(lista_de_jogadores, key=criterio)

        return ranking_ordenado
        
    def listar_ranking_top_3(self):
        ranking_ordenado = self.listar_ranking()
        return ranking_ordenado[:3]   
    
    def adicionar_jogador(self):
        pass
    
    def editar_jogador_por_nome(self):
        pass

    def remover_jogador_por_nome(self):
        pass