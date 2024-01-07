from connect_db import connect
import os
import time
from dotenv import load_dotenv

load_dotenv()

database = os.getenv('DATABASE')
table = os.getenv('TABLE')

def limpar_duplicatas():
    while True:
        try:
            conn = connect()
            mycursor = conn.cursor()

            mycursor.execute(f"USE {database}")

            # Consulta para encontrar e contar duplicatas
            sql_select_duplicates = """
                SELECT name_url_http, COUNT(*) AS contador
                FROM sites
                GROUP BY name_url_http
                HAVING COUNT(*) > 1
            """

            mycursor.execute(sql_select_duplicates)
            duplicatas = mycursor.fetchall()

            qtds_sites = len(duplicatas)

            # Remover as duplicatas diretamente da tabela
            for duplicata in duplicatas:
                sql_delete_duplicate = f"""
                    DELETE FROM {table}
                    WHERE name_url_http = '{duplicata[0]}'
                    LIMIT {duplicata[1] - 1}
                """
                mycursor.execute(sql_delete_duplicate)

            # Comitar as alterações
            conn.commit()

            porcentagem_progresso = (qtds_sites / 200000000) * 100

            print(f"(DELETE!) Tabela '{table}' foi limpa em: {time.strftime('%d/%m/%Y %H:%M:%S')} com um total de: {qtds_sites} sites limpos")
            
        except Exception as e:
            print(f"Erro: {e}")

        finally:
            mycursor.close()
            conn.close()
        time.sleep(60)

if __name__ == "__main__":
    limpar_duplicatas()
