# Classe modelo das embarcações.
class Embarcacao():
    
    _nome : str
    _formato : list
    
    def __init__(self, nome, formato):
        self._nome = nome
        self._formato = formato

# Classe fabrica que constroí embarcações.
class FabricaEmbarcacao():
    
    _instance = None 
    
    # Implementação singleton.
    @classmethod
    def instance(cls):
        if(cls._instance == None):
            cls._instance = FabricaEmbarcacao()
        return cls._instance
    
    # Método fabrica.
    def fabrica(cls, nome:str):
        match nome:
            case "Submarino":
                return Embarcacao(nome, [
                    ["1"]
                ])
            case "Navio Pequeno":
                return Embarcacao(nome, [
                    ["2", "2"]
                ])
            case "Navio Médio":
                return Embarcacao(nome, [
                    ["3", "3", "3"] 
                ])
            # case "Navio Grande":
            #     return Embarcacao(nome, [
            #         ["N", "N", "N", "N"]
            #     ])
            case "Porta Aviões":
                return Embarcacao(nome, [
                    ["4", "4", "4"],
                    ["X", "4", "X"],
                    ["X", "4", "X"]
                ])
            case _:
                return None
