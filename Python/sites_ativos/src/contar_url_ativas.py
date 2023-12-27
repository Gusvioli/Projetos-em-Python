import os
import pandas as pd

qtds_de_pagina_ativas = 0

def listar_arquivos_em_diretorio(caminho_diretorio):
    try:
        lista = []
        arquivos = os.listdir(caminho_diretorio)
        
        for arquivo in arquivos:
            lista.append(arquivo)
            
        return lista
    except FileNotFoundError:
        print(f"O diretório '{caminho_diretorio}' não foi encontrado.")
        return None


def contar():
    lista_contagem = 0
    data_dominios = listar_arquivos_em_diretorio('data/dominios')
    for n in data_dominios:
        itens = pd.read_json(f'data/dominios/{n}')['dominios']
        for l in itens:
            lista_contagem += len(l)
    return lista_contagem

ver = contar()
print(ver)