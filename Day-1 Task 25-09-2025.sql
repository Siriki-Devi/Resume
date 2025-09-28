create database employees_db;
USE employees_db;
CREATE TABLE HR(
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50) NOT NULL,
    emp_dept VARCHAR(10) NOT NULL,
    emp_salary DECIMAL(10,2) NOT NULL,
    emp_joiningdate DATE NOT NULL
);
insert into HR(emp_id,emp_name,emp_dept,emp_salary,emp_joiningdate)
values(1, 'Ravi Kumar', 'IT', 60000.00, '2023-05-10'),
(2, 'Priya Sharma', 'HR', 45000.00, '2022-08-20'),
(3, 'Arjun Reddy', 'Finance', 75000.00, '2021-11-15');

SELECT * FROM HR
WHERE emp_salary > 50000;

CREATE database chocolates;
use chocolates;
create table DairyMilk(
product_id int primary key,
product_name varchar(50) not null,
weight_grams decimal(10,2) not null,
product_price decimal(10) not null,
product_flavour varchar(20) not null
);
INSERT INTO DairyMilk (product_id, product_name, weight_grams, product_price, product_flavour)
VALUES
(1, 'Dairy Milk', 20.00, 60.00, 'Fruit & Nut'),
(2, 'Dairy Milk', 25.00, 70.00, 'Roast Almond'),
(3, 'Dairy Milk', 30.00, 80.00, 'Silk Oreo');

select* from DairyMilk;
select product_name,product_price,product_flavour from DairyMilk;
select* from DairyMilk
WHERE product_price>60;
select* from DairyMilk
WHERE product_flavour='Silk Oreo';

create database Bikes;
use Bikes;
CREATE TABLE RoyalEnfield(
    Bike_id INT PRIMARY KEY,
    Model_name VARCHAR(20) NOT NULL,
    Enginee_cc DECIMAL(10,2) NOT NULL,
    Bike_price DECIMAL(10,2) NOT NULL,
    Bike_color VARCHAR(10) NOT NULL,
    Bike_MileageKMPL DECIMAL(5,2) NOT NULL,
    Bike_Launchyear INT NOT NULL,
    Bike_ABS VARCHAR(20) NOT NULL,
    Bike_FuelType VARCHAR(20) NOT NULL
);

INSERT INTO RoyalEnfield
(Bike_id, Model_name, Enginee_cc, Bike_price, Bike_color, Bike_MileageKMPL, Bike_Launchyear, Bike_ABS, Bike_FuelType)
VALUES
(1, 'Classic 350', 349.00, 195000.00, 'Black', 35.00, 2021, 'Dual-Channel', 'Petrol'),
(2, 'Meteor 350', 349.00, 205000.00, 'Blue', 32.00, 2021, 'Single-Channel', 'Petrol'),
(3, 'Himalayan 411', 411.00, 223000.00, 'White', 30.00, 2022, 'Dual-Channel', 'Petrol');

SELECT * FROM RoyalEnfield;
SELECT Model_name, Bike_price, Bike_MileageKMPL FROM RoyalEnfield; 
SELECT * FROM RoyalEnfield
WHERE Bike_price>205000.00;
SELECT * FROM RoyalEnfield
WHERE Bike_Launchyear>2020;
SELECT * FROM RoyalEnfield
WHERE Bike_ABS='Single-Channel';













