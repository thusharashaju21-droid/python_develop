-- ============================================================
-- MySQL Basic Query Practice Assessment
-- Topics: DATABASE, CREATE TABLE, DESC, INSERT, SELECT, WHERE, 
--         UPDATE, DELETE, OPERATORS, ORDER BY, LIMIT, AGGREGATES
-- Domain: Store Inventory Management
-- ============================================================


-- ============================================================
-- SECTION 1: DATABASE OPERATIONS
-- ============================================================

-- Q1. Create a database named store_db.

create database store_db;
-- Q2. Switch to store_db.

use store_db;
-- ============================================================
-- SECTION 2: CREATE TABLE
-- ============================================================

-- Q3. Inside store_db, create a table named product with the following columns:
--     id       -> integer, auto increment, primary key
--     name     -> varchar(150), cannot be NULL
--     stock    -> integer, cannot be NULL
--     price    -> decimal(8,2), can be NULL
--     category -> enum('electronics', 'clothing', 'books', 'groceries') with default 'electronics'

create table store(
id int auto_increment primary key,
name varchar(150) not NULL,
stock int not NULL,
price decimal(8,2) NULL,
category enum('electronics', 'clothing', 'books', 'groceries') default 'electronics'
);



-- ============================================================
-- SECTION 3: DESCRIBING TABLES
-- ============================================================

-- Q4. Write a query to display the structure of the product table.


desc store;

-- ============================================================
-- SECTION 4: INSERT RECORDS
-- ============================================================

-- Q5. Insert the following product into the product table:
--     name: 'Wireless Mouse'
--     stock: 50
--     price: 1200.00
--     category: 'electronics'
insert into store(name,stock,price,category) values ("Wireless Mouse",50,1200.00,"electronics");

-- Q6. Insert the following product into the product table:
--     name: 'Cotton T-Shirt'
--     stock: 120
--     price: 850.00
--     category: 'clothing'

insert into store(name,stock,price,category) values ("cotton T-shirt",120,850.00,"clothing");
-- Q7. Insert the following product into the product table:
--     name: 'SQL Guide Book'
--     stock: 30
--     price: 450.00
--     category: 'books'

insert into store(name,stock,price,category) values ("SQL Guide Book",30,450.00,"books");
-- Q8. Insert the following product into the product table:
--     name: 'Organic Milk'
--     stock: 15
--     price: 60.00
--     category: 'groceries'

insert into store(name,stock,price,category) values ("Organic Milk",15,60.00,"groceries");

-- ============================================================
-- SECTION 5: SELECT RECORDS
-- ============================================================

-- Q9. Display all records from the product table.

select * from store;
-- Q10. Display only the name and price of all products.

select name,price from store;
-- ============================================================
-- SECTION 6: FILTERING USING WHERE & COMPARISON OPERATORS
-- ============================================================

-- Q11. Display the product whose id is 3.
select * from store where id=3;

-- Q12. Display the product whose name is 'Cotton T-Shirt'.
select * from store where name='Cotton T-Shirt';

-- Q13. Display all products whose stock is greater than 40.
select * from store where stock >40;

-- Q14. Display all products with a price less than or equal to 500.00.

select *from store where price <=500.00;
-- Q15. Display all products whose stock is NOT equal to 30. (Try using both != and <>)
select * from store where stock !=30;
select * from store where stock <> 30;

-- ============================================================
-- SECTION 7: MULTIPLE CONDITIONS (AND, OR, NOT, IN, BETWEEN)
-- ============================================================

-- Q16. Display products having price > 500 AND category is 'electronics'.

select * from store where price >500 AND category='electronics';
-- Q17. Display products whose category is either 'books' OR 'groceries'.

select * from store where category ='books' OR category='groceries';
-- Q18. Display products whose category is IN ('clothing', 'electronics').

select * from store where category in('clothing','electronics');
-- Q19. Display products whose category is NOT IN ('electronics', 'groceries').

select * from store where category not in('electronics','groceries');

-- Q20. Display products whose price is in the range of 400.00 to 1500.00 using AND.

select * from store where price>=400.00 and price<=1500.00;
-- Q21. Display products whose price is in the range of 400.00 to 1500.00 using BETWEEN.

select * from store where price between 400.00 and 1500.00;


-- ============================================================
-- SECTION 8: UPDATE & DELETE RECORDS
-- ============================================================

-- Q22. Change the price of the product with id 1 to 1100.00.
update store set price=1100.00 where id =1;

-- Q23. Change the category of the product with id 4 to 'clothing'.

update store set category='clothing' where id =4;
-- Q24. Change both price and stock for product with id 2:
--      price = 799.00
--      stock = 100
update store set price=799.00,stock=100 where id =2;

-- Q25. Delete the product whose id is 4.

delete from store where id =4;


-- ============================================================
-- SECTION 9: ORDER BY, LIMIT, AND OFFSET
-- ============================================================

-- Q26. Display all products ordered by price in ascending order.

select * from store order by price ;
-- Q27. Display all products ordered by stock in descending order.
select * from store order by price desc; 
-- Q28. Display the product with the highest price.

select * from store order by price desc limit 1;
-- Q29. Display the product with the second highest price.

select * from store order by price desc limit 1 offset 1;
-- Q30. Display the product with the lowest stock.

select * from store order by stock limit 1;


-- ============================================================
-- SECTION 10: AGGREGATE FUNCTIONS
-- ============================================================

-- Q31. Count the total number of products in the table.
select count(*) from store;

-- Q32. Calculate the total sum of stock across all products.
select sum(stock) from store;

-- Q33. Find the maximum price among all products.

select max(stock) from store;
-- Q34. Find the minimum price among all products.

select min(stock) from store;
-- Q35. Calculate the average price of all products.
select avg(stock) from store;