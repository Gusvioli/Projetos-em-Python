import time
from dbs.db import insert_sites
from verificar_tam_arquivos_e_separar import verificar_tam_arquivos_e_separar
from limpar_duplicatas import listar_arquivos_em_diretorio, remover_de_todos
# from contar_url_ativas import contar

tempo = 60 * 60
x = 1

while True:
    try:
        remover_de_todos(listar_arquivos_em_diretorio('data/dominios'))
        time.sleep(5)
        verificar_tam_arquivos_e_separar()
        time.sleep(3)
        insert_sites('./data/dominios')
        time.sleep(3)
        print(f'N-{x} Executou em: {time.strftime("%d/%m/%Y %H:%M:%S")}')
        x += 1
        time.sleep(tempo) 
    except Exception as e:
        print(e)