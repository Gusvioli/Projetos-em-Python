import requests
from bs4 import BeautifulSoup
import json

import pandas as pd

#################################

# v = requests.get('https://registro.br/dominio/categorias/', auth=('GUVOL65', 'G1u5s9g3u5s7'))
# soup = BeautifulSoup(v.text, 'html.parser')
# gets = soup.find_all('strong')

# for i in gets:
#     print(f'".{i.text}"', end=',')

#################################

# def verifica_se_existe(procura):
#     get_json_dimis = pd.read_json('./data/dominios.json')
#     dominios = get_json_dimis['dominios'].to_list()

#     listaDoms = []

#     for i in dominios:
#         listaDoms.append(i['endereco_url_http'])

#     resultados = list(filter(lambda x: procura in x, listaDoms))
#     return len(resultados) >= 1

# print(verifica_se_existe('http://www.google.com.br'))

#################################


# get_json_dimis = pd.read_json('./data/dominios.json')
# dominios = get_json_dimis['dominios'].to_list()

# listaDoms = []
# x = 0
# for i in dominios:
#     dict_lit = {
#         "ID": f'{x}',
#         "endereco_url_http": f'{i["endereco_url_http"]}',
#         "status": f'{i["status"]}',
#         "data_criacao": f'{i["data_criacao"]}'
#     },
#     listaDoms.extend(dict_lit)
#     x += 1

# class ProductEncoder(json.JSONEncoder):
#     def default(self, obj):
#         return obj.__dict__
    
# with open(f'data/dominios.json', 'w') as json_file:
#         json.dump(
#             { "dominios": listaDoms},
#             json_file,
#             ensure_ascii=False,
#             indent=2, cls=ProductEncoder)

################################# 

