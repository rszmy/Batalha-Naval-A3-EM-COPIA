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
@app.get("/tabuleiro")
async def mostrar_tabuleiro():
    tabuleiro : Tabuleiro = Tabuleiro()
    return TabuleiroControlador.representacao_tabuleiro(tabuleiro)

#========================== Embarcação

#Para teste   
@app.get('/embarcacao/{embarcacao}/{coord_x}/{coord_y}/{orientacao}/{parte}')
async def colocar_embarcacao(embarcacao : str, coord_x : int, coord_y : int, orientacao : str, parte : str):
    tabuleiro : Tabuleiro = Tabuleiro()
    return TabuleiroControlador.colocar_embarcacoes_no_tabuleiro(tabuleiro, embarcacao, coord_x, coord_y, orientacao, parte)

#Para teste   
@app.get('/embarcacao/teste')
async def teste_embarcacao():
    tabuleiro : Tabuleiro = Tabuleiro()
    TabuleiroControlador.definir_embarcacoes_para_colocar(tabuleiro)
    return TabuleiroControlador.listar_embarcacoes_para_colocar(tabuleiro, "a")

