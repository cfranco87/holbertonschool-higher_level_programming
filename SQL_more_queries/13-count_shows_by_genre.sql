--  lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT tv_shows_genres.genre_id AS "genre", COUNT(tv_shows.id) as "number of shows"
FROM tv_shows_genres
LEFT JOIN tv_show ON tv_shows_genres.show_id = tv_show.id 
GROUP BY tv_shows_genres.genre_id
ORDER BY tv_show_genres.genre_id DESC;
