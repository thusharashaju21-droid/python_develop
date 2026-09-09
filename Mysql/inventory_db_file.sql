create database inventory_db;

use inventory_db;

create table inventory (
    item_id int auto_increment primary key,
    item_name varchar(100) not null,
    sku varchar(50) unique not null,
    category varchar(50) not null,
    quantity int default 0,
    reorder_level int default 10,
    unit_price decimal(10,2) default 0.00,
    storage_zone varchar(20) default 'Zone-A',
    status varchar(20) default 'In Stock',
    created_at timestamp default current_timestamp
);