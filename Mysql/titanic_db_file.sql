-- ============================================================
-- TITANIC DATA - MYSQL BASIC QUERY CASE STUDY
-- ============================================================
--
-- Topics Covered:
-- Database
-- USE
-- CREATE TABLE
-- DESC
-- INSERT
-- SELECT
-- WHERE
-- Comparison Operators
-- AND / OR / NOT
-- IN / NOT IN
-- BETWEEN
-- ORDER BY
-- LIMIT / OFFSET
-- Aggregate Functions
-- Subqueries
-- GROUP BY
-- HAVING
--
-- ============================================================


-- ============================================================
-- SECTION 1: DATABASE OPERATIONS
-- ============================================================

-- Q1. Create a database named titanic_db.

create database titanic_db;
-- Q2. Switch to the titanic_db database.

use titanic_db;
-- ============================================================
-- SECTION 2: CREATE TABLE
-- ============================================================

-- Q3. Create a table named passengers with the following fields:
--
-- passenger_id  -> integer, auto increment, primary key
-- name          -> varchar(200), cannot be NULL
-- age           -> integer, cannot be NULL
-- gender        -> enum('male','female'), cannot be NULL
-- ticket_class  -> integer, cannot be NULL
-- fare          -> decimal(8,2), cannot be NULL
-- survived      -> integer, cannot be NULL
-- embarked      -> enum('S','C','Q')
--
-- S = Southampton
-- C = Cherbourg
-- Q = Queenstown

create table passenger(
passenger_id int auto_increment primary key,
name varchar(200) not null,
age int not null,
gender enum('male','female') not null,
ticket_class int not null,
fare decimal(8,2) not null,
survived int not null,
embarked enum('s','c','q')
);

-- ============================================================
-- SECTION 3: DESCRIBING TABLE
-- ============================================================

-- Q4. Display the structure of the passengers table.
desc passenger;

-- ============================================================
-- SECTION 4: INSERT RECORDS
-- ============================================================

-- Insert the following Titanic passenger records.
--
-- passenger_id is auto increment, so do not insert it manually.


-- Q5.
-- Name: John Smith
-- Age: 25
-- Gender: male
-- Ticket Class: 3
-- Fare: 7.25
-- Survived: 0
-- Embarked: S
insert into passenger(Name,Age,Gender,Ticket_Class,Fare,Survived,Embarked) values ('John Smith',25,'Male',3,7.25,0,'S');

-- Q6.
-- Name: Mary Johnson
-- Age: 28
-- Gender: female
-- Ticket Class: 1
-- Fare: 71.28
-- Survived: 1
-- Embarked: C

insert into passenger(Name,Age,Gender,Ticket_Class,Fare,Survived,Embarked) values ('Mary Johnson',28,'Female',1,71.28,0,'C');

-- Q7.
-- Name: William Brown
-- Age: 35
-- Gender: male
-- Ticket Class: 2
-- Fare: 26.00
-- Survived: 0
-- Embarked: S

insert into passenger(Name,Age,Gender,Ticket_Class,Fare,Survived,Embarked) values ('William Brown',35,'Male',2,26.00,0,'S');

-- Q8.
-- Name: Anna Davis
-- Age: 22
-- Gender: female
-- Ticket Class: 3
-- Fare: 8.05
-- Survived: 1
-- Embarked: S

insert into passenger(Name,Age,Gender,Ticket_Class,Fare,Survived,Embarked) values ('Anna Davis',22,'Female',3,8.05,1,'S');

-- Q9.
-- Name: Robert Wilson
-- Age: 40
-- Gender: male
-- Ticket Class: 1
-- Fare: 83.48
-- Survived: 1
-- Embarked: C

insert into passenger(Name,Age,Gender,Ticket_Class,Fare,Survived,Embarked) values ('Robert Wilson',40,'Male',1,83.48,1,'C');

-- Q10.
-- Name: Elizabeth Taylor
-- Age: 31
-- Gender: female
-- Ticket Class: 2
-- Fare: 26.50
-- Survived: 1
-- Embarked: Q
insert into passenger(Name,Age,Gender,Ticket_Class,Fare,Survived,Embarked) values ('Elizabeth Taylor',31,'Female',2,26.50,1,'Q');


-- Q11.
-- Name: Charles Anderson
-- Age: 19
-- Gender: male
-- Ticket Class: 3
-- Fare: 7.75
-- Survived: 0
-- Embarked: Q

insert into passenger(Name,Age,Gender,Ticket_Class,Fare,Survived,Embarked) values ('Charles Anderson',19,'Male',3,7.75,0,'Q');

-- Q12.
-- Name: Margaret Thomas
-- Age: 45
-- Gender: female
-- Ticket Class: 1
-- Fare: 120.00
-- Survived: 1
-- Embarked: S

insert into passenger(Name,Age,Gender,Ticket_Class,Fare,Survived,Embarked) values ('Margaret Thomas',45,'Female',1,120.00,1,'S');

-- Q13.
-- Name: George Jackson
-- Age: 52
-- Gender: male
-- Ticket Class: 2
-- Fare: 30.00
-- Survived: 0
-- Embarked: S
insert into passenger(Name,Age,Gender,Ticket_Class,Fare,Survived,Embarked) values ('George Jackson',52,'Male',2,30.00,0,'S');


-- Q14.
-- Name: Sophia White
-- Age: 18
-- Gender: female
-- Ticket Class: 3
-- Fare: 10.50
-- Survived: 1
-- Embarked: C

insert into passenger(Name,Age,Gender,Ticket_Class,Fare,Survived,Embarked) values ('Sophia White',18,'Female',3,10.50,1,'C');

-- Q15.
-- Name: Thomas Harris
-- Age: 29
-- Gender: male
-- Ticket Class: 3
-- Fare: 15.00
-- Survived: 0
-- Embarked: S
insert into passenger(Name,Age,Gender,Ticket_Class,Fare,Survived,Embarked) values('Thomas Harris',29,'Male',3,15.00,0,'S');


-- Q16.
-- Name: Emma Martin
-- Age: 36
-- Gender: female
-- Ticket Class: 2
-- Fare: 35.00
-- Survived: 1
-- Embarked: S
insert into passenger(Name,Age,Gender,Ticket_Class,Fare,Survived,Embarked) values ('Emma Martin',36,'Female',2,35.00,1,'S');
-- Q17.
-- Name: Daniel Thompson
-- Age: 41
-- Gender: male
-- Ticket Class: 1
-- Fare: 90.00
-- Survived: 1
-- Embarked: C

insert into passenger(Name,Age,Gender,Ticket_Class,Fare,Survived,Embarked) values ('Daniel Thompson',41,'male',1,90.00,1,'C');
-- Q18.
-- Name: Grace Garcia
-- Age: 27
-- Gender: female
-- Ticket Class: 3
-- Fare: 12.00
-- Survived: 0
-- Embarked: Q

insert into passenger(Name,Age,Gender,Ticket_Class,Fare,Survived,Embarked) values ('Grace Garcia',27,'female',3,12.00,0,'Q');
-- Q19.
-- Name: Henry Martinez
-- Age: 60
-- Gender: male
-- Ticket Class: 1
-- Fare: 100.00
-- Survived: 0
-- Embarked: S

insert into passenger(Name,Age,Gender,Ticket_Class,Fare,Survived,Embarked) values ('Henry Martinez',60,'Male',1,100.00,0,'S');
-- Q20.
-- Name: Olivia Robinson
-- Age: 24
-- Gender: female
-- Ticket Class: 2
-- Fare: 28.00
-- Survived: 1
-- Embarked: C
insert into passenger(Name,Age,Gender,Ticket_Class,Fare,Survived,Embarked) values ('Olivia Robinson',24,'Female',2,28.00,1,'C');

-- Q21.
-- Name: James Clark
-- Age: 33
-- Gender: male
-- Ticket Class: 3
-- Fare: 9.50
-- Survived: 0
-- Embarked: S

insert into passenger(Name,Age,Gender,Ticket_Class,Fare,Survived,Embarked) values ('James Clark',33,'Male',3,9.50,0,'S');
-- Q22.
-- Name: Emily Rodriguez
-- Age: 30
-- Gender: female
-- Ticket Class: 1
-- Fare: 75.00
-- Survived: 1
-- Embarked: S
insert into passenger(Name,Age,Gender,Ticket_Class,Fare,Survived,Embarked) values ('Emily Rodriguez', 30,'Female',1,75.00,1,'S');

-- Q23.
-- Name: Edward Lewis
-- Age: 47
-- Gender: male
-- Ticket Class: 2
-- Fare: 32.00
-- Survived: 0
-- Embarked: Q
insert into passenger(Name,Age,Gender,Ticket_Class,Fare,Survived,Embarked) values ('Edward Lewis',47,'Male',2,32.00,0,'Q');

-- Q24.
-- Name: Charlotte Lee
-- Age: 26
-- Gender: female
-- Ticket Class: 3
-- Fare: 11.25
-- Survived: 1
-- Embarked: C
insert into passenger(Name,Age,Gender,Ticket_Class,Fare,Survived,Embarked) values ('Charlotte Lee',26,'Female',3,11.25,1,'C');


-- ============================================================
-- SECTION 5: BASIC SELECT
-- ============================================================

-- Q25. Display all passenger records.

select * from passenger;
-- Q26. Display only passenger names.

select name from passenger;
-- Q27. Display passenger names and ages.

select name,age from passenger;
-- Q28. Display passenger names, gender and fare.

select name,age,gender,fare from passenger;
-- Q29. Display passenger names and ticket class.

select name,ticket_class from passenger;
-- ============================================================
-- SECTION 6: WHERE CLAUSE
-- ============================================================

-- Q30. Display the passenger whose passenger_id is 5.
select * from passenger where passenger_id =5;

-- Q31. Display the passenger named 'Mary Johnson'.

select * from passenger where name='Mary Johnson';
-- Q32. Display all passengers whose age is 30.

select * from passenger where age=30;
-- Q33. Display all passengers whose gender is 'female'.
select * from passenger where gender='Female';

-- Q34. Display all passengers whose gender is 'male'.
select * from passenger where gender ='Male';

-- Q35. Display all passengers who survived.
--
-- survived = 1 means survived
-- survived = 0 means did not survive
select * from passenger where survived = 1;

-- Q36. Display all passengers who did not survive.

select * from passenger where survived = 0;
-- Q37. Display all passengers travelling in ticket class 1.
select * from passenger where ticket_class = 1;

-- Q38. Display all passengers travelling in ticket class 3.

select * from passenger where ticket_class = 3;
-- ============================================================
-- SECTION 7: COMPARISON OPERATORS
-- ============================================================

-- Q39. Display passengers whose age is greater than 40.
select * from passenger where age>40;

-- Q40. Display passengers whose age is less than 25.

select * from passenger where age<25;
-- Q41. Display passengers whose age is greater than or equal to 30.
select * from passenger where age >=30;

-- Q42. Display passengers whose age is less than or equal to 30.

select * from passenger where age <=30;
-- Q43. Display passengers whose fare is greater than 50.

select * from passenger where fare>50;
-- Q44. Display passengers whose fare is less than 20.

select * from passenger where fare <=20;
-- Q45. Display passengers whose fare is not equal to 10.50.

select * from passenger where fare<>10.50;
-- Q46. Display passengers whose age is not 30.
select * from passenger where age <>30;

-- ============================================================
-- SECTION 8: AND OPERATOR
-- ============================================================

-- Q47. Display female passengers who survived.

select * from passenger where gender='Female' and survived=1;
-- Q48. Display male passengers who survived.

select * from passenger where gender='Male' and survived=1;
-- Q49. Display passengers older than 30 and survived.

select * from passenger where age>30 and survived=1;
-- Q50. Display passengers younger than 30 and survived.

select * from passenger where age<30 and survived=1;
-- Q51. Display passengers travelling in class 1 and
--      whose fare is greater than 50.

select * from passenger where ticket_class=1 and fare>50;
-- Q52. Display female passengers travelling in class 1.

select * from passenger where gender='Female' and ticket_class=1;
-- Q53. Display male passengers travelling in class 3
--      and whose age is greater than 30.

select * from passenger where gender='Male'and ticket_class=3 and age >30; 
-- ============================================================
-- SECTION 9: OR OPERATOR
-- ============================================================

-- Q54. Display passengers who are either male or female.
--      (Practice OR operator)
select * from passenger where gender='Male' or gender='Female';

-- Q55. Display passengers travelling in class 1 or class 2.
select * from passenger where ticket_class =1 or ticket_class=2;


-- Q56. Display passengers who embarked from S or C.

select * from passenger where embarked='S' or embarked='C';
-- Q57. Display passengers whose age is below 20 or above 50.
select * from passenger where age<20 or age>50;

-- ============================================================
-- SECTION 10: IN OPERATOR
-- ============================================================

-- Q58. Display passengers travelling in class 1 or class 2
--      using IN.
select * from passenger where ticket_class in(1,2);

-- Q59. Display passengers who embarked from S or C
--      using IN.
select * from passenger where embarked in('s','c');

-- Q60. Display passengers whose age is 25, 30 or 40
--      using IN.

select *from passenger where age in(25,30,40);
-- Q61. Display passengers whose ticket class is not 1 or 3
--      using NOT IN.

select * from passenger where ticket_class not in(1,3);
-- ============================================================
-- SECTION 11: BETWEEN OPERATOR
-- ============================================================

-- Q62. Display passengers whose age is between 20 and 30.

select * from passenger where age between 20 and 20;
-- Q63. Display passengers whose age is between 30 and 50.
select * from passenger where age between 30 and 50;

-- Q64. Display passengers whose fare is between 20 and 50.

select * from passenger where fare between 20 and 50;
-- Q65. Display passengers whose fare is between 50 and 100.

select * from passenger where fare between 50 and 100;
-- Q66. Display passengers whose age is between 20 and 30
--      and who survived.

select * from passenger where age between 20 and 30;
-- ============================================================
-- SECTION 12: ORDER BY
-- ============================================================

-- Q67. Display all passengers ordered by age
--      from lowest to highest.
select * from passengers order by age ;

-- Q68. Display all passengers ordered by age
--      from highest to lowest.
select * from passengers order by age desc ;


-- Q69. Display all passengers ordered by fare
--      from lowest to highest.
select * from passengers order by fare ;

-- Q70. Display all passengers ordered by fare
--      from highest to lowest.
select * from passengers order by fare desc ;

-- Q71. Display all passengers ordered by name alphabetically.
select * from passengers order by name;

-- Q72. Display all passengers ordered by name
--      in reverse alphabetical order.
select * from passengers order by name desc;

-- ============================================================
-- SECTION 13: LIMIT AND OFFSET
-- ============================================================

-- Q73. Display the passenger with the highest fare.
 select * from passengers order by fare desc limit 1;

-- Q74. Display the passenger with the lowest fare.

 select * from passengers order by fare  limit 1;
-- Q75. Display the oldest passenger.

 select * from passengers order by age desc limit 1;
-- Q76. Display the youngest passenger.

 select * from passengers order by age  limit 1;
-- Q77. Display the passenger with the second highest fare.

 select * from passengers order by fare desc limit 1 offset 1;
-- Q78. Display the passenger with the second lowest fare.

 select * from passengers order by fare  limit 1 offset 1;

-- Q79. Display the three passengers with the highest fare.

 select * from passengers order by fare desc limit 3;
 
-- Q80. Display the three oldest passengers.

 select * from passengers order by age desc limit 3;

-- ============================================================
-- SECTION 14: AGGREGATE FUNCTIONS
-- ============================================================

-- Q81. Find the total number of passengers.
select count(*) from passenger;

-- Q82. Find the total number of passengers who survived.
select count(*) from passenger where survived=1;

-- Q83. Find the total number of passengers who did not survive.

select count(*) from passenger where survived=0;
-- Q84. Find the total fare collected from all passengers.
select sum(fare) from passenger;

-- Q85. Find the highest fare.

select max(fare) from passenger;
-- Q86. Find the lowest fare.

select  min(fare) from passenger;
-- Q87. Find the average fare.

select avg(fare) from passenger;
-- Q88. Find the highest age.

select max(age) from passenger;
-- Q89. Find the lowest age.

select min(age) from passenger;
-- Q90. Find the average age of all passengers.

select avg(age) from passenger;
-- ============================================================
-- SECTION 15: AGGREGATE + WHERE
-- ============================================================

-- Q91. Count the number of female passengers.
select count(*) from passenger where gender='Female';

-- Q92. Count the number of male passengers.
select count(*) from passenger where gender ='Male';

-- Q93. Count the number of passengers who survived.
select count(*)from passenger where survived=1;

-- Q94. Count the number of passengers who did not survive.

select count(*) from passenger where survived=0;
-- Q95. Find the average age of female passengers.

select avg(age) from passenger where gender='Female';
-- Q96. Find the average age of male passengers.

select avg(age) from passenger where gender='Male';
-- Q97. Find the average fare of passengers
--      travelling in class 1.

select avg(fare) from passenger where ticket_class =1;
-- Q98. Find the highest fare paid by a female passenger.

select max(fare) from passenger where gender='female';
-- Q99. Find the lowest fare paid by a male passenger.
select min(fare) from passenger where gender='male';

-- ============================================================
-- SECTION 16: SUBQUERIES
-- ============================================================

-- Q100. Display the passenger who paid the highest fare.
select * from passenger where fare=(select max(fare)from passenger);

-- Q101. Display the passenger who paid the lowest fare.

select * from passenger where fare=(select min(fare) from passenger);
-- Q102. Display the oldest passenger.

select * from passenger where age=(select max(age) from passenger);
-- Q103. Display the youngest passenger.

select * from passenger where age=(select min(age) from passenger);
-- Q104. Display all passengers whose fare is equal to
--       the average fare.

select * from passenger where fare=(select avg(fare) from passenger);
-- Q105. Display all passengers whose age is greater than
--       the average age.
select * from passenger where age>(select avg(age) from passenger);

-- Q106. Display all passengers whose age is less than
--       the average age.

select * from passenger where age<(select avg(age) from passenger);
-- Q107. Display all passengers whose fare is greater than
--       the average fare.

select * from passenger where fare>(select avg(fare) from passenger);
-- Q108. Display the passenger(s) who paid the highest fare
--       among passengers who survived.
select * from passenger where survived=1 and fare=(select max(fare) from passenger where survived=1);

-- Q109. Display the passenger(s) who paid the lowest fare
--       among passengers who survived.
select * from passenger where survived=1 and fare =(select min(fare) from passenger);

-- ============================================================
-- SECTION 17: GROUP BY
-- ============================================================

-- Q110. Display the number of passengers in each gender.
select gender,count(*) from passenger group by gender;

-- Q111. Display the number of passengers in each ticket class.

select ticket_class,count(*) from passenger group by ticket_class;
-- Q112. Display the number of passengers from each
--       embarkation point.

select embarked,count(*) from passenger group by embarked;
-- Q113. Display the number of survivors and non-survivors.

select survived,count(*) from passenger group by survived;
-- Q114. Display the average age for each gender.
select gender,avg(age) from passenger group by gender;

-- Q115. Display the average fare for each gender.
select gender,avg(fare) from passenger group by gender;

-- Q116. Display the total fare collected from each
--       ticket class.
select ticket_class,sum(fare) from passenger group by ticket_class;

-- Q117. Display the average fare for each ticket class.
select ticket_class,avg(fare) from passenger group by ticket_class;

-- Q118. Display the highest fare in each ticket class.
select ticket_class,max(fare) from passenger group by ticket_class;

-- Q119. Display the lowest fare in each ticket class.
select ticket_class,min(fare) from passenger group by ticket_class;

-- Q120. Display the number of survivors in each gender.

-- Hint:
-- Use GROUP BY and WHERE.
select gender,count(*) from passenger where survived=1 group by gender;


-- ============================================================
-- SECTION 18: GROUP BY + ORDER BY
-- ============================================================

-- Q121. Display each ticket class and the number of
--       passengers in that class, ordered by passenger
--       count from highest to lowest.
select ticket_class,count(*) as total from passengers group by ticket_class order by count(*) desc;

-- Q122. Display each gender and the number of passengers,
--       ordered by count from highest to lowest.

select gender,count(*) as total from passengers group by gender order by count(*) desc;
-- Q123. Display each embarkation point and the total fare
--       collected, ordered by total fare from highest
--       to lowest.
select embarked,sum(fare) as total from passengers group by embarked order by total desc;

-- Q124. Display each ticket class and its average fare,
--       ordered by average fare from highest to lowest.
select ticket_class,avg(fare) as avg_fare from passengers group by ticket_class order by avg_fare desc;

-- Q125. Display each gender and its average age,
--       ordered by average age from highest to lowest.
select gender ,avg(age) as avg_age from passengers group by gender order by avg_age desc;

-- ============================================================
-- SECTION 19: HAVING
-- ============================================================

-- Q126. Display ticket classes having more than 5 passengers.
select ticket_class,count(*) as count from passengers group by ticket_class having count>5;

-- Q127. Display genders having more than 5 passengers.
select gender,count(*) as count from passengers group by gender having count>5;

-- Q128. Display embarkation points having more than 5 passengers.
select embarked,count(*) as count from passengers group by embarked having count>5;

-- Q129. Display ticket classes whose average fare is
--       greater than 30.
select ticket_class ,avg(fare) as avg_fare from passengers group by ticket_class having avg_fare>30;

-- Q130. Display genders whose average age is greater than 30.
select gender,avg(age) as avg_age from passengers group by gender having avg_age>30;

-- Q131. Display ticket classes where the total fare is
--       greater than 100.
select ticket_class,sum(fare) as total_fare from passengers group by ticket_class having total_fare>100;

-- Q132. Display embarkation points where the total fare
--       collected is greater than 100.
select embarked,sum(fare) as total_fare from passengers group by embarked having total_fare>100;

-- ============================================================
-- SECTION 20: REAL-WORLD BUSINESS QUESTIONS
-- ============================================================

-- Q133. How many passengers travelled in first class?
select count(*) from passengers where ticket_class=1;

-- Q134. How many passengers travelled in third class?
select count(*) from passengers where ticket_class=3;

-- Q135. How many female passengers survived?
select count(*) from passengers where gender="female" and survived=1;

-- Q136. How many male passengers did not survive?
select count(*) from passengers where gender="male" and survived=0;


-- Q137. What is the average fare paid by survivors?
select avg(fare) from passengers where survived=1;

-- Q138. What is the average fare paid by passengers
--       who did not survive?
select avg(fare) from passengers where survived=0;

-- Q139. Find the highest fare paid by a passenger
--       who survived.
select max(fare) from passengers where survived=1;

-- Q140. Find the oldest female passenger.
select * from passengers where gender="female" order by age desc limit 1;

-- Q141. Find the oldest male passenger.
select * from passengers where gender="male" order by age desc limit 1;

-- Q142. Find the youngest passenger who survived.
select * from passengers where survived=1 order by age limit 1;

-- Q143. Find the highest-paid female passenger.
select * from passengers where gender="female" order by fare desc limit 1;

-- Q144. Find the highest-paid male passenger.
select * from passengers where gender="male" order by fare desc limit 1;

-- Q145. Display passengers who are female, survived,
--       and paid a fare greater than 30.
select * from passengers where gender="female"and survived=1 and fare>30;

-- Q146. Display passengers who are male, did not survive,
--       and are older than 30.
select * from passengers where gender="male"and survived=0 and age>30;

-- Q147. Display passengers travelling in class 1 or class 2
--       who survived.
select * from passengers where ticket_class in (1,2) and survived=1;

-- Q148. Display passengers travelling in class 3 whose
--       fare is below 20.
select * from passengers where ticket_class =3 and fare<20;

-- Q149. Display passengers whose age is between 20 and 40
--       and whose fare is greater than 25.
select * from passengers where age between 20 and 40 and fare>25;

-- Q150. Find the ticket class having the highest
--       number of passengers.
select ticket_class,count(*) as count from passengers group by ticket_class order by count desc limit 1;

-- ============================================================
-- END OF TITANIC MYSQL CASE STUDY
-- ============================================================