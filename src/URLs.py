from typing import Union
from fastapi import FastAPI
from controladores.jogador_controlador import JogadorControlador
from controladores.fila_controlador import FilaControlador

app = FastAPI()

# ========================== Topico

@app.post("/fila/entrar/{nome_jogador}")
def entrar_na_fila(nome_jogador: str):
    return FilaControlador.inscrever_na_fila(nome_jogador)

@app.post("/fila/sair/{nome_jogador}")
def sair_da_fila(nome_jogador: str):
    return FilaControlador.desinscrever_da_fila(nome_jogador)

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

# ========================== Auth