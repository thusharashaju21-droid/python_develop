CREATE DATABASE movie_db;

SHOW DATABASES;

USE movie_db;

CREATE TABLE movies (
    id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(200) NOT NULL,
    year VARCHAR(20) NOT NULL,
    run_time INT,
    rating DECIMAL(2,1) NOT NULL,
    genre ENUM("action","comdey","thriller","drama","horror") DEFAULT "action"
);

DESC movies;

INSERT INTO movies(title, year, run_time, rating, genre)
VALUES
('ABCD', '2002', 120, 8.0, 'action'),
('Malayali Singh', '2004', 124, 8.0, 'comdey'),
('Drishyam', '2013', 150, 8.5, 'thriller'),
('Premam', '2015', 156, 9.0, 'drama'),
('The Conjuring', '2013', 112, 7.5, 'horror');

select * FROM movies;

#SELECT * FROM movies
#WHERE id = 2;

update movies set title ="mallu singh",run_time=150 where id=2;

select * from movies where id=2;