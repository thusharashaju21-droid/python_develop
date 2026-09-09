create database todo_db;
use todo_db;

create table user(
id int auto_increment primary key,
name varchar(200) not null,
email varchar(100) unique not null
);

desc user;

create table todo(
id int auto_increment primary key,
title varchar(200) not null,
status int not null,
user_id int not null
);
 
desc todo;

insert into user(name,email) values('arun','arun@gmail.com');
insert into user(name,email) values('meera','meera@gmail.com');
insert into user(name,email) values('rahul','rahul@gmail.com');

select * from user;

insert into todo(title,status,user_id)values('study mysql',1,1);
insert into todo(title,status,user_id)values('complete assignment',0,2);
insert into todo(title,status,user_id)values('practice python',1,1);
insert into todo(title,status,user_id)values('learn joins',0,3);

select * from todo;

select user.name, todo.title, todo.status from user right join todo on user.id = todo.user_id;