from persistencia.jogador_db import JogadorDB
from modelos.jogador import Jogador

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

    @classmethod
    def filtrar_lista_de_jogadores(cls):
        jogadores = cls.get_instance()._db.listar_todos_os_jogadores()
        
        jogadores_dto = []
        for jogador in jogadores:

            jogadores_dto.append({
                "nome": jogador._nome,
                "pontuacao": int(jogador._pontuacao_acumulada),
                "email": jogador._email
            })

        lista_filtrada : [] = jogadores_dto

        return lista_filtrada

    @classmethod
    def listar_todos_os_jogadores(cls):
        return cls.get_instance().filtrar_lista_de_jogadores()

    @classmethod
    def listar_ranking(cls):
        lista_de_jogadores = cls.get_instance().filtrar_lista_de_jogadores()

        def criterio(lista_de_jogadores):
            return - lista_de_jogadores["pontuacao"]

        ranking_ordenado = sorted(lista_de_jogadores, key=criterio)

        return ranking_ordenado
    
    @classmethod
    def listar_ranking_top_3(cls):
        ranking_ordenado = cls.get_instance().listar_ranking()
        return ranking_ordenado[:3]   
    
    
    @classmethod
    def adicionar_jogador(cls, nome : str, email : str, senha : str):
        j : Jogador = Jogador(nome, email, senha)
        cls.get_instance()._db.inserir_jogador_no_banco(j)

    @classmethod
    def editar_jogador_por_nome(cls):
        pass

    @classmethod
    def remover_jogador_por_nome(cls, nome: str):
        cls.get_instance()._db.remover_jogador_do_banco(nome)