#classe embarcações
class Embarcacao():
    
    _nome : str
    _formato = []
    
    def __init__(self, nome, formato):
        self._nome = nome
        self._formato = formato

#constroi as embarcações
class FabricaEmbarcacao():
    
    @classmethod
    def instance(cls):
        if(cls._instace == None):
            cls._instance = FabricaEmbarcacao()
        return cls._instance
    
    def fabrica(nome:str):
        if(nome == 'Submarino'):
            return Embarcacao(nome, [
                [1, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]
            ])
        elif(nome == 'Navio Pequeno'):
            return Embarcacao(nome, [
                [2, 2, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]
            ])
        elif(nome == 'Navio Medio'):
            return Embarcacao(nome, [
                [3, 3, 3, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]
            ])
        elif(nome == 'Navio Grande'):
            return Embarcacao(nome, [
                [4, 4, 4, 4],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]
            ])
        elif(nome == 'Porta Aviões'):
            return Embarcacao(nome, [
                [5, 5, 5, 0],
                [0, 5, 0, 0],
                [0, 5, 0, 0],
                [0, 0, 0, 0]
            ])
        else:
            return None

