import json
import pandas as pd
import time

dataCriacao = time.strftime("%d/%m/%Y %H:%M:%S")

class ProductEncoder(json.JSONEncoder):
    def default(self, obj):
        return obj.__dict__

def limpar_duplicatas(p1):
    new_dict = pd.read_json(f'data/dominios/dominios{p1}.json') 
    seu_dict = new_dict['dominios'].to_list()
    unique_list = list()
    for i in range(len(seu_dict)):
        if seu_dict[i] not in seu_dict[i + 1:]:
            unique_list.append(seu_dict[i])

    with open(f'data/dominios/dominios{p1}.json', 'w') as json_file:
        json.dump(
            {"data_criacao": dataCriacao, "dominios": unique_list},
            json_file,
            ensure_ascii=False,
            indent=2, cls=ProductEncoder
        )
