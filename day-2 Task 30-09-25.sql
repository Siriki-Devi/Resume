CREATE DATABASE products;
USE products;

CREATE TABLE Products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(50) NOT NULL,
    category VARCHAR(30) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    rating DECIMAL(3,1) NOT NULL,   
    stock INT NOT NULL,
    brand VARCHAR(30) NOT NULL,
    sold_quantity INT NOT NULL
);

INSERT INTO Products (product_id, product_name, category, price, rating, stock, brand, sold_quantity) VALUES
(1, 'Echo Dot', 'Electronics', 3499, 4.6, 120, 'Amazon', 500),
(2, 'Kindle Paperwhite', 'Electronics', 9999, 4.8, 80, 'Amazon', 300),
(3, 'Fire TV Stick', 'Electronics', 3999, 4.5, 50, 'Amazon', 450),
(4, 'Instant Pot Duo', 'Kitchen', 7999, 4.7, 30, 'InstantPot', 200),
(5, 'Air Fryer', 'Kitchen', 5999, 4.6, 40, 'Philips', 150),
(6, 'Samsung Galaxy S23', 'Mobiles', 69999, 4.8, 25, 'Samsung', 100),
(7, 'OnePlus 11', 'Mobiles', 49999, 4.7, 20, 'OnePlus', 90),
(8, 'Bose Headphones', 'Electronics', 19999, 4.5, 15, 'Bose', 80),
(9, 'Logitech Mouse', 'Electronics', 1299, 4.4, 200, 'Logitech', 600),
(10, 'Amazon Basics Bag', 'Accessories', 999, 4.3, 300, 'Amazon', 400);



select category,sum(sold_quantity) as totalsoldquantity
from products
group by category;

select brand,avg(price) as priceofeachbrand
from products
group by brand;

select category,count(product_name) as productineachcategory
from products
group by category;

select category,max(rating) as ratingineachcategory
from products
group by category;

select brand,min(price) as minpriceineachbrand
from products
group by brand;

select category, SUM(sold_quantity) AS totalsold
from products
group by category
having sum(sold_quantity) > 1000;

select brand,avg(price) as avgpriceofproducts
from products
group by brand
having avg(price)>10000;

select category,max(rating) as maxratingofproduct
from products
group by category
having max(rating)>4.7;

select brand,count(product_name) as countofproducts
from products
group by brand
having count(product_name)>2;

select category,sum(stock) as sumofstock
from products
group by category
having sum(stock)<200;

select* from products
order by price asc;

select* from products
order by sold_quantity desc;

select* from products
order by rating desc,price asc;

select* from products
order by category asc,sold_quantity desc;

select* from products
order by brand asc;

select* from products
limit 5;

select* from products
order by price desc
limit 3;

select* from products
order by rating desc
limit 5;

select* from products
limit 2 offset 5;

select* from products
order by sold_quantity desc
limit 10;

select* from products
order by price asc;

select* from products
order by rating desc;

select* from products
order by sold_quantity desc,price asc;

select* from products
order by category asc,sold_quantity desc;

select* from products
order by brand desc;















