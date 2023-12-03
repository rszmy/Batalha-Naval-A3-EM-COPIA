from modelos.partida import Partida

class PartidaDB():

    _instance = None
    _lista_de_partidas : list = []

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = PartidaDB()
        return cls._instance
    
    @classmethod
    def listar_partidas(cls):
        return cls.get_instance()._lista_de_partidas
    
    @classmethod
    def checar_jogador_em_partida(cls, nome_jogador: str):
        lista_de_partidas = cls.get_instance().listar_partidas()

        for partida in lista_de_partidas:
            if partida._jogador_a["nome"] == nome_jogador or partida._jogador_b["nome"] == nome_jogador:
                return {"message": f"Partida iniciada no id: {partida._id}"}
        return {"message": "Você não está em fila e nem em uma partida"}
    
    @classmethod
    def começar_nova_partida(cls, jogador_a: object, jogador_b: object):
        partida : Partida = Partida(jogador_a, jogador_b)
        cls.get_instance()._lista_de_partidas.append(partida)

    @classmethod
    def pegar_id_por_jogador(cls, jogador_a: object):
        lista_de_partidas = cls.get_instance().listar_partidas()
        id = 0

        for partida in lista_de_partidas:
            if partida._jogador_a == jogador_a:
                id = partida._id
        
        return id
    
    @classmethod
    def pegar_nome_jogador_por_id(cls, id: int, id_jogador: str):
        lista_de_partidas = cls.get_instance().listar_partidas()

        for partida in lista_de_partidas:
            if partida._id == id:
                if id_jogador == "a":
                    return partida._jogador_a["nome"]
                elif id_jogador == "b": 
                    return partida._jogador_b["nome"]
                else:
                    return False
    
    @classmethod
    def pegar_tabuleiro_por_id(cls, id: int):
        lista_de_partidas = cls.get_instance().listar_partidas()
        tabuleiro = None

        for partida in lista_de_partidas:
            if partida._id == id:
                tabuleiro = partida._tabuleiro
        
        return tabuleiro
    