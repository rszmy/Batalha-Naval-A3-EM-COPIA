class Embarcacao():
    
    _nome : str
    _formato : []
    
    def __init__(self, nome, formato):
        self._nome = nome
        self._formato = formato


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
                [1, 1, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]
            ])
        elif(nome == 'Navio Medio'):
            return Embarcacao(nome, [
                [1, 1, 1, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]
            ])
        elif(nome == 'Navio Grande'):
            return Embarcacao(nome, [
                [1, 1, 1, 1],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]
            ])
        elif(nome == 'Porta Aviões'):
            return Embarcacao(nome, [
                [1, 1, 1, 0],
                [0, 1, 0, 0],
                [0, 1, 0, 0],
                [0, 0, 0, 0]
            ])
        else:
            return None

