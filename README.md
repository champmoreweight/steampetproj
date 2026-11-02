

Сбор данных об играх Steam, загрузка в PostgreSQL и SQL-аналитика.

## Что делает проект
1. `main.py` собирает данные об играх из Steam API.
2. `load_to_db.py` загружает их в PostgreSQL.
3. `zaprosi.sql` содержит аналитические запросы.

## Стек
Python, PostgreSQL, SQL 

## Запуск
1. `pip install -r requirements.txt`
2. Создай базу и выполни `tablica.sql`
3. Скопируй `.env.example` в `.env` и впиши свои данные
4. `python main.py`, затем `python load_to_db.py`

## Структура
steamgameproj/
├── main.py                # сбор данных из Steam API
├── load_to_db.py          # загрузка данных в PostgreSQL
├── tablica.sql             # CREATE TABLE для games, genres, game_genres
├── zaprosi.sql            # аналитические запросы с комментариями
├── requirements.txt       # зависимости (pip freeze)
├── README.md              # описание и инструкция запуска
├── .gitignore
├── .env.example           # шаблон настроек без паролей
├── .env                   # твои реальные настройки (НЕ в git)
├── data/                  # сырые данные (JSON/CSV), в .gitignore, если большие
├── logs/                  # логи запусков (в .gitignore)
└── screenshots/           # картинки результатов для README

## Примеры запросов и результатов
[Кол-во игр по жанрам](screenshots/kolvo.png)
