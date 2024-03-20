-- List all shows from hbtn_0d_tvshows_rate by their rating
SELECT tv_shows.title, SUM(rating)
FROM tv_shows
LEFT JOIN tv_shows_rate ON tv_shows.id = tv_shows_rate.show_id
GROUP BY tv_shows.title
ORDER BY SUM(rating) DESC;
