import os
import requests
from dotenv import load_dotenv
import json
import time

load_dotenv()
api_key = os.getenv("STEAM_API_KEY")

print('Ключ загружен:', bool(api_key))

url = 'https://api.steampowered.com/IStoreService/GetAppList/v1/'
skoka = int(input('Сколько игр загружаем? - '))
filters = {
    "include_games": True,
    "include_dlc": False,
    "include_software": False,
    "include_videos": False,
    "include_hardware": False,
    "max_results": skoka
}

details_url = "https://store.steampowered.com/api/appdetails"





params = {"key": api_key,
          "input_json": json.dumps(filters)
          }
response = requests.get(url, params=params, timeout=30)

#print(response.status_code) статус запроса
data = response.json()
#print(data) #текст про всю игру
apps = data["response"]["apps"]
#for app in apps:
   # print('ИГРА: ',app['appid'],app['name'])


#print('Получено игр', len(apps))


records = []
for app in apps[:skoka]:
    app_id = app['appid']


    details_params = {
    "appids": app_id,
    "cc": "us",
    "l": "english"
    }

    details_response = requests.get(details_url, params=  details_params, timeout=30)
    details_response.raise_for_status()
    details_data = details_response.json()
#   print(detail_app)
    entry = details_data[str(app_id)]

    if entry["success"]:

        game = entry["data"]


        record = {
        "appid": app_id,
        "name": game["name"],
        "is_free": game.get("is_free"),
        "developers": game.get("developers", []),
        "genres": game.get("genres", []),
        "release_date": game.get("release_date", {}),
        "price_overview": game.get("price_overview")
    }

        records.append(record)
        print("Добавлено:", game["name"])
    else:
        print('Steam ne vernyl karty: ', app_id)

    time.sleep(0.1) #КОНЕЦ ЦИКЛА



    
with open("games.json", "w", encoding="utf-8") as file:
    json.dump(records, file, ensure_ascii=False, indent=2)
