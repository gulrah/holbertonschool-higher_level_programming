-- List all genres in the database by their rating
SELECT tv_genres.name, SUM(rating)
FROM tv_genres
LEFT JOIN tv_shows_genres ON tv_genres.id = tv_shows_genres.genre_id
LEFT JOIN tv_shows_rate ON tv_shows_genres.show_id = tv_shows_rate.show_id
GROUP BY tv_genres.name
ORDER BY SUM(rating) DESC;
