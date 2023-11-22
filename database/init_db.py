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
        id INTEGER,
        pontuacao INTEGER DEFAULT 0,
        nome TEXT,
        email TEXT,
        senha TEXT,
        PRIMARY KEY(id)
    );
'''

sql_popula_table_jogadores = [
    "INSERT INTO Jogadores (id, nome, pontuacao, email, senha) VALUES (0, 'Admin', 0; 'admin@admin.com', '!@$%$#5%');",
    "INSERT INTO Jogadores (id, nome, pontuacao, email, senha) VALUES (1, 'Guilherme Ferrari', 0, 'guilherme@guilherme.com','!#%$¨@!');",
    "INSERT INTO Jogadores (id, nome, pontuacao, email, senha) VALUES (2, 'João Otávio Neumann', 0,  'joao@joao.com','!#%$¨@!');",
    "INSERT INTO Jogadores (id, nome, pontuacao, email, senha) VALUES (3, 'Luigi Veloso', 0,  'luigi@luigi.com','!#%$¨@!');",
    "INSERT INTO Jogadores (id, nome, pontuacao, email, senha) VALUES (4, 'Nicolas Oliveira', 0,  'nicolas@nicolas.com','!#%$¨@!');",
    "INSERT INTO Jogadores (id, nome, pontuacao, email, senha) VALUES (5, 'Teste', 0,  'teste@teste.com','!#%$¨@!');"
]

# Cria tabela jogador
executa_sql(sql_create_table_jogador)

# Popula a tabela jogadores 
for x in sql_popula_table_jogadores:
    executa_sql(x)