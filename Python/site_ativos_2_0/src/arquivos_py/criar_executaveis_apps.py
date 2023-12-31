# Lista de nomes de arquivos
nomes_arquivos = ['app_2.py', 'app_3.py', 'app_4.py', 'app_5.py', 'app_6.py', 'app_7.py', 'app_8.py', 'app_9.py', 'app_10.py', 'app_11.py', 'app_12.py', 'app_13.py', 'app_14.py', 'app_15.py', 'app_16.py', 'app_17.py', 'app_18.py', 'app_19.py', 'app_20.py', 'app_21.py', 'app_22.py', 'app_23.py', 'app_24.py', 'app_25.py', 'app_26.py']

def codigo_python(number_of_characters, nome_url_http='nome_url_http', dominios='dominios'):
    return  f"""import sys
import os
# Adicione o diretório ao sys.path
diretorio_atual = os.path.dirname(os.path.abspath(__file__))

sys.path.append(os.path.join(diretorio_atual, '/home/gusvioli/Documentos/projetos/Projetos-em-Python/Python/site_ativos_2_0/src/arquivos_py'))

sys.path.append(os.path.join(diretorio_atual, '/home/gusvioli/Documentos/projetos/Projetos-em-Python/Python/site_ativos_2_0/src/migrations'))

import itertools
import time
import pandas as pd
import requests as rqs

from cria_dominio import dominio
from dotenv import load_dotenv

import select_db
import cria_dominio

load_dotenv()

sl_all = select_db.select_db_all(os.getenv('DATABASE'), os.getenv('TABLE'))

number_of_characters = {number_of_characters}
array_name_url_http = [i[0] for i in sl_all]
array_name_url_http = [x for x in array_name_url_http if len(x) == number_of_characters]

data_dominios = 'src/arquivos_jsons/dominios_mais_usados.json'
data_dominios_json = pd.read_json(data_dominios)
extensoes = data_dominios_json["extensoes"]
dominios = extensoes.to_list()

def gerar_combinacoes(characters, dominios, tamanho):
    for combination in itertools.product(characters, repeat=tamanho):
        yield ''.join(combination)

def realizar_requisicao(nome_url_http, dominios, array_name_url_http):
    if nome_url_http not in array_name_url_http:
        try:
            url = f'http://{{nome_url_http}}{{dominios}}'
            r_http = rqs.get(url, timeout=3)
            cria_dominio.dominio(nome_url_http, r_http.status_code, r_http.headers, r_http.url, number_of_characters)
            print(f"(OK) '{{nome_url_http}}' adicionado com sucesso")
        except Exception:
            print(f"(ERRO) ao fazer a requisicao '{{url}}'")
    else:
        print(f"(X) '{{nome_url_http}}' já existe no sistema")

def main():
    characters = "abcdefghijklmnopqrstuvwxyz0123456789"

    for nome_url_http in gerar_combinacoes(characters, dominios, number_of_characters):
        realizar_requisicao(nome_url_http, dominios[0], array_name_url_http)
        time.sleep(0.3) # 0.3

if __name__ == "__main__":
    main()"""

def run():
    x = 2
    for nome_arquivo in nomes_arquivos:
        with open(f'src/arquivos_py/apps/{nome_arquivo}', 'w') as arquivo:
            arquivo.write(codigo_python(x))
        x += 1
    print("Arquivos apps criados com sucesso!")

if __name__ == "__main__":
    run()