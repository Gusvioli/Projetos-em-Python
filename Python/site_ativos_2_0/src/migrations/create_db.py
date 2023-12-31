from connect_db import connect

def criar_db(database):
    conn = connect()
    mycursor = conn.cursor()

    try:
        mycursor.execute(f"CREATE DATABASE IF NOT EXISTS {database}")
        print(f"(OK!) Banco de dados '{database}'")
    except Exception as e:
        print(f"Erro: {e}")

    finally:
        connect().commit()
        mycursor.close()