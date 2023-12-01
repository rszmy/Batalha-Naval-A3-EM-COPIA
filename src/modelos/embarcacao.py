#classe embarcações
class Embarcacao():
    
    _nome : str
    _formato : list
    
    def __init__(self, nome, formato):
        self._nome = nome
        self._formato = formato

#constroi as embarcações
class FabricaEmbarcacao():
    
    _instance = None 
    
    @classmethod
    def instance(cls):
        if(cls._instance == None):
            cls._instance = FabricaEmbarcacao()
        return cls._instance
    
    def fabrica(cls, nome:str):
        match nome:
            case "Submarino":
                return Embarcacao(nome, [
                    [1]
                ])
            case "Navio Pequeno":
                return Embarcacao(nome, [
                    [2, 2]
                ])
            case "Navio Médio":
                return Embarcacao(nome, [
                    [3, 3, 3] 
                ])
            case "Navio Grande":
                return Embarcacao(nome, [
                    [4, 4, 4, 4]
                ])
            case "Porta Aviões":
                return Embarcacao(nome, [
                    [5, 5, 5],
                    [0, 5, 0],
                    [0, 5, 0]
                ])
            case _:
                return None
