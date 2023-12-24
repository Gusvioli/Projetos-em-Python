import json
import time
dataCriacao = time.strftime("%d/%m/%Y %H:%M:%S")

class ProductEncoder(json.JSONEncoder):
    def default(self, obj):
        return obj.__dict__ 

def dominio(name_url_http, status, headers, url, n_arq):
    with open(f'data/dominios/dominios{n_arq}.json', 'r') as json_file:
        dom = json.load(json_file)

    lista = dom['dominios']

    dict_lit = {
        "name_url_http": name_url_http,
        "url": url,
        "status": status,
        "headers": headers
    }

    lista.append(dict_lit)

    with open(f'data/dominios/dominios{n_arq}.json', 'w') as json_file:
        json.dump(
            {"data_criacao": dataCriacao, "dominios": lista },
            json_file,
            ensure_ascii=False,
            indent=2, cls=ProductEncoder) 