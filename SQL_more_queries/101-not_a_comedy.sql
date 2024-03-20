-- List all shows without the genre Comedy
SELECT tv_shows.title
FROM tv_shows
LEFT JOIN tv_shows_genres ON tv_shows.id = tv_shows_genres.show_id
LEFT JOIN tv_genres ON tv_shows_genres.genre_id = tv_genres.id
WHERE tv_genres.name != 'Comedy' OR tv_genres.name IS NULL
GROUP BY tv_shows.title
ORDER BY tv_shows.title ASC;
