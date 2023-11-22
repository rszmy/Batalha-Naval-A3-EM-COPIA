from typing import Union
from fastapi import FastAPI
from controladores.main_controlador import MainControlador
from controladores.jogador_controlador import JogadorControlador

app = FastAPI()

@app.get("/")
async def menu():
    pass

# ========================== Jogador

@app.get("/jogadores/lista_de_jogadores")
async def listar_jogadores():
    return JogadorControlador.get_instance().lista_todos_os_jogadores()

@app.put("/jogadores/registro/{nome}/{idade}")
def adicionar_jogador(nome: str, idade: int):
    pass
    # return PessoasController.insere_pessoa(idade, nome)

@app.delete("/jogadores/remoção/{nome}")
def remover_jogador_por_nome(nome: str):
    pass
    # return PessoasController.remove_por_nome(nome)

@app.patch("/jogadores/edição/{nome}/{idade}")
def editar_jogador_por_nome(nome: str, idade: int):
    pass 
    # return PessoasController.editar_idade(nome, idade)

@app.get("/jogadores/top3")
async def ranking_top3():
    return JogadorControlador.get_instance().lista_ranking_top_3()

# ========================== Auth