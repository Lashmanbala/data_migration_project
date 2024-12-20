--
-- Creating user and granting permissions
--

CREATE USER retail_user WITH ENCRYPTED PASSWORD 'retail123';

CREATE DATABASE retail_db;

GRANT ALL PRIVILEGES ON DATABASE retail_db TO retail_user;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO retail_user;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO retail_user;
GRANT USAGE, CREATE ON SCHEMA public TO retail_user;


-- Connect to the database
\c retail_db;

-- Creating tables

CREATE TABLE IF NOT EXISTS departments (
    department_id SERIAL PRIMARY KEY,
    department_name VARCHAR(45) NOT NULL
);

CREATE TABLE IF NOT EXISTS categories (
    category_id SERIAL PRIMARY KEY,
    category_department_id INT NOT NULL,
    category_name VARCHAR(45) NOT NULL
);

CREATE TABLE IF NOT EXISTS products (
    product_id SERIAL PRIMARY KEY,
    product_category_id INT NOT NULL,
    product_name VARCHAR(45) NOT NULL,
    product_description VARCHAR(255) NOT NULL,
    product_price REAL NOT NULL,
    product_image VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS customers (
    customer_id SERIAL PRIMARY KEY,
    customer_fname VARCHAR(45) NOT NULL,
    customer_lname VARCHAR(45) NOT NULL,
    customer_email VARCHAR(45) NOT NULL,
    customer_password VARCHAR(45) NOT NULL,
    customer_street VARCHAR(255) NOT NULL,
    customer_city VARCHAR(45) NOT NULL,
    customer_state VARCHAR(45) NOT NULL,
    customer_zipcode VARCHAR(45) NOT NULL
);

CREATE TABLE IF NOT EXISTS orders (
    order_id SERIAL PRIMARY KEY,
    order_date TIMESTAMP NOT NULL,
    order_customer_id INT NOT NULL,
    order_status VARCHAR(45) NOT NULL
);

CREATE TABLE IF NOT EXISTS order_items (
    order_item_id SERIAL PRIMARY KEY,
    order_item_order_id INT NOT NULL,
    order_item_product_id INT NOT NULL,
    order_item_quantity INT NOT NULL,
    order_item_subtotal REAL NOT NULL,
    order_item_product_price REAL NOT NULL
);