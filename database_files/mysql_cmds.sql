--
-- Creating user and granting permissions
--

CREATE USER IF NOT EXISTS 'retail_user' IDENTIFIED BY 'retail123';

GRANT ALL PRIVILEGES ON retail_db.* TO 'retail_user';

FLUSH PRIVILEGES;

CREATE DATABASE IF NOT EXISTS retail_db;

USE retail_db;

SET GLOBAL local_infile = 1;   -- to be able to load data into table from a file

--
-- Creating tables
--

CREATE TABLE IF NOT EXISTS departments (
  department_id INT NOT NULL,
  department_name VARCHAR(45) NOT NULL,
  PRIMARY KEY (department_id)
);


CREATE TABLE IF NOT EXISTS categories (
  category_id INT NOT NULL,
  category_department_id INT NOT NULL,
  category_name VARCHAR(45) NOT NULL,
  PRIMARY KEY (category_id)
); 


CREATE TABLE IF NOT EXISTS products (
  product_id INT NOT NULL,
  product_category_id INT NOT NULL,
  product_name VARCHAR(45) NOT NULL,
  product_description VARCHAR(255) NOT NULL,
  product_price FLOAT NOT NULL,
  product_image VARCHAR(255) NOT NULL,
  PRIMARY KEY (product_id)
);


CREATE TABLE IF NOT EXISTS customers (
  customer_id INT NOT NULL,
  customer_fname VARCHAR(45) NOT NULL,
  customer_lname VARCHAR(45) NOT NULL,
  customer_email VARCHAR(45) NOT NULL,
  customer_password VARCHAR(45) NOT NULL,
  customer_street VARCHAR(255) NOT NULL,
  customer_city VARCHAR(45) NOT NULL,
  customer_state VARCHAR(45) NOT NULL,
  customer_zipcode VARCHAR(45) NOT NULL,
  PRIMARY KEY (customer_id)
); 


CREATE TABLE IF NOT EXISTS orders (
  order_id INT NOT NULL,
  order_date TIMESTAMP NOT NULL,
  order_customer_id INT NOT NULL,
  order_status VARCHAR(45) NOT NULL,
  PRIMARY KEY (order_id)
);



CREATE TABLE IF NOT EXISTS order_items (
  order_item_id INT NOT NULL,
  order_item_order_id INT NOT NULL,
  order_item_product_id INT NOT NULL,
  order_item_quantity INT NOT NULL,
  order_item_subtotal FLOAT NOT NULL,
  order_item_product_price FLOAT NOT NULL,
  PRIMARY KEY (order_item_id)
);

--
-- Loading data into tables
--

LOAD DATA LOCAL INFILE '/migration_project/data/retail_db/categories/part-00000'
INTO TABLE categories
FIELDS TERMINATED BY ',' 
LINES TERMINATED BY '\n';

LOAD DATA LOCAL INFILE '/migration_project/data/retail_db/products/part-00000'
INTO TABLE products
FIELDS TERMINATED BY ',' 
LINES TERMINATED BY '\n';

LOAD DATA LOCAL INFILE '/migration_project/data/retail_db/customers/part-00000'
INTO TABLE customers
FIELDS TERMINATED BY ',' 
LINES TERMINATED BY '\n';

LOAD DATA LOCAL INFILE '/migration_project/data/retail_db/orders/part-00000'
INTO TABLE orders
FIELDS TERMINATED BY ',' 
LINES TERMINATED BY '\n';

LOAD DATA LOCAL INFILE '/migration_project/data/retail_db/order_items/part-00000'
INTO TABLE order_items
FIELDS TERMINATED BY ',' 
LINES TERMINATED BY '\n';