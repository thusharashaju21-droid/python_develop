create database expense_db;
use expense_db;
create  table expenses(
            id int primary key auto_increment,
            title varchar(100) not null,
            amount decimal(10,2) not null,
            category enum("food","travel","shopping","bills","other")default "other"
            
);

desc expenses;

insert into expenses(title,amount,category)
values
('Lunch',200,'food'),
('Bus Ticket',50,'travel'),
('Dress',2500,'shopping'),
('Electricity bill',750,'bills'),
('Accessories',500,'other');

select * from expenses;

Select * from expenses
WHERE id = 2;

update expenses set title='Breakfast',amount=300 where id=1;

select * from expenses
where id =1;

