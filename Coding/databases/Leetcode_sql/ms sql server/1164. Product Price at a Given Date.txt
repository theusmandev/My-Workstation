-- Products table create karna
CREATE TABLE Products_1164_price_at_a_Given_Date (
    product_id INT,
    new_price INT,
    change_date DATE,
    PRIMARY KEY (product_id, change_date)
);

-- Sample data insert karna (jo example me diya gaya hai)
INSERT INTO Products_1164_price_at_a_Given_Date  (product_id, new_price, change_date) VALUES
(1, 20, '2019-08-14'),
(2, 50, '2019-08-14'),
(1, 30, '2019-08-15'),
(1, 35, '2019-08-16'),
(2, 65, '2019-08-17'),
(3, 20, '2019-08-18');


select * from Products_1164_price_at_a_Given_Date 


SELECT p.product_id, p.new_price AS price
FROM Products_1164_price_at_a_Given_Date p
JOIN (
  SELECT product_id, MAX(change_date) AS last_change
  FROM Products_1164_price_at_a_Given_Date
  WHERE change_date <= '2019-08-16'
  GROUP BY product_id
) t
ON p.product_id = t.product_id AND p.change_date = t.last_change

UNION

SELECT DISTINCT product_id, 10 AS price
FROM Products_1164_price_at_a_Given_Date
WHERE product_id NOT IN (
  SELECT product_id
  FROM Products_1164_price_at_a_Given_Date
  WHERE change_date <= '2019-08-16'
);
