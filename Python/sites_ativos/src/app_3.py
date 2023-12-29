
import itertools
import time
import pandas as pd
import requests as rqs

from cria_dominio import dominio

number_of_characters = 3

data_dominios = './data/dominios_mais_usados.json'
data_dominios_json = pd.read_json(data_dominios)
extensoes = data_dominios_json["extensoes"]
dominios = extensoes.to_list()

def gerar_combinacoes(characters, dominios, tamanho):
    for combination in itertools.product(characters, repeat=tamanho):
        yield ''.join(combination)

def realizar_requisicao(nome_url_http, dominios):
    try:
        url = f'http://{nome_url_http}{dominios}'
        r_http = rqs.get(url, timeout=3)
        dominio(nome_url_http, r_http.status_code, r_http.headers, r_http.url, number_of_characters)
    except Exception as e:
        print(e)

def main():
    characters = "abcdefghijklmnopqrstuvwxyz0123456789"

    for nome_url_http in gerar_combinacoes(characters, dominios, number_of_characters):
        realizar_requisicao(nome_url_http, dominios[0])
        # time.sleep(0.1)

if __name__ == "__main__":
    main()