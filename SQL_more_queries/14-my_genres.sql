-- lists all genres of the show Dexter.
SELECT tv_genres.name 
FROM tv_show
LEFT JOIN tv_genres ON tv_show.genre_id = tv_genres.id
WHERE tv_show.title = 'Dexter'
ORDER BY tv_show.name ASC;
