import psycopg2
import os
from dotenv import load_dotenv
from os.path import join, dirname

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

#Connection to DB
def db_connection():
    host = os.getenv('HOST')
    db = os.getenv('DB')
    user = os.getenv('USER')
    password = os.getenv('PASSWORD')
    return psycopg2.connect(
        host = f'{host}',
        database = f'{db}',
        user = f'{user}',
        password = f'{password}'
    )