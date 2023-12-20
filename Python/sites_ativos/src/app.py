import requests as rqs
import pandas as pd
import json
import time


data_dominios = './data/dominios_mais_usados.json'
data_dominios_json = pd.read_json(data_dominios)
extensoes = data_dominios_json["extensoes"]
extensoes = extensoes.to_list()    
dataCriacao = time.strftime("%d/%m/%Y %H:%M:%S")

class ProductEncoder(json.JSONEncoder):
    def default(self, obj):
        return obj.__dict__    

def dominio(protocolo_nome_extensao, status):
    dict_lit = {
        "endereco_url_http": f'{protocolo_nome_extensao}',
        "status": f'{status}',
    }

    with open('data/dominios.json', 'r') as json_file:
        dom = json.load(json_file)

    lista = dom['dominios']
    lista.append(dict_lit)

    with open(f'data/dominios.json', 'w') as json_file:
        json.dump(
            {"data_criacao": dataCriacao, "dominios": lista },
            json_file,
            ensure_ascii=False,
            indent=2, cls=ProductEncoder)

def generate_all_words(characters):
    all_words = []
    
    for char in characters:
        all_words.append(char)

    current_words = list(all_words)
    

    for _ in range(1, len(characters)):
        new_words = []
        for word in current_words:
            for char in characters:
                new_words.append(word + char)
                for ext in extensoes:
                    try:
                        if len(word + char) > 1:
                            v = f'http://{word + char}{ext}'
                            r_http = rqs.get(v, timeout=1)
                            dominio(
                                v,
                                r_http.status_code
                            )
                        else:
                            pass
                    except Exception as e:
                        print(e)
        all_words.extend(new_words)
        current_words = new_words

    return all_words

characters = "abcdefghijklmnopqrstuvwxyz"
all_possible_words = generate_all_words(characters)


print(all_possible_words)

###################################