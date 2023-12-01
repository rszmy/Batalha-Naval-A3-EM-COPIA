from modelos.embarcacao import FabricaEmbarcacao

class EmbarcacoesControlador():

    def criar_embarcacoes():
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
    