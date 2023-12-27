from connect_db import connect

mycursor = connect().cursor()

mycursor.execute("CREATE DATABASE sites_ativos")