from modelos.embarcacao import FabricaEmbarcacao

class EmbarcacoesControlador():

    def criar_embarcacoes():
        embarcacoes = [
            FabricaEmbarcacao.instance().create('Submarino'),
            FabricaEmbarcacao.instance().create('Submarino'),
            FabricaEmbarcacao.instance().create('Submarino'),
            FabricaEmbarcacao.instance().create('Navio Pequeno'),
            FabricaEmbarcacao.instance().create('Navio Pequeno'),
            FabricaEmbarcacao.instance().create('Navio Medio'),
            FabricaEmbarcacao.instance().create('Navio Grande'),
            FabricaEmbarcacao.instance().create('Porta Aviões')
        ]
        
        return embarcacoes
    