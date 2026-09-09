create database song_db;
use song_db;

create table song (
id int auto_increment primary key,
title varchar(200) not null,
track_number int not null,
movie varchar(200) not null,
singers varchar(200) not null
);

select * from song;