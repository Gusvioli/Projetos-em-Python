# Lista de nomes de arquivos
nomes_arquivos = ['app_2.py', 'app_3.py', 'app_4.py', 'app_5.py', 'app_6.py', 'app_7.py', 'app_8.py', 'app_9.py', 'app_10.py', 'app_11.py', 'app_12.py', 'app_13.py', 'app_14.py', 'app_15.py', 'app_16.py', 'app_17.py', 'app_18.py', 'app_19.py', 'app_20.py', 'app_21.py', 'app_22.py', 'app_23.py', 'app_24.py', 'app_25.py', 'app_26.py']

def codigo_python(number_of_characters, nome_url_http='nome_url_http', dominios='dominios'):
    return  f"""
import itertools
import time
import pandas as pd
import requests as rqs

from cria_dominio import dominio

number_of_characters = {number_of_characters}

data_dominios = './data/dominios_mais_usados.json'
data_dominios_json = pd.read_json(data_dominios)
extensoes = data_dominios_json["extensoes"]
dominios = extensoes.to_list()

def gerar_combinacoes(characters, dominios, tamanho):
    for combination in itertools.product(characters, repeat=tamanho):
        yield ''.join(combination)

def realizar_requisicao(nome_url_http, dominios):
    try:
        url = f'http://{{nome_url_http}}{{dominios}}'
        r_http = rqs.get(url, timeout=3)
        dominio(nome_url_http, r_http.status_code, r_http.headers, r_http.url, number_of_characters)
    except Exception as e:
        print(e)

def main():
    characters = "abcdefghijklmnopqrstuvwxyz0123456789"

    for nome_url_http in gerar_combinacoes(characters, dominios, number_of_characters):
        realizar_requisicao(nome_url_http, dominios[0])
        time.sleep(0.1)

if __name__ == "__main__":
    main()"""

x = 2
for nome_arquivo in nomes_arquivos:
    with open(f'src/{nome_arquivo}', 'w') as arquivo:
        arquivo.write(codigo_python(x))
    x += 1