from persistencia.autenticacao_db import AutenticacaoDB
from controladores.jogador_controlador import JogadorControlador
from enum import Enum
import hashlib

class AutenticacaoErros(Enum):
    USUARIO_OU_SENHA_INCORRETOS = 1
    AUTENTICACAO_OK = 2

class AutenticacaoControlador:
    
    @classmethod
    def autenticar(cls, nome: str, senha: str):

        lista_de_jogadores = JogadorControlador.pegar_lista_de_jogadores()

        hash_db = AutenticacaoDB.get_instance().pegar_hash_por_nome(nome, lista_de_jogadores)

        senha = hashlib.md5(senha.encode('utf-8'))
        senha = senha.hexdigest()
        
        if (senha == hash_db):
            return AutenticacaoDB.get_instance().registrar_sessao(nome)
        return AutenticacaoErros.USUARIO_OU_SENHA_INCORRETOS
    
    @classmethod
    def checar_chave(chave: str):
        return AutenticacaoDB.get_instance().checar_chave()
