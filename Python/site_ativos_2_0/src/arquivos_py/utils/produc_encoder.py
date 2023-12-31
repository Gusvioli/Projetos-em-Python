import sys
sys.path.append('/home/gusvioli/Documentos/projetos/Projetos-em-Python/Python/site_ativos_2_0/src/arquivos_py/utils')

import json


class ProductEncoder(json.JSONEncoder):
    def default(self, obj):
        return obj.__dict__
