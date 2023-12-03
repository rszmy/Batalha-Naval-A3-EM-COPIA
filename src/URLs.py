from typing import Union
from fastapi import FastAPI
from controladores.jogador_controlador import JogadorControlador
from controladores.tabuleiro_controlador import TabuleiroControlador
from modelos.tabuleiro import Tabuleiro #Para teste

app = FastAPI()

@app.get("/")
async def menu():
    pass

# ========================== Jogador

@app.get("/jogadores/lista_de_jogadores")
async def listar_jogadores():
    return JogadorControlador.get_instance().listar_todos_os_jogadores()

@app.get("/jogadores/ranking")
async def listar_jogadores():
    return JogadorControlador.get_instance().listar_ranking()

@app.get("/jogadores/ranking/top3")
async def ranking_top3():
    return JogadorControlador.get_instance().listar_ranking_top_3()

@app.put("/jogadores/registro/{nome}/{email}/{senha}")
def adicionar_jogador(nome: str, email: str, senha: str):
    return JogadorControlador.get_instance().adicionar_jogador(nome, email, senha)

@app.patch("/jogadores/edição/{nome}/{email}")
def editar_jogador_por_nome(nome: str, email: str):
    return JogadorControlador.get_instance().editar_jogador_por_nome(nome, email)

@app.delete("/jogadores/remoção/{nome}")
def remover_jogador_por_nome(nome: str):
    return JogadorControlador.get_instance().remover_jogador_por_nome(nome)

# ========================== Auth

# ========================== Tabuleiro

#Para teste
tabuleiro : Tabuleiro = Tabuleiro()
TabuleiroControlador.definir_embarcacoes_para_colocar(tabuleiro)

#Para teste
@app.get("/tabuleiro/{parte}")
async def mostrar_tabuleiro(parte: str):
    return TabuleiroControlador.pegar_tabuleiro_por_parte(tabuleiro, parte)

#Para teste
@app.get("/tabuleiro2/{parte}")
async def mostrar_tabuleiro_camuflado(parte: str):
    return TabuleiroControlador.pegar_tabuleiro_camuflado_por_parte(tabuleiro, parte)
# ========================== Embarcação

#Para teste   
@app.get('/embarcacao/{embarcacao}/{coord_x}/{coord_y}/{orientacao}/{parte}')
async def colocar_embarcacao(embarcacao : str, coord_x : str, coord_y : int, orientacao : str, parte : str):
    return TabuleiroControlador.colocar_embarcacoes_no_tabuleiro(tabuleiro, parte, embarcacao, coord_x, coord_y, orientacao)

#Para teste   
@app.get('/embarcacao/teste')
async def teste_embarcacao():
    return TabuleiroControlador.listar_embarcacoes_para_colocar(tabuleiro, "a")

#Para teste disparo
@app.get('/disparo/{parte}/{coord_x}/{coord_y}')
async def teste_disparo(parte: str, coord_x: str, coord_y: int):
    return TabuleiroControlador.disparo(tabuleiro, parte, coord_x, coord_y)