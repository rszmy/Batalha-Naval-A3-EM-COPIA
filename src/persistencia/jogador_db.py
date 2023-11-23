from modelos.jogador import Jogador
from persistencia.config_db import ConfigDB
import sqlite3

class JogadorDB():

    _lista_de_jogadores : list = []

    def __init__(self):
        self.popular_do_banco()

    def popular_do_banco(self):

        res = ConfigDB.executa_sql("SELECT id, nome, email, senha, pontuacao FROM Jogadores", False)

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
        sqlite_insert_parametro = """INSERT INTO Jogadores (nome, pontuacao, email, senha) VALUES (?, ?, ?, ?);"""
        valores = (jogador._nome, jogador._pontuacao_acumulada, jogador._email, jogador._senha)
        ConfigDB.executa_sql(sqlite_insert_parametro, valores)
        
        self._lista_de_jogadores.append(jogador)
    
    def editar_jogador_no_banco(self, nome: str, email: str):
        lista_filtrada : list[Jogador] = [x for x in self._lista_de_jogadores if x._nome == nome]
        if(len(lista_filtrada) == 0):
            return False
        else:
            jogador_alvo : Jogador = lista_filtrada[0]
            jogador_alvo._email = email
            return True

    def remover_jogador_do_banco(self, nome: str):
        tam : int = len(self._lista_de_jogadores)
        self._lista_de_jogadores = [p for p in self._lista_de_jogadores if p._nome != nome]
        return (tam != len(self._lista_de_jogadores))