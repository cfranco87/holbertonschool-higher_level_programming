-- database dump from hbtn_0d_tvshows to your MySQL server
USE hbtn_0d_tvshows;
SELECT tv_shows.titles, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_shows_genres ON tv_shows.id = tv_show_genres.genre_id;
WHERE tv_show_genres.genre_id IS NOT NULL
ORDER BY tv_shows.title, tv_show_genres.genre_id;
