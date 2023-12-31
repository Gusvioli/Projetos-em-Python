import sys
sys.path.append('/home/gusvioli/Documentos/projetos/Projetos-em-Python/Python/site_ativos_2_0/src/arquivos_py')

from utils.produc_encoder import ProductEncoder

import json
import time
dataCriacao = time.strftime("%d/%m/%Y %H:%M:%S")

arquivos_jsons = 'src/arquivos_jsons/dominios/dominios'


def dominio(name_url_http, status, headers, url, n_arq):
    with open(f'{arquivos_jsons}{n_arq}.json', 'r') as json_file:
        dom = json.load(json_file)

    lista = dom['dominios']

    dict_lit = {
        "name_url_http": name_url_http,
        "url": url,
        "status": status,
        "headers": headers
    }

    lista.append(dict_lit)

    with open(f'{arquivos_jsons}{n_arq}.json', 'w') as json_file:
        json.dump(
            {"data_criacao": dataCriacao, "dominios": lista},
            json_file,
            ensure_ascii=False,
            indent=2, cls=ProductEncoder)
