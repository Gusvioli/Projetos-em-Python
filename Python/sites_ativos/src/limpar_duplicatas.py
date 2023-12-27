import json
import os
import time

dataCriacao = time.strftime("%d/%m/%Y %H:%M:%S")

class ProductEncoder(json.JSONEncoder):
    def default(self, obj):
        return obj.__dict__

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

def remover_duplicatas(arquivo_json):
    with open(arquivo_json, 'r') as json_file:
        data = json.load(json_file)

    unique_names = set()
    unique_dominios = []

    for dominio in data["dominios"]:
        name = dominio["name_url_http"]
        if name not in unique_names:
            unique_names.add(name)
            unique_dominios.append(dominio)

    with open(arquivo_json, 'w') as json_file:
        json.dump(
            {"data_criacao": dataCriacao, "dominios": unique_dominios},
            json_file,
            ensure_ascii=False,
            indent=2,
            cls=ProductEncoder
        )

def remover_de_todos(all_json):
    for x in all_json:
        remover_duplicatas(f'data/dominios/{x}')

remover_de_todos(listar_arquivos_em_diretorio('data/dominios'))