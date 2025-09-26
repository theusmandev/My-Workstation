CREATE TABLE Product_1084_Sales_Analysis_III (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(50),
    unit_price INT
);

CREATE TABLE Sales_1084_Sales_Analysis_III (
    seller_id INT,
    product_id INT,
    buyer_id INT,
    sale_date DATE,
    quantity INT,
    price INT,
    FOREIGN KEY (product_id) REFERENCES Product_1084_Sales_Analysis_III(product_id)
);



-- Product data
INSERT INTO Product_1084_Sales_Analysis_III (product_id, product_name, unit_price) VALUES
(1, 'S8', 1000),
(2, 'G4', 800),
(3, 'iPhone', 1400);

-- Sales data
INSERT INTO Sales_1084_Sales_Analysis_III (seller_id, product_id, buyer_id, sale_date, quantity, price) VALUES
(1, 1, 1, '2019-01-21', 2, 2000),
(1, 2, 2, '2019-02-17', 1, 800),
(2, 2, 3, '2019-06-02', 1, 800),
(3, 3, 4, '2019-05-13', 2, 2800);



select * from Product_1084_Sales_Analysis_III
select * from Sales_1084_Sales_Analysis_III 




SELECT DISTINCT p.product_id, p.product_name
FROM Product_1084_Sales_Analysis_III p
JOIN Sales_1084_Sales_Analysis_III s
    ON p.product_id = s.product_id
WHERE p.product_id NOT IN (
    SELECT product_id
    FROM Sales_1084_Sales_Analysis_III
    WHERE sale_date NOT BETWEEN '2019-01-01' AND '2019-03-31'
)
AND p.product_id IN (
    SELECT product_id
    FROM Sales_1084_Sales_Analysis_III
    WHERE sale_date BETWEEN '2019-01-01' AND '2019-03-31'
);



SELECT p.product_id, p.product_name
FROM Product_1084_Sales_Analysis_III p
JOIN Sales_1084_Sales_Analysis_III s
    ON p.product_id = s.product_id
GROUP BY p.product_id, p.product_name
HAVING 
    MIN(s.sale_date) >= '2019-01-01'
    AND MAX(s.sale_date) <= '2019-03-31';
