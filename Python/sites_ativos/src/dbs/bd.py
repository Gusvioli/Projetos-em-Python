import json
import os
from dbs.connect_db import connect
from limpar_dominios_jsons import excluir_site_registrado

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
    sql_select_all = "SELECT * FROM sites"

    qtds_sites_add = 0

    for data in get_data_arquivos(arquivo_json):
        mycursor.execute(sql_select, (data['name_url_http'], data['url']))
        resultado = mycursor.fetchone()

        if resultado:
            excluir_site_registrado(data['name_url_http'])
            print(f"(X) Registro para {data['name_url_http']} - {data['url']} já existe. Não foi inserido novamente.")
        else:
            mycursor.execute(sql_insert, (data['name_url_http'], data['url'], data['status'], json.dumps(data['headers'])))
            mydb.commit()
            excluir_site_registrado(data['name_url_http'])
            print(f"(OK) Registro para {data['name_url_http']} - {data['url']} e {mycursor.rowcount}, foi inserido.")
            qtds_sites_add += 1
    
    mycursor.execute(sql_select_all)
    resultado = mycursor.fetchall()
    qtds_sites = len(resultado)

    print(f"Total de sites inseridos: {qtds_sites_add}")
    print(f"Total de sites adicionados: {qtds_sites}")
    print('(OK) Realizado a inserção de sites no banco de dados')
            
    mycursor.close()
    mydb.close()

insert_sites('./data/dominios')

