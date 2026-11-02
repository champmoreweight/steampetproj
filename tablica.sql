CREATE TABLE IF NOT EXISTS public.game_genres
(
    appid integer NOT NULL,
    genre_id integer NOT NULL,
    CONSTRAINT game_genres_pkey PRIMARY KEY (appid, genre_id),
    CONSTRAINT game_genres_appid_fkey FOREIGN KEY (appid)
        REFERENCES public.games (appid) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT game_genres_genre_id_fkey FOREIGN KEY (genre_id)
        REFERENCES public.genres (genre_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
);


CREATE TABLE IF NOT EXISTS public.games
(
    appid integer NOT NULL,
    name text COLLATE pg_catalog."default" NOT NULL,
    is_free boolean,
    release_date text COLLATE pg_catalog."default",
    price_usd numeric(10,2),
    CONSTRAINT games_pkey PRIMARY KEY (appid)
);

CREATE TABLE IF NOT EXISTS public.genres
(
    genre_id integer NOT NULL,
    name text COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT genres_pkey PRIMARY KEY (genre_id),
    CONSTRAINT genres_name_key UNIQUE (name)
);