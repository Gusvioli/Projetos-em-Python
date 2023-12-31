import sys
import os
# Adicione o diretório ao sys.path
diretorio_atual = os.path.dirname(os.path.abspath(__file__))
diretorio_do_modulo = os.path.join(diretorio_atual, '/home/gusvioli/Documentos/projetos/Projetos-em-Python/Python/site_ativos_2_0/src/migrations')
sys.path.append(diretorio_do_modulo)

from connect_db import connect

def select_db_all(database, table):
    try:
        conn = connect()
        mycursor = conn.cursor()

        sql_select_all = f"SELECT * FROM {database}.{table}"
        mycursor.execute(sql_select_all)
        print(f"(OK!) Db/table({database}/{table}) selecionados")
        return mycursor.fetchall()
    except Exception as e:
        print(f"Erro: {e}")
    finally:
        connect().commit()
        mycursor.close()

if __name__ == "__main__":
    select_db_all("site_ativos", "url_http")