from controladores.jogador_controlador import JogadorControlador
from datetime import datetime, timedelta
import hashlib

class AutenticacaoControlador:

    _instance = None

    def __init__(self):
        pass

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = AutenticacaoControlador()
        return cls._instance

    # def get_hash(self, nome:str):
    #     for u in JogadorControlador.get_instance()._db.listar_todos_os_jogadores():
    #         if u._nome == nome:
    #             return u._senha
    #     return "-1"

    # def destruir_sessao(cls, usuario: str):
    #     cls.instance()._sessions = [x for x in cls.instance()._sessions if x._nome != usuario]

    # def registrar_sessao(self, usuario: str):

    #     AuthDB.destroy_session(usuario)

    #     expiracao = datetime.now()
    #     expiracao = expiracao + timedelta(minutes=30)

    #     chave = hashlib.md5((usuario + str(expiracao.timestamp())).encode('utf-8'))
    #     session : AuthDBSession = AuthDBSession(usuario, chave.hexdigest(), expiracao)
    #     cls.instance()._sessions.append(session)

    #     return session._chave

    # def checar_chave(cls, chave: str):
    #     for session in cls.instance()._sessions:
    #         if(session._chave == chave and session._expiracao > datetime.now()):
    #             return True
    #     return False
