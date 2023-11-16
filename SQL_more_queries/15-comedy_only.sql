--  lists all Comedy shows in the database
SELECT tv_shows.title
FROM tv_show
JOIN tv_show_genres ON tv_show.id = tv_show_genres.show_id
JOIN tv_genres ON tv_show_genres.genre_id = tv_genre.id
WHERE tv_genres.name = 'Comedy'
ORDER BY tv_shows.title;