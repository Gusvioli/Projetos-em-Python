import sys
import os
import pickle
# Adicione o diretório ao sys.path
diretorio_atual = os.path.dirname(os.path.abspath(__file__))

sys.path.append(os.path.join(diretorio_atual, '/home/gusvioli/Documentos/projetos/Projetos-em-Python/Python/site_ativos_2_0/src/arquivos_py'))

sys.path.append(os.path.join(diretorio_atual, '/home/gusvioli/Documentos/projetos/Projetos-em-Python/Python/site_ativos_2_0/src/migrations'))

import itertools
import time
import pandas as pd
import requests as rqs

from insert_in_table import insert
from dotenv import load_dotenv

import select_db

load_dotenv()

sl_all = select_db.select_db_all(os.getenv('DATABASE'), os.getenv('TABLE'))

number_of_characters = 13

data_dominios = 'src/arquivos_jsons/dominios_mais_usados.json'
data_dominios_json = pd.read_json(data_dominios)
extensoes = data_dominios_json["extensoes"]
dominios = extensoes.to_list()

# Função para salvar o estado
def salvar_estado(nome_arquivo, estado):
    with open(nome_arquivo, 'wb') as arquivo:
        pickle.dump(estado, arquivo)

# Função para carregar o estado
def carregar_estado(nome_arquivo):
    try:
        with open(nome_arquivo, 'rb') as arquivo:
            return pickle.load(arquivo)
    except FileNotFoundError:
        return None

def gerar_combinacoes(characters, dominios, tamanho):
    for combination in itertools.product(characters, repeat=tamanho):
        yield ''.join(combination)

def realizar_requisicao(nome_url_http, dominios, array_name_url_http):
    if nome_url_http not in array_name_url_http:
        try:
            url = f'http://{nome_url_http}{dominios}'
            salvar_estado('estado_url_name.pkl', {'url': url, 'nome_url_http': nome_url_http})

            estado = carregar_estado('estado_url_name.pkl')
            
            if estado is None:
                r_http = rqs.get(url, timeout=3)
                        
                insert(nome_url_http, r_http.url, r_http.status_code, dict(r_http.headers))
            else:
                r_http = rqs.get(estado['url'], timeout=3)
                        
                insert(estado['nome_url_http'], r_http.url, r_http.status_code, dict(r_http.headers))
        except Exception:
            return
    else:
        print(f"(X) '{nome_url_http}' já existe no sistema")

def main():
    characters = "abcdefghijklmnopqrstuvwxyz0123456789"
    array_name_url_http_in = [i[0] for i in sl_all]
    array_name_url_http = [x for x in array_name_url_http_in if x == number_of_characters]

    for nome_url_http in gerar_combinacoes(characters, dominios, number_of_characters):
        realizar_requisicao(nome_url_http, dominios[0], array_name_url_http)
        time.sleep(0.3) # 0.3

if __name__ == "__main__":
    main()