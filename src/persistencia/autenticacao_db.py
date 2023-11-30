from modelos.autenticacao_sessao import AutenticacaoSessao
from datetime import datetime, timedelta
import hashlib

class AutenticacaoDB():

    _get_instance = None
    _sessoes : list[AutenticacaoSessao]

    def __init__(self: "AutenticacaoDB"):
        self._sessoes = []

    @classmethod
    def get_instance(cls):
        if cls._get_instance is None:
            cls._get_instance = AutenticacaoDB()
        return cls._get_instance
    
    @classmethod
    def pegar_hash_por_nome(cls, nome: str, lista: list):
        for jogador in lista:
            if jogador._nome == nome:
                return jogador._senha
        return "-1 deu ruim"
    
    @classmethod
    def destruir_sessao(cls, nome: str):
        cls.get_instance()._sessoes = [x for x in cls.get_instance()._sessoes if x._nome != nome]

    @classmethod
    def registrar_sessao(cls, nome: str):
        cls.get_instance().destruir_sessao(nome)

        expiracao = datetime.now()
        expiracao = expiracao + timedelta(minutes=30)

        chave = hashlib.md5((nome + str(expiracao.timestamp())).encode('utf-8'))
        
        session : AutenticacaoSessao = AutenticacaoSessao(nome, chave.hexdigest(), expiracao)
        cls.get_instance()._sessoes.append(session)

        return session._chave
    
    @classmethod
    def checar_chave(cls, chave: str):
        for session in cls.get_instance()._sessoes:
            if(session._chave == chave and session._expiracao > datetime.now()):
                return True
        return False