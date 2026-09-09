-- course[id,title,fee,duration]
create database course_db;
use course_db;

create table course(
id int auto_increment primary key,
title varchar(200)unique not null,
fee decimal(8,2)not null,
duration varchar(200)not null
);

-- batch [id,title,head_count,course_id]
create table batch(
id int auto_increment primary key,
title varchar(200)unique not null,
head_count int not null,
course_id int not null
);

insert into course(id,title,fee,duration) values (1,"Mearn",70000,"6.5 month");
insert into course(id,title,fee,duration) values (2,"Python",65000,"6 Month");
insert into course(id,title,fee,duration)values (3,"Software Testing",55000,"5.5 month");
insert into course(id,title,fee,duration)values(4,"Data Science",75000,"6 month");

select * from course;

insert into batch(title,head_count,course_id) values ("py-dj-june",40,1);
insert into batch(title,head_count,course_id) values ("py-dj-aug",45,2);
insert into batch(title,head_count,course_id) values ("ds-july",47,4);

select * from batch;

update batch set title="Mearn-may" where id=1;

select course.title,course.fee,batch.title,batch.head_count from course left join batch on course.id=batch.course_id;
select course.title,course.fee,batch.title,batch.head_count from course inner join batch on course.id=batch.course_id;
select course.title,course.fee,batch.title,batch.head_count from course right join batch on course.id=batch.course_id;
