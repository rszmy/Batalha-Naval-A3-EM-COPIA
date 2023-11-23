class TabuleiroParte():

    _dict_alphanum = {
        "A" : 0,
        "B" : 1,
        "C" : 2,
        "D" : 3,
        "E" : 4,
        "F" : 5,
        "G" : 6,
        "H" : 7,
        "I" : 8,
        "J" : 9
    }

    # 10x10
    # [ 'z', 'z', 'z'] === "zzz"
    _matrix = [
        [ 'XXXXXXXXXX' ], # 0
        [ 'XXXXXXXXXX' ], # 1
        [ 'XXXXXXXXXX' ], # ...
        [ 'XXXXXXXXXX' ],
        [ 'XXXXXXXXXX' ],
        [ 'XXXXXXXXXX' ],
        [ 'XXXXXXXXXX' ],
        [ 'XXXXXXXXXX' ],
        [ 'XXXXXXXXXX' ],
        [ 'XXXXXXXXXX' ]
    ]

    _matrix2 = ["XXXXXXXXXX" for x in range(10)]

    def set_quadrante(self, x, y, val):
        cord_x = self._dict_alphanum[x]
        cord_y = y - 1
        self._matrix2[cord_x][cord_y] = val

    # Loop para cada quadrado do tabuleiro (se necessário)

        for cord_x in range(linha+1):
            for cord_y in range(coluna+1):

    """
    get_quadrante
    @param x: coordenada X (valores de A à J)
    @param y: coordenada Y (valores entre 1 e 10)
    @return : caracteres do quadrante
        X: água
        O: não descoberto ainda
        N: navio inimigo
        E: navio do jogador)
    """
    def get_quadrante(self, x, y):
        cord_x = self._dict_alphanum[x]
        return self._matrix2[cord_x][y-1]
    

class Tabuleiro():
    
    _parte_a : TabuleiroParte = None
    _parte_b : TabuleiroParte = None


    def __init__(self):
        self._parte_a = TabuleiroParte()
        self._parte_b = TabuleiroParte()

    def representacao_tabuleiro(self):
        # Esta função cria uma representação textual do tabuleiro
        representacao = ""
        for linha in self._parte_a._matrix2:
            representacao += " ".join(linha) + "\n"
        return representacao
    
    def enviar_tabuleiro(tabuleiro, jogador):
    # Converte a representação do tabuleiro em bytes
    bytes_data = bytes(tabuleiro.representacao_tabuleiro(), 'utf-8')
    jogador.sendall(bytes_data)



    if tabuleiro == COMPUTER_BOARD: #aqui!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            orientation, row, column = random.choice(["linha", "coluna"]), random.randint(0,7), random.randint(0,7)
            if check_ship_fit(ship_length, linha, coluna):
                   #check if ship overlaps
                if ship_overlaps(tabuleiro, linha, coluna, ship_length) == False:

    tabuleiro = Tabuleiro(10)
    navio = Navio(3, 'X')
    tabuleiro.colocar_navio(navio)

    bytes = enviar_tabuleiro(tabuleiro)

        # Envia o tabuleiro para o jogador 1
    jogador_1.sendall(bytes)

        # Envia o tabuleiro para o jogador 2
    jogador_2.sendall(bytes)
    