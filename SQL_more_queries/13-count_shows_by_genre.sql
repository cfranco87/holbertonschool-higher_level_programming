--  lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT tv_shows_genres.name AS "genre", COUNT(*) AS "number of shows"
FROM tv_shows_genres
LEFT JOIN tv_genres ON tv_shows_genres.genre_id = tv_genres.id 
GROUP BY genre
ORDER BY number_of_shows DESC;
