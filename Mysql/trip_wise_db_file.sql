create database tripwise_db;
use tripwise_db;

create table expense(
id int auto_increment primary key,
trip varchar(200) not null,
paid_by varchar(200) not null,
amount decimal(8,2) not null,
category varchar(200) not null
);
select * from expense;
