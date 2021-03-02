--script that lists all Comedy shows in the database hbtn_0d_tvshows.
SELECT tv_genres.name AS genre;
FROM tv_show_genres;
ORDER BY tv_show_genres.tv_genres ASC;
