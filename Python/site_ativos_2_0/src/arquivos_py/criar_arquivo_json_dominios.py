import sys
sys.path.append('/home/gusvioli/Documentos/projetos/Projetos-em-Python/Python/site_ativos_2_0/src/arquivos_py')

import json

from utils.produc_encoder import ProductEncoder

def criar_arquivo_json_dominios(): 
    for i in range(2, 27):
        with open(f'src/arquivos_jsons/dominios/dominios{i}.json', 'w') as json_file:
            json.dump(
                {"data_criacao": "", "dominios": []},
                json_file,
                ensure_ascii=False,
                indent=2, cls=ProductEncoder
            )
    print("Arquivos JSON criados com sucesso!")


if __name__ == "__main__":
    criar_arquivo_json_dominios()
