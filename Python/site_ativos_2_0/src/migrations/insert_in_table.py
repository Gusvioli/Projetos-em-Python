from connect_db import connect
import json
import os
import time

from dotenv import load_dotenv

load_dotenv()

database = os.getenv('DATABASE')
table = os.getenv('TABLE')

def listar_arquivos_em_diretorio(caminho_diretorio):
    try:
        lista = []
        arquivos = os.listdir(caminho_diretorio)
        
        for arquivo in arquivos:
            lista.append(arquivo)
            
        return lista
    except FileNotFoundError:
        print(f"O diretório '{caminho_diretorio}' não foi encontrado.")
        return None

def get_arquivo_json():
    data = []
    for x in listar_arquivos_em_diretorio('src/arquivos_jsons/dominios/'):
        with open(f"src/arquivos_jsons/dominios/{x}", "r") as file:
            end = json.load(file)
            data.append(end['dominios'])

    return data[0]

def insert(table, database):
    conn = connect()
    mycursor = conn.cursor()
    mycursor.execute(f"USE {database}")

    data = get_arquivo_json()    
    
    try:
        for x in data:
            sql_insert = f"INSERT INTO {database}.{table} (name_url_http, url, status, headers) VALUES (%s, %s, %s, %s)"

            mycursor.execute(sql_insert, (x['name_url_http'], x['url'], x['status'], json.dumps(x['headers'])))

            conn.commit()

        sql_select_all = "SELECT * FROM sites"
        mycursor.execute(sql_select_all)
        resultado = mycursor.fetchall()
        qtds_sites = len(resultado)

        print(f"(OK!) {len(data)} sites inseridos na tabela: '{table}' em: {time.strftime('%d/%m/%Y %H:%M:%S')} com um total de: {qtds_sites} sites.")
    except Exception as e:
        print(f"Erro: {e}")

    finally:
        connect().commit()
        mycursor.close()

if __name__ == "__main__":
    while True:
        time.sleep(5)
        insert(table, database) # Insere os sites na tabela
        time.sleep(60 * 60)