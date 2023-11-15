-- database dump from hbtn_0d_tvshows to your MySQL server
USE hbtn_0d_tvshows;

SELECT tv_shows.titles, tv_show_genres.genre_id
FROM 
RIGHT JOIN cities ON cities.state_id = states.id;