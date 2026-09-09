create database book_db;

use book_db;

create table book (
    id int auto_increment primary key,
    title varchar(100),
    author varchar(100),
    price int
);

select * from book;