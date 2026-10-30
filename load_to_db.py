import json
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

with open("games.json", "r", encoding="utf-8") as file:
    records = json.load(file)





for record in records:
    appid = record['appid']
    name = record['name']
    is_free = record['is_free']
    release_date = record['release_date'].get('date')

    if record['price_overview'] is None:
        price = None
    else:
        price = record['price_overview']['final'] / 100


    cur.execute(
    "INSERT INTO games (appid,name,is_free,release_date,price_usd) " 
    "VALUES (%s,%s,%s,%s,%s) "
    "ON CONFLICT (appid) DO NOTHING",
    (appid,name,is_free,release_date,price))


    for genre in record['genres']:
        genre_id = int(genre['id']) #приходит строкой оборачиваем сразу в число
        genre_name = genre['description'] 

        cur.execute("INSERT INTO genres (genre_id, name) "  
                    "VALUES (%s, %s) "
                    "ON CONFLICT (genre_id) DO NOTHING",
                     (genre_id,genre_name))
    


        cur.execute(
            "INSERT INTO game_genres (appid,genre_id) "
            "VALUES (%s, %s) "
            "ON CONFLICT (appid, genre_id) DO NOTHING",
            (appid,genre_id)
        )






conn.commit()

cur.close()
conn.close()

print("Загружено игр:", len(records))