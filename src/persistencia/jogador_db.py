from modelos.jogador import Jogador
import sqlite3

class JogadorDB():

    _lista_de_jogadores : list = []

    def popula_do_banco(self):
        # lê do banco de dados
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

    def __init__(self):
        self.popula_do_banco()
         
    def lista_todos_os_jogadores(self):
        return self._lista_de_jogadores