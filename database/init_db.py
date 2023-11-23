import sqlite3 

arquivo_banco = "batalha_naval.sqlite"

def executa_sql(codigo_sql):
    with sqlite3.connect(arquivo_banco) as conn:
        try:
            cursor = conn.cursor()
            cursor.execute(codigo_sql)
        except sqlite3.Error as e:
            print(e)

sql_create_table_jogador = '''
    CREATE TABLE Jogadores(
        id INTEGER PRIMARY KEY,
        pontuacao INTEGER DEFAULT 0,
        nome TEXT UNIQUE,
        email TEXT,
        senha TEXT
    );
'''

sql_popula_table_jogadores = [
    "INSERT INTO Jogadores (nome, pontuacao, email, senha) VALUES ('Admin', 0; 'admin@admin.com', '!@$%$#5%');",
    "INSERT INTO Jogadores (nome, pontuacao, email, senha) VALUES ('Guilherme Ferrari', 1, 'guilherme@guilherme.com','!#%$¨@!');",
    "INSERT INTO Jogadores (nome, pontuacao, email, senha) VALUES ('João Otávio Neumann', 2,  'joao@joao.com','!#%$¨@!');",
    "INSERT INTO Jogadores (nome, pontuacao, email, senha) VALUES ('Luigi Veloso', 3,  'luigi@luigi.com','!#%$¨@!');",
    "INSERT INTO Jogadores (nome, pontuacao, email, senha) VALUES ('Nicolas Oliveira', 4,  'nicolas@nicolas.com','!#%$¨@!');",
    "INSERT INTO Jogadores (nome, pontuacao, email, senha) VALUES ('Teste', 5,  'teste@teste.com','!#%$¨@!');"
]

# Cria tabela jogador
executa_sql(sql_create_table_jogador)

# Popula a tabela jogadores 
for x in sql_popula_table_jogadores:
    executa_sql(x)