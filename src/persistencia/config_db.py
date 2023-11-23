import sqlite3

class ConfigDB():

    def executa_sql(codigo_sql, valores):
        with sqlite3.connect("../batalha_naval.sqlite") as conn:
            if (valores != False):
                try:
                    cursor = conn.cursor()
                    return cursor.execute(codigo_sql, valores)
                except sqlite3.Error as e:
                    print(e)
            else:
                try:
                    cursor = conn.cursor()
                    return cursor.execute(codigo_sql)
                except sqlite3.Error as e:
                    print(e)
