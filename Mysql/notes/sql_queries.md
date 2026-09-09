

--creating new database
   mysql>create database database_name;

eg:

  mysql>create database movie_db;

--mysql query for listing database

  mysql>show databases;

-- query switch into d database

  mysql>use database_name;

  eg:

    mysql>use movie_db;

--creating table

 mysql>create table table_name(
    column_name data_type constraint,
    column_name data_type constraint)

--descrisble tablename
 mysql>desc table_name;

  eg:

   desc movie;
--lisiting all tables

  mysql> select* from table_name; 

   eg:

   select * from movie;

   --filtering records

    --selection record with id =2 
    mysql> select * from table _name where conditon 

    eg:
     mysql> select * from movie where id=1;


--updating records

mysql>update table_name set coil 1 value ,colun2,column 3=