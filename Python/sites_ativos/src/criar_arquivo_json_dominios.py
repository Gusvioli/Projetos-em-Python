import json

class ProductEncoder(json.JSONEncoder):
    def default(self, obj):
        return obj.__dict__

def criar_arquivo_json_dominios(): 
    for i in range(2, 27):
        with open(f'data/dominios/dominios{i}.json', 'w') as json_file:
            json.dump(
                {"data_criacao": "", "dominios": []},
                json_file,
                ensure_ascii=False,
                indent=2, cls=ProductEncoder
            )

criar_arquivo_json_dominios()
