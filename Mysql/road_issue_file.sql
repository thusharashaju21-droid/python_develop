create database road_issue_db;

use road_issue_db;

create table issues (
    id int primary key auto_increment,
    title varchar(100),
    location varchar(100),
    posted_by varchar(100),
    status enum('unsolved', 'solved')
);