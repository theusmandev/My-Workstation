-- Create Products table
CREATE TABLE Products_1327_List_the_Products_Ordered_in_a_Period1 (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    product_category VARCHAR(50)
);

-- Create Orders table
CREATE TABLE Orders_1327_List_the_Products_Ordered_in_a_Period1 (
    product_id INT,
    order_date DATE,
    unit INT,
    FOREIGN KEY (product_id) REFERENCES Products_1327_List_the_Products_Ordered_in_a_Period1(product_id)
);

-- Insert data into Products
INSERT INTO Products_1327_List_the_Products_Ordered_in_a_Period1 (product_id, product_name, product_category) VALUES
(1, 'Leetcode Solutions', 'Book'),
(2, 'Jewels of Stringology', 'Book'),
(3, 'HP', 'Laptop'),
(4, 'Lenovo', 'Laptop'),
(5, 'Leetcode Kit', 'T-shirt');

-- Insert data into Orders
INSERT INTO Orders_1327_List_the_Products_Ordered_in_a_Period1 (product_id, order_date, unit) VALUES
(1, '2020-02-05', 60),
(1, '2020-02-10', 70),
(2, '2020-01-18', 30),
(2, '2020-02-11', 80),
(3, '2020-02-17', 2),
(3, '2020-02-24', 3),
(4, '2020-03-01', 20),
(4, '2020-03-04', 30),
(4, '2020-03-04', 60),
(5, '2020-02-25', 50),
(5, '2020-02-27', 50),
(5, '2020-03-01', 50);


select * from Orders_1327_List_the_Products_Ordered_in_a_Period1
select * from Products_1327_List_the_Products_Ordered_in_a_Period1


SELECT 
    p.product_name,
    SUM(o.unit) AS unit
FROM Products_1327_List_the_Products_Ordered_in_a_Period1 p
JOIN Orders_1327_List_the_Products_Ordered_in_a_Period1 o
    ON o.product_id = p.product_id
WHERE 
    o.order_date >= '2020-02-01' 
    AND o.order_date < '2020-03-01'
GROUP BY 
    p.product_name
HAVING 
    SUM(o.unit) >= 100;
