-- script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
SELECT tv_genres.name AS genre;
FROM tv_show_genres;
ORDER BY tv_show_genres.tv_genres ASC;
