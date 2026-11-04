import os
import psycopg2
from dotenv import load_dotenv


load_dotenv()

conn = psycopg2.connect(
host=os.getenv("DB_HOST"),
port=os.getenv("DB_PORT"),
dbname=os.getenv("DB_NAME"),
user=os.getenv("DB_USER"),
password=os.getenv("DB_PASSWORD"))

cur = conn.cursor() #курсор для хождение по базе

cur.execute("SELECT version();") #выполнение запроса
 
print(cur.fetchone()) #кортеж из выборки 

cur.close() # закрыли курсор
conn.close() #закрыли соедениние с бд