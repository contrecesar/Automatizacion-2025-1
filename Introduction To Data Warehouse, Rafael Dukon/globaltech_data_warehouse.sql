/*
 * GLOBALTECH RETAIL - COMPLETE DATA WAREHOUSE SOLUTION
 * Single-file MySQL implementation
 * Author: [Tu Nombre]
 * Date: [Fecha]
 */

-- =============================================
-- SECTION 1: DATABASE SETUP
-- =============================================
DROP DATABASE IF EXISTS globaltech_dw;
CREATE DATABASE globaltech_dw;
USE globaltech_dw;

-- =============================================
-- SECTION 2: DIMENSION TABLES
-- =============================================
-- Products Dimension
CREATE TABLE dim_products (
    product_id INT PRIMARY KEY,
    sku VARCHAR(20) UNIQUE NOT NULL,
    product_name VARCHAR(100) NOT NULL,
    category VARCHAR(50) NOT NULL,
    current_price DECIMAL(10,2) CHECK (current_price > 0),
    cost DECIMAL(10,2) CHECK (cost > 0)
) ENGINE=InnoDB;

-- Dates Dimension (with pre-populated data example)
CREATE TABLE dim_dates (
    date_id INT PRIMARY KEY,
    full_date DATE NOT NULL,
    day INT NOT NULL,
    month INT NOT NULL,
    year INT NOT NULL
) ENGINE=InnoDB;

-- =============================================
-- SECTION 3: FACT TABLES
-- =============================================
CREATE TABLE fact_sales (
    sale_id BIGINT PRIMARY KEY AUTO_INCREMENT,
    product_id INT NOT NULL,
    date_id INT NOT NULL,
    quantity INT CHECK (quantity > 0),
    unit_price DECIMAL(10,2) CHECK (unit_price > 0),
    FOREIGN KEY (product_id) REFERENCES dim_products(product_id),
    FOREIGN KEY (date_id) REFERENCES dim_dates(date_id)
) ENGINE=InnoDB;

-- =============================================
-- SECTION 4: STORED PROCEDURES
-- =============================================
DELIMITER //
CREATE PROCEDURE load_sample_data()
BEGIN
    -- Insert sample products
    INSERT INTO dim_products VALUES
    (1, 'TV-001', '4K Smart TV', 'Televisions', 899.99, 600),
    (2, 'PH-001', 'Smartphone X', 'Phones', 699.99, 450);
    
    -- Insert sample dates
    INSERT INTO dim_dates VALUES
    (20240101, '2024-01-01', 1, 1, 2024),
    (20240102, '2024-01-02', 2, 1, 2024);
    
    -- Insert sample sales
    INSERT INTO fact_sales (product_id, date_id, quantity, unit_price) VALUES
    (1, 20240101, 2, 899.99),
    (2, 20240102, 3, 699.99);
END //
DELIMITER ;

-- =============================================
-- SECTION 5: EXAMPLE QUERIES
-- =============================================
-- Query 1: Total sales by product category
SELECT 
    p.category,
    SUM(fs.quantity * fs.unit_price) AS total_sales
FROM fact_sales fs
JOIN dim_products p ON fs.product_id = p.product_id
GROUP BY p.category;

-- =============================================
-- SECTION 6: EXECUTION INSTRUCTIONS
-- =============================================
-- 1. Execute entire script to create database
-- 2. Call procedures to load data:
--    CALL load_sample_data();
-- 3. Run analytical queries