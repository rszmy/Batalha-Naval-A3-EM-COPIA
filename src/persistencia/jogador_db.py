from modelos.jogador import Jogador
import sqlite3

class JogadorDB():

    _lista_de_jogadores : list = []

    def __init__(self):
        self.popular_do_banco()

    def popular_do_banco(self):

        with sqlite3.connect("../batalha_naval.sqlite") as conn:
            cursor = conn.cursor()
            res = cursor.execute("SELECT id, nome, email, senha, pontuacao FROM Jogadores")

            for r in res:
                j : Jogador = Jogador(
                    nome=r[1],
                    email=r[2],
                    senha=r[3]
                )
                j._pontuacao_acumulada = r[4]
                self._lista_de_jogadores.append(j)

    def listar_todos_os_jogadores(self):
        return self._lista_de_jogadores
    
    def inserir_jogador_no_banco(self, jogador: Jogador):

        # sqlite_insert_with_param = """INSERT INTO Jogadores (id, nome, pontuacao, email, senha) VALUES (?, ?, ?, ?, ?);"""
        # data_tuple = (5, jogador._nome, jogador._pontuacao_acumulada, jogador._email, jogador._senha)

        # with sqlite3.connect("../batalha_naval.sqlite") as conn:
        #     cursor = conn.cursor()
        #     cursor.execute(sqlite_insert_with_param, data_tuple)
        
        self._lista_de_jogadores.append(jogador)
    
    def editar_jogador_no_banco(self):
        pass

    def remover_jogador_do_banco(self, nome: str):
        tam : int = len(self._lista_de_jogadores)
        self._lista_de_jogadores = [p for p in self._lista_de_jogadores if p._nome != nome]
        return (tam != len(self._lista_de_jogadores))