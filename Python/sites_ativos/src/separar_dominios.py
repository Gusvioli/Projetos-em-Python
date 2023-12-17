import json
import pandas as pd

get_json_dimis = pd.read_json('./data/dominios.json')

dominios = get_json_dimis['dominios'].to_list()

listaDoms = {
    2: [], 3: [], 4: [], 5: [], 6: [], 7: [],
    8: [], 9: [], 10: [], 11: [], 12: [], 13: [], 14: [], 15: [],
    16: [], 17: [], 18: [], 19: [], 20: [], 21: [], 22: [], 23: [],
    24: [], 25: [], 26: []
}


class ProductEncoder(json.JSONEncoder):
    def default(self, obj):
        return obj.__dict__


def eliminar_duplicatas(lista):
    chaves_unicas = set()
    lista_sem_duplicatas = []
    for dicionario in lista:
        tupla_dicionario = tuple(sorted(dicionario.items()))
        if tupla_dicionario not in chaves_unicas:
            chaves_unicas.add(tupla_dicionario)
            lista_sem_duplicatas.append(dicionario)

    return lista_sem_duplicatas


def cria_arquivos_dominios(val, listaDoms):
    ver = pd.read_json(f'./data/dominios/dominios{val}.json')
    v = ver['dominios'].to_list()
    v.extend(listaDoms)

    with open(f'data/dominios/dominios{val}.json', 'w') as json_file:
        json.dump(
            {"dominios": eliminar_duplicatas(v)},
            json_file,
            ensure_ascii=False,
            indent=2, cls=ProductEncoder
        )


for i in dominios:
    sel = i['endereco_url_http'].split('/')[2].split('.')[0]
    if 2 <= len(sel) <= 26:
        listaDoms[len(sel)].append(i)

for x in range(2, 27):
    cria_arquivos_dominios(x, listaDoms[x])

with open(f'data/dominios.json', 'w') as json_file:
    json.dump(
        {"dominios": [{
            "endereco_url_http": "https://www.test.com",
            "status": "000",
            "data_criacao": "00/00/0000 00:00:00"
        }]},
        json_file,
        ensure_ascii=False,
        indent=2, cls=ProductEncoder
    )
