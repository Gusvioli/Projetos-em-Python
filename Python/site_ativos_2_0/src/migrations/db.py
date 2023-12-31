import sys
sys.path.append('/home/gusvioli/Documentos/projetos/Projetos-em-Python/Python/site_ativos_2_0/src/migrations')
from dotenv import load_dotenv
import os

from connect_db import connect
from create_db import criar_db
from create_table import criar_table

load_dotenv()

def verificar_tamanho_tabela(database, nome_tabela):
    mydb = connect()
    mycursor = mydb.cursor()
    consulta = f"SELECT COUNT(*) FROM {database}.{nome_tabela}"
    mycursor.execute(consulta)
    resultados = mycursor.fetchall()
    return resultados[0][0]

def db_run():
    database = os.getenv('DATABASE')
    table = os.getenv('TABLE')

    criar_db(database)
    criar_table(table, database)
