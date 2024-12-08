import sqlite3
import os

# Classe para configuração do banco de dados SQLite
class ConfigDB():
    # Obtém o caminho absoluto do banco de dados
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    DATABASE_PATH = os.path.join(BASE_DIR, "batalha_naval.sqlite")

    @classmethod
    def executa_sql(cls, codigo_sql, valores):
        with sqlite3.connect(cls.DATABASE_PATH) as conn:
            try:
                cursor = conn.cursor()
                if valores:
                    return cursor.execute(codigo_sql, valores)
                else:
                    return cursor.execute(codigo_sql)
            except sqlite3.Error as e:
                print(f"Erro ao executar SQL: {e}")
                return None
