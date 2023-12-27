import mysql.connector

def connect():    
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1593572846",
        database="sites_ativos"
    )
    return mydb