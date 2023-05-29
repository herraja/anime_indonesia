-- Active: 1667427687682@@localhost@3306@django_anime

USE django_anime;

SHOW TABLES;

SELECT * FROM api_anime ORDER BY anime_title ASC;

SELECT * FROM api_anime ORDER BY LENGTH(anime_title) DESC;

DESCRIBE api_anime;