from modelos.embarcacao import FabricaEmbarcacao

class EmbarcacoesControlador():

    _instance = None
    
    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = EmbarcacoesControlador()
        return cls._instance
    
    @classmethod
    def criar_embarcacoes(cls):
        embarcacoes = [
            FabricaEmbarcacao.instance().fabrica('Submarino'),
            FabricaEmbarcacao.instance().fabrica('Submarino'),
            FabricaEmbarcacao.instance().fabrica('Submarino'),
            FabricaEmbarcacao.instance().fabrica('Navio Pequeno'),
            FabricaEmbarcacao.instance().fabrica('Navio Pequeno'),
            FabricaEmbarcacao.instance().fabrica('Navio Medio'),
            FabricaEmbarcacao.instance().fabrica('Navio Grande'),
            FabricaEmbarcacao.instance().fabrica('Porta Aviões')
        ]
        return embarcacoes
