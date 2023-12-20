import pandas as pd


def contar():
    lista_contagem = 0
    for n in range(2, 27):
        itens = pd.read_json(f'data/dominios/dominios{n}.json')['dominios']
        for l in itens:
            if l['endereco_url_http'] != 'http://www.test-.com':
                lista_contagem += len(l)
    return lista_contagem