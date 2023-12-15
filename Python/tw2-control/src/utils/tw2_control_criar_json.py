import json

def criar_json(se_dados, name_arquivo='data/default.json'):
    with open(name_arquivo, 'w') as json_file:
        json.dump(se_dados, json_file, ensure_ascii=False, indent=2)