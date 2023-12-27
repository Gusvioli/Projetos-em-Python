import json
import os
from dbs.connect_db import connect

def listar_arquivos_em_diretorio(caminho_diretorio):    
    lista = []
    arquivos = os.listdir(caminho_diretorio)
    
    for arquivo in arquivos:
        lista.append(arquivo)
        
    return lista

def get_data_arquivos(arquivo_json):
    data_list = []
    for arquivo in listar_arquivos_em_diretorio(arquivo_json):
        with open(f'{arquivo_json}/{arquivo}', 'r') as json_file:
            data = json.load(json_file)
            for d in data['dominios']:
                data_list.append(d)
    return data_list

def insert_sites(arquivo_json):
    mydb = connect()
    mycursor = mydb.cursor()
    
    sql_select = "SELECT * FROM sites WHERE name_url_http = %s AND url = %s"
    sql_insert = "INSERT INTO sites (name_url_http, url, status, headers) VALUES (%s, %s, %s, %s)"

    for data in get_data_arquivos(arquivo_json):
        mycursor.execute(sql_select, (data['name_url_http'], data['url']))
        resultado = mycursor.fetchone()

        if resultado:
            print(f"Registro para {data['name_url_http']} - {data['url']} já existe. Não foi inserido novamente.")
        else:
            mycursor.execute(sql_insert, (data['name_url_http'], data['url'], data['status'], json.dumps(data['headers'])))
            mydb.commit()
            print(mycursor.rowcount, "foi inserido.")
            
    mycursor.close()
    mydb.close()

insert_sites('./data/dominios')

