-- script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT tvg.name AS genre, COUNT(tvsg.show_id) AS number_of_shows
FROM tv_show_genres AS tvsg
JOIN tv_genres AS tvg ON tvsg.genre_id = tvg.id
GROUP BY tvg.id /* distinct groups to run aggregate on each time */
ORDER BY number_of_shows DESC;
