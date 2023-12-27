from connect_db import connect

mydb = connect()

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE sites (name_url_http VARCHAR(2048), url VARCHAR(2048), status VARCHAR(6), headers MEDIUMTEXT)")