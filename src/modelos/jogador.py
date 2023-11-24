class Jogador():

    _nome : str
    _email : str
    _senha : str
    _pontuacao_acumulada: int

    def __init__(self, nome: str, email: str, senha: str):
        self._nome = nome
        self._email = email
        self._senha = senha
        self._pontuacao_acumulada = 0 