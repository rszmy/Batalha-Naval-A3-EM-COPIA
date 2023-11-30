from persistencia.jogador_db import JogadorDB
from modelos.jogador import Jogador
import hashlib

class JogadorControlador:

    @classmethod
    def pegar_lista_de_jogadores (cls):
        return JogadorDB.get_instance().listar_todos_os_jogadores()

    @classmethod
    def filtrar_lista_de_jogadores(cls):
        jogadores = cls.pegar_lista_de_jogadores
        
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
        return cls.filtrar_lista_de_jogadores()

    @classmethod
    def listar_ranking(cls):
        lista_de_jogadores = cls.filtrar_lista_de_jogadores()

        def criterio(lista_de_jogadores):
            return - lista_de_jogadores["pontuacao"]

        ranking_ordenado = sorted(lista_de_jogadores, key=criterio)

        return ranking_ordenado
    
    @classmethod
    def listar_ranking_top_3(cls):
        ranking_ordenado = cls.listar_ranking()
        return ranking_ordenado[:3]   

    @classmethod
    def adicionar_jogador(cls, nome: str, email: str, senha: str):
        senha = hashlib.md5(senha.encode('utf-8'))
        senha = senha.hexdigest()
        j : Jogador = Jogador(nome, email, senha)
        JogadorDB.get_instance().inserir_jogador_no_banco(j)

    @classmethod
    def editar_jogador_por_nome(cls, nome: str, email: str):
        JogadorDB.get_instance().editar_jogador_no_banco(nome, email)

    @classmethod
    def remover_jogador_por_nome(cls, nome: str):
        JogadorDB.get_instance().remover_jogador_do_banco(nome)