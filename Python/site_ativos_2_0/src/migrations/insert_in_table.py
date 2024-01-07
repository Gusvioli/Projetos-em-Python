from connect_db import connect
import json
import os
import time

from dotenv import load_dotenv

load_dotenv()
   
database = os.getenv('DATABASE')
table = os.getenv('TABLE')

def insert(name_url_http, url, status, headers): 
    conn = connect()
    mycursor = conn.cursor()
    mycursor.execute(f"USE {database}")

    try:
        sql_insert = f"INSERT INTO {database}.{table} (name_url_http, url, status,headers) VALUES (%s, %s, %s, %s)"
        mycursor.execute(sql_insert, (name_url_http, url, status, (json.dumps(headers))))

        conn.commit()

        sql_select_all = "SELECT * FROM sites"
        mycursor.execute(sql_select_all)
        resultado = mycursor.fetchall()
        qtds_sites = len(resultado)

        porcentagem_progresso = (qtds_sites / 200000000) * 100

        print(f"(OK!) {time.strftime('%d/%m/%Y %H:%M:%S')} | Name: '{name_url_http}' | Sites: {qtds_sites: <6}/200mi | Progresso: {porcentagem_progresso:.2f}% Completo")


    except Exception as e:
        print(f"Erro: {e}")

    finally:
        connect().commit()
        mycursor.close()# Insere os sites na tabela