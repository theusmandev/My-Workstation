-- Sales table
CREATE TABLE Sales_1068_Product_Sales_Analysis_I (
    sale_id INT,
    product_id INT,
    year INT,
    quantity INT,
    price INT,
    PRIMARY KEY (sale_id, year)

);

-- Sample data
INSERT INTO Sales_1068_Product_Sales_Analysis_I (sale_id, product_id, year, quantity, price) VALUES
(1, 100, 2008, 10, 5000),
(2, 100, 2009, 12, 5000),
(7, 200, 2011, 15, 9000);


select * from Sales_1068_Product_Sales_Analysis_I


SELECT 
    s.product_id,
    s.year AS first_year,
    s.quantity,
    s.price
FROM Sales_1068_Product_Sales_Analysis_I s
JOIN (
    SELECT product_id, MIN(year) AS first_year
    FROM Sales_1068_Product_Sales_Analysis_I
    GROUP BY product_id
) AS first_sales
ON s.product_id = first_sales.product_id
AND s.year = first_sales.first_year;

