-- 1. Количество игр по жанрам
SELECT genres.name, COUNT(*) AS games_count
FROM game_genres
JOIN genres ON genres.genre_id = game_genres.genre_id
GROUP BY genres.name
ORDER BY games_count DESC;

-- 2. Топ-10 самых дорогих игр
SELECT name, price_usd
FROM games
WHERE price_usd IS NOT NULL
ORDER BY price_usd DESC
LIMIT 10;

-- 3. Средняя цена по жанрам
SELECT genres.name,
       ROUND(AVG(games.price_usd), 2) AS avg_price,
       COUNT(*) AS games_count
FROM games
JOIN game_genres ON game_genres.appid = games.appid
JOIN genres ON genres.genre_id = game_genres.genre_id
WHERE games.price_usd IS NOT NULL
GROUP BY genres.name
ORDER BY avg_price DESC;

-- 4. Жанры, где больше 5 игр
SELECT genres.name, COUNT(1) AS games_count
FROM games
JOIN game_genres ON game_genres.appid = games.appid
JOIN genres ON genres.genre_id = game_genres.genre_id
GROUP BY genres.name
HAVING COUNT(1) > 5
ORDER BY games_count DESC;