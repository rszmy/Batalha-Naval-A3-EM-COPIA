from typing import Union
from fastapi import FastAPI
from controladores.jogador_controlador import JogadorControlador
from controladores.topicos_crontrolador import TopicoControlador

app = FastAPI()

# ========================== Topico
@app.get("/topicos/get")
def get_all_topics():
    return TopicoControlador.listar_topicos()

@app.get("/topicos/put/{nome}")
def put_new_topic(nome: str):
    return TopicoControlador.criar_novo_topico(nome)

@app.get("/topicos/delete/{nome}")
def remove_topic(nome: str):
    return TopicoControlador.remover_topico(nome)

@app.post("/topicos/subscribe/{nome_topico}/{nome_jogador}")
def subscribe(nome_topico: str, nome_jogador: str):
    return TopicoControlador.subscribe(nome_topico, nome_jogador)

@app.post("/topicos/unsubscribe/{nome_topico}/{nome_jogador}")
def unsubscribe(nome_topico: str, nome_jogador: str):
    return TopicoControlador.unsubscribe(nome_topico, nome_jogador)

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