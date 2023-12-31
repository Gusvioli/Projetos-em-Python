from dotenv import load_dotenv
import os
import mysql.connector

load_dotenv()

def connect():   
    host = os.getenv("HOST")
    user = os.getenv("USER")
    password = os.getenv("PASSWORD")

    if not all([host, user, password]):
        raise ValueError("Certifique-se de definir as variáveis de ambiente HOST, USER e PASSWORD no arquivo .env")

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password=password,
    )
    return mydb

