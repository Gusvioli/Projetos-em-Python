import json
import os
import time

dataCriacao = time.strftime("%d/%m/%Y %H:%M:%S")

def listar_arquivos_em_diretorio(caminho_diretorio):    
    lista = []
    arquivos = os.listdir(caminho_diretorio)
    
    for arquivo in arquivos:
        lista.append(arquivo)
        
    return lista

class ProductEncoder(json.JSONEncoder):
    def default(self, obj):
        return obj.__dict__

def excluir_site_registrado(nome_arquivo_json, caminho_diretorio='data/dominios'):
    for i in listar_arquivos_em_diretorio(caminho_diretorio):        
        with open(f'{caminho_diretorio}/{i}', 'r') as json_file:
            data = json.load(json_file)

        names = set()
        unique_dominios = []

        for dominio in data["dominios"]:
            if nome_arquivo_json not in names:
                names.add(nome_arquivo_json)
                unique_dominios.append(dominio)

        with open(f'{caminho_diretorio}/{i}', 'w') as json_file:
            json.dump(
                {"data_criacao": dataCriacao, "dominios": unique_dominios},
                json_file,
                ensure_ascii=False,
                indent=2,
                cls=ProductEncoder
            )

        if len(unique_dominios) <= 1 and len(i.split('-')) > 1:
            os.remove(f'{caminho_diretorio}/{i}')
            print(f"(X) Arquivo {i} foi removido.")