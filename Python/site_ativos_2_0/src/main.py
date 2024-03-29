import sys
import os
import pickle

# Adicione o diretório ao sys.path
diretorio_atual = os.path.dirname(os.path.abspath(__file__))

sys.path.append(os.path.join(diretorio_atual, '/home/gusvioli/Documentos/projetos/Projetos-em-Python/Python/site_ativos_2_0/src'))

sys.path.append(os.path.join(diretorio_atual, '/home/gusvioli/Documentos/projetos/Projetos-em-Python/Python/site_ativos_2_0/src/arquivos_py'))

sys.path.append(os.path.join(diretorio_atual, '/home/gusvioli/Documentos/projetos/Projetos-em-Python/Python/site_ativos_2_0/src/migrations'))

from arquivos_py.rodar_todos_apps import rodar
from migrations.select_db import select_db_all
from migrations.insert_in_table import insert
from migrations.db import verificar_tamanho_tabela, db_run
from arquivos_py.criar_executaveis_apps import run
from arquivos_py.criar_arquivo_json_dominios import criar_arquivo_json_dominios
from arquivos_py.limpar_dominios_json import limpar

# Função para salvar o estado
def salvar_estado(nome_arquivo, estado):
    with open(nome_arquivo, 'wb') as arquivo:
        pickle.dump(estado, arquivo)

# Função para carregar o estado
def carregar_estado(nome_arquivo):
    try:
        with open(nome_arquivo, 'rb') as arquivo:
            return pickle.load(arquivo)
    except FileNotFoundError:
        return None

def main():
    try:
        db_run()
        run()
        rodar()
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
