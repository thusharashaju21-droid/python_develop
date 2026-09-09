-- Food Database SQL
-- Database: food_db
-- Tables: user, food_log

CREATE DATABASE IF NOT EXISTS food_db;
USE food_db;

-- ============================================================
-- TABLE 1: user
-- ============================================================

CREATE TABLE user (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE
);

-- ============================================================
-- TABLE 2: food_log
-- ============================================================

CREATE TABLE food_log (
    id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(150) NOT NULL,
    meal_type VARCHAR(50) NOT NULL,
    calorie DECIMAL(8,2) NOT NULL,
    user_id INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES user(id)
);

-- ============================================================
-- INSERT 5 USERS
-- ============================================================

INSERT INTO user (name, email) VALUES
('Arun Kumar', 'arun@gmail.com'),
('Anjali Menon', 'anjali@gmail.com'),
('Rahul Nair', 'rahul@gmail.com'),
('Meera Thomas', 'meera@gmail.com'),
('Vishnu Raj', 'vishnu@gmail.com');

-- ============================================================
-- INSERT 10 FOOD LOGS
-- ============================================================

INSERT INTO food_log (title, meal_type, calorie, user_id) VALUES
('Idli with Sambar', 'Breakfast', 280, 1),
('Chicken Biriyani', 'Lunch', 650, 1),
('Banana', 'Snack', 105, 2),
('Chapati with Chicken Curry', 'Dinner', 520, 2),
('Dosa with Chutney', 'Breakfast', 350, 3),
('Rice with Fish Curry', 'Lunch', 580, 3),
('Vegetable Sandwich', 'Snack', 250, 4),
('Grilled Chicken Salad', 'Dinner', 420, 4),
('Appam with Egg Curry', 'Breakfast', 450, 5),
('Fried Rice', 'Dinner', 600, 5);

insert into food_log(title,meal_type,calorie,user_id) values("tea","breakfast",100,2);

-- ============================================================
-- SAMPLE QUERIES
-- ============================================================

select user.name,food_log.title,food_log.calorie from user left join food_log on user.id=food_log.user_id;

select user.name,food_log.title,food_log.calorie from user inner join food_log on user.id=food_log.user_id;

select user.name,food_log.title,food_log.calorie from user right join food_log on user.id=food_log.user_id;

select user.name,sum(food_log.calorie)from user left join food_log on user.id=food_log.user_id group by user.name;

select user.name,count(food_log.calorie)from user left join food_log on user.id=food_log.user_id group by user.name;

select user.name,sum(food_log.calorie)from user left join food_log on user.id=food_log.user_id where user.name='meera thomas';


