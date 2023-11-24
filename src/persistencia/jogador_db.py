from modelos.jogador import Jogador
from persistencia.config_db import ConfigDB

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
        sqlite_insert = """INSERT INTO Jogadores (nome, pontuacao, email, senha) VALUES (?, ?, ?, ?);"""
        valores = (jogador._nome, jogador._pontuacao_acumulada, jogador._email, jogador._senha)
        ConfigDB.executa_sql(sqlite_insert, valores)
        
        self._lista_de_jogadores.append(jogador)
    
    def editar_jogador_no_banco(self, nome: str, email: str):
        lista_filtrada : list[Jogador] = [x for x in self._lista_de_jogadores if x._nome == nome]
        if(len(lista_filtrada) == 0):
            return False
        else:
            jogador_alvo : Jogador = lista_filtrada[0]
            jogador_alvo._email = email

            sqlite_update = """UPDATE Jogadores SET email = ? where nome = ?"""
            valores = (jogador_alvo._email, jogador_alvo._nome)
            ConfigDB.executa_sql(sqlite_update, valores)

            return True

    def remover_jogador_do_banco(self, nome: str):
        self._lista_de_jogadores = [p for p in self._lista_de_jogadores if p._nome != nome]
        valor = (nome,)
        sqlite_delete = """DELETE FROM Jogadores where nome = ?"""
        ConfigDB.executa_sql(sqlite_delete, valor)