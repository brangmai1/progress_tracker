DROP DATABASE IF EXISTS progress_tracker;

-- progress_tracker database
CREATE DATABASE progress_tracker;

USE progress_tracker;

-- DROP TABLE IF EXISTS genres;

-- genres table
CREATE TABLE genres (
	id INT PRIMARY KEY,
    genre_type VARCHAR(25) NOT NULL
);

ALTER TABLE genres AUTO_INCREMENT = 21;

-- DROP TABLE IF EXISTS movies;

-- movies table
CREATE TABLE movies (
	id INT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    rating FLOAT,
    release_year INT
);
ALTER TABLE movies AUTO_INCREMENT = 101;

-- DROP TABLE IF EXISTS movie_genre;

-- movie_genre table
CREATE TABLE movie_genre (
	genre_id INT NOT NULL,
    movie_id INT NOT NULL,
    PRIMARY KEY (genre_id, movie_id),
    CONSTRAINT fk_genre FOREIGN KEY (genre_id) REFERENCES genres(id) ON DELETE CASCADE,
    CONSTRAINT fk_movie FOREIGN KEY (movie_id) REFERENCES movies(id) ON DELETE CASCADE
);




