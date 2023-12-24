import pandas as pd

qtds_de_pagina_ativas = {
    'qtds': 0
    }

def contar():
    lista_contagem = 0
    for n in range(2, 27):
        itens = pd.read_json(f'data/dominios/dominios{n}.json')['dominios']
        for l in itens:
            lista_contagem += len(l)
    qtds_de_pagina_ativas['qtds'] = lista_contagem
    return qtds_de_pagina_ativas['qtds']

ver = contar()
print(ver)