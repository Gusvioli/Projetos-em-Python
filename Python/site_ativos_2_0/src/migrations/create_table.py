from connect_db import connect


def criar_table(table, database):
    conn = connect()
    mycursor = conn.cursor()

    mycursor.execute(f"USE {database}")
    
    try:
        mycursor.execute(f"CREATE TABLE IF NOT EXISTS {table} (id INT AUTO_INCREMENT PRIMARY KEY, name_url_http VARCHAR(2048), url VARCHAR(2048), status VARCHAR(6), headers MEDIUMTEXT)")
        print(f"(OK!) Tabela '{table}'")
    except Exception as e:
        print(f"Erro: {e}")

    finally:
        connect().commit()
        mycursor.close()