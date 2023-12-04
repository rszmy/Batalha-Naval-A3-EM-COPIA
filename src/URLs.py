#from typing import Union
from fastapi import FastAPI
from controladores.jogador_controlador import JogadorControlador
from controladores.fila_controlador import FilaControlador
from controladores.partida_controlador import PartidaControlador

app = FastAPI()

# ========================== 

@app.get("/")
async def menu():
    return {"message": "Hello World"}

# ========================== Jogador

@app.get("/jogadores/lista_de_jogadores")
async def listar_jogadores():
    return JogadorControlador.listar_todos_os_jogadores()

@app.get("/jogadores/ranking")
async def listar_jogadores():
    return JogadorControlador.listar_ranking()

@app.get("/jogadores/ranking/top3")
async def ranking_top3():
    return JogadorControlador.listar_ranking_top_3()

@app.put("/jogadores/registro/{nome}/{email}/{senha}")
def adicionar_jogador(nome: str, email: str, senha: str):
    return JogadorControlador.adicionar_jogador(nome, email, senha)

@app.patch("/jogadores/edição/{nome}/{email}")
def editar_jogador_por_nome(nome: str, email: str):
    return JogadorControlador.editar_jogador_por_nome(nome, email)

@app.delete("/jogadores/remoção/{nome}")
def remover_jogador_por_nome(nome: str):
    return JogadorControlador.remover_jogador_por_nome(nome)

# ========================== Fila

@app.post("/fila/entrar/{nome_jogador}")
def entrar_na_fila(nome_jogador: str):
    return FilaControlador.inscrever_na_fila(nome_jogador)

@app.post("/fila/sair/{nome_jogador}")
def sair_da_fila(nome_jogador: str):
    return FilaControlador.desinscrever_da_fila(nome_jogador)

@app.get("/fila/jogadores_na_fila")
def mostrar_jogadores_na_fila():
    return FilaControlador.mostrar_jogadores_na_fila()

@app.get("/fila/checagem/{nome_jogador}")
def checar_começo_de_partida(nome_jogador: str):
    return FilaControlador.checar_confirmacao_da_partida(nome_jogador)

# ========================== Auth

# ========================== Partida

@app.get("/partida/tabuleiro/{id}/{nome_jogador}")
def pegar_representacao_tabuleiro_partida(id: int, nome_jogador: str):
    return PartidaControlador.pegar_representacao_tabuleiro_partida(id, nome_jogador)

@app.get("/partida/embarcacoes/peças/{id}/{nome_jogador}")
def checar_embarcacoes_disponiveis(id: int, nome_jogador: str):
    return PartidaControlador.checar_embarcacoes_disponiveis(id, nome_jogador)

@app.patch("/partida/tabuleiro/peças/{id}/{nome_jogador}/{embarcacao}/{coord_x}/{coord_y}/{orientacao}")
def colocar_embarcacao_tabuleiro(id: int, nome_jogador: str, embarcacao: str, coord_x: str, coord_y: int, orientacao: str):
    return PartidaControlador.colocar_embarcacao_tabuleiro(id, nome_jogador, embarcacao, coord_x, coord_y, orientacao)

@app.get("/partida/tabuleiro/disparo/{id}/{nome_jogador}/{coord_x}/{coord_y}/")
def realizar_disparo(id: int, nome_jogador: str, coord_x: str, coord_y: int):
    return PartidaControlador.realizar_disparo(id, nome_jogador, coord_x, coord_y)
    