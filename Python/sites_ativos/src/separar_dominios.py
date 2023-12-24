import json
import pandas as pd
import time

from limpar_duplicatas import limpar_duplicatas

get_json_dimis = pd.read_json('./data/dominios.json')
dominios = get_json_dimis['dominios'].to_list()
dataCriacao = time.strftime("%d/%m/%Y %H:%M:%S")

listaDoms = {
    2: [], 3: [], 4: [], 5: [], 6: [], 7: [],
    8: [], 9: [], 10: [], 11: [], 12: [], 13: [], 14: [], 15: [],
    16: [], 17: [], 18: [], 19: [], 20: [], 21: [], 22: [], 23: [],
    24: [], 25: [], 26: []
}

class ProductEncoder(json.JSONEncoder):
    def default(self, obj):
        return obj.__dict__

def cria_arquivos_dominios(val, listaDoms):
    ver = pd.read_json(f'./data/dominios/dominios{val}.json')
    v = ver['dominios'].to_list()
    v.extend(listaDoms)

    with open(f'data/dominios/dominios{val}.json', 'w') as json_file:
        json.dump(
            {"data_criacao": dataCriacao, "dominios": v},
            json_file,
            ensure_ascii=False,
            indent=2, cls=ProductEncoder
        )

def executar():
    for i in dominios:
        sel = i['name_url_http']
        if len(sel) <= 26 and len(sel) >= 2:
            listaDoms[len(sel)].append(i)

    for x in range(2, 27):
        cria_arquivos_dominios(x, listaDoms[x])
        limpar_duplicatas(x)

    with open(f'data/dominios.json', 'w') as json_file:
        json.dump(
            {"data_criacao": '', "dominios": []},
            json_file,
            ensure_ascii=False,
            indent=2, cls=ProductEncoder
        )