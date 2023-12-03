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
                    ["N"]
                ])
            case "Navio Pequeno":
                return Embarcacao(nome, [
                    ["N", "N"]
                ])
            case "Navio Médio":
                return Embarcacao(nome, [
                    ["N", "N", "N"] 
                ])
            case "Navio Grande":
                return Embarcacao(nome, [
                    ["N", "N", "N", "N"]
                ])
            case "Porta Aviões":
                return Embarcacao(nome, [
                    ["N", "N", "N"],
                    ["X", "N", "X"],
                    ["X", "N", "X"]
                ])
            case _:
                return None
