-- Lists all shows in hbtn_0d_tvshows and their associated genres.

SELECT tv_shows.title, GROUP_CONCAT(tv_genres.name ORDER BY tv_genres.name ASC SEPARATOR ', ') AS genres
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
GROUP BY tv_shows.title;
