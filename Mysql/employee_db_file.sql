-- MySQL Basic Query Practice Assessment
-- Questions Only
-- Topics: Database, USE, CREATE TABLE, DESC, INSERT, SELECT, WHERE, UPDATE

-- ============================================================
-- SECTION 1: DATABASE OPERATIONS
-- ============================================================

-- Q1. Create a database named employee_db.

create database employee_db;

-- Q2 switch to employee_db

use employee_db;

-- ============================================================
-- SECTION 2: CREATE TABLE
-- ============================================================

-- Q6. Inside employee_db, create a table named employee with:
--     id        -> integer, auto increment, primary key
--     name      -> varchar(100), cannot be NULL
--     age       -> integer, cannot be NULL
--     salary    -> float, cannot be NULL
--     department -> enum('hr','it','sales','finance') with default 'it'

create table employee(
id int auto_increment primary key,
name varchar(100) not NULL,
age int not null,
salary float not null,
department enum('hr','it','sales','finance') default "it"
);

-- ============================================================
-- SECTION 3: DESCRIBING TABLES
-- ============================================================

-- Q11. Write a query to display the structure of the employee table.

desc employee;
-- ============================================================
-- SECTION 4: INSERT RECORDS
-- ============================================================

-- Q16. Insert the following employee into the employee table:
--      name: Arun
--      age: 25
--      salary: 30000
--      department: it

insert into employee(name,age,salary,department) values ("tom",24,35000,"it");

-- Q17. Insert the following employee into the employee table:
--      name: Meera
--      age: 28
--      salary: 42000
--      department: hr

insert into employee(name,age,salary,department) values ("Meera",28,42000,"hr");

-- Q18. Insert the following employee into the employee table:
--      name: Rahul
--      age: 32
--      salary: 55000
--      department: finance

insert into employee(name,age,salary,department) values ("Ram",34,57000,"finance");

insert into employee(name,age,salary,department) values ("Meera",28,42000,"hr");


-- ============================================================
-- SECTION 5: SELECT RECORDS
-- ============================================================

-- Q26. Write a query to display all records from the employee table.

select  * from employee;

-- Q27. Write a query to display all employees name and salary

select name,salary from employee;

-- ============================================================
-- SECTION 6: FILTERING USING WHERE
-- ============================================================

-- Q31. Display the employee whose id is 2.

select * from employee where id =2;

-- Q32. Display the employee whose name is 'Arun'.

select * from employee where name = 'Arun';

-- Q33. Display all employees whose age is 30.

select * from employee where age=30;

-- Q34. Display all employees whose department is 'it'.


-- Q35. Display all employees whose salary is 50000.




-- ============================================================
-- SECTION 7: UPDATE RECORDS
-- ============================================================

-- Q47. Change the salary of the employee with id 1 to 35000.
update employee set salary =35000 where id =1;
-- Q48. Change the department of the employee with id 2 to 'sales'.
update employee set department ='sales' where id =2;
-- Q49. Change the age of the employee with id 3 to 35.
update employee set age =29 where id=5;

-- Q50. Change both salary and department of the employee with id 1:
--      salary = 40000
--      department = 'finance'
update employee set salary=40000,department='finance' where id =1;

-- query for deleting employee whose id =4

delete from employee where id=4;

-- select employee records where salary>35000 >,<,>=,<=

select * from employee where salary > 35000;

-- display employee whose salary in range of 30k to 45k
 select * from employee where salary >30000 and salary < 45000;
 
 -- operator <,>,<=,>=,!=,<>
 -- display employee records whose age not 30
 
 select * from employee where age <>30;
 
 -- multiple conditions evaluate and,or,not
 -- display employee records having salary >30k and department 'it'
 
 select * from employee where salary >30000 and department='it';
 
 -- display employee whose department either hr or it
 
 select * from employee where department= 'hr' or department='it';
 
 select * from employee where department in('it','hr'); -- many records dipslay use
 
 -- display employees whoses not working in it,hr
 
 select * from employee where department not in('it','hr');
 
 -- between
 -- select employee whosse salary in range of 30k -45k
 
 select * from employee where salary between 30000 and 45000;
 
 -- order by
 
 select * from employee order by salary;
 
 -- sorted
 
 select * from employee order by salary desc;
 
 -- limit ,offset
 
 
 select * from employee limit 1;
 select * from employee limit 2 offset 1; -- skip
  select * from employee limit 1 offset 2; -- last
  
  -- employee with highest age (no id)
  select * from employee order by age desc limit 1;
  
  -- employee with second highest age
  select * from employee order by age desc limit 1 offset 1;
  
  -- employee with highest salary 
  select * from employee order by salary desc limit 1;
  
  -- employee with second highest salary
  
  select * from employee order by salary desc limit 1 offset 1;
 
 -- aggrerate functions max,min,sum,count,avg
 
 select count(*) from employee;
 select sum(salary) from employee;
 select max(salary) from employee; 
 select min(salary) from employee;
 select avg(salary) from employee;
 
 -- subquery , nestedquery
-- write query to display highest salary employee

select * from employee where salary=(select max(salary) from employee);

-- employee with lowest salary

select * from employee where salary=(select min(salary) from employee); 

-- employee with highest age

select * from employee where age=(select max(age) from employee);

-- employee with lowest age

select * from employee where age=(select min(age) from employee); 

-- duplicate  remove

select distinct department from employee;

-- count number of employee in each department
select department,count(*) from employee group by department;

--  sum of salary employee in each department wise 
select department,sum(salary) from employee group by department;

-- table name change(total),descending order
select department,sum(salary) as total from employee group by department order by total desc;

-- department with most number of employees

select department,count(*)as count_dep from employee group by department order by count_dep desc limit 1;

-- display department with more than 1 employee

select department,count(*) as count_dep from employee group by department having count_dep>1;

-- 