import sys
import time
sys.path.append('/home/gusvioli/Documentos/projetos/Projetos-em-Python/Python/site_ativos_2_0/src/arquivos_py')

from utils.produc_encoder import ProductEncoder
import json
import os


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
    
def limpar():
    for i in listar_arquivos_em_diretorio('src/arquivos_jsons/dominios'):
        with open(f"src/arquivos_jsons/dominios/{i}", "r") as file:
            jend = json.load(file)
            tam = len(jend['dominios'])
        if tam >= 500:
            with open(f'src/arquivos_jsons/dominios/{i}', 'w') as json_file:
                json.dump(
                    {"data_criacao": "", "dominios": []},
                    json_file,
                    ensure_ascii=False,
                    indent=2, cls=ProductEncoder
                )
            print(f'(OK) O arquivo {i} foi limpo e iniciado.')
        else:
            print(f'(X) O arquivo {i} não foi limpo e iniciado.')

if __name__ == "__main__":
    while True:
        time.sleep(5)
        limpar()# Insere os sites na tabela
        time.sleep(60 * 60)
    