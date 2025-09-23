-- Product table
CREATE TABLE Product_1045_Customers_Who_Bought_All_Products (
    product_key INT PRIMARY KEY
);

-- Customer table
CREATE TABLE Customer_1045_Customers_Who_Bought_All_Products (
    customer_id INT NOT NULL,
    product_key INT,
    FOREIGN KEY (product_key) REFERENCES Product_1045_Customers_Who_Bought_All_Products(product_key)
);

-- Product data
INSERT INTO Product_1045_Customers_Who_Bought_All_Products (product_key) VALUES
(5),
(6);

-- Customer data
INSERT INTO Customer_1045_Customers_Who_Bought_All_Products (customer_id, product_key) VALUES
(1, 5),
(2, 6),
(3, 5),
(3, 6),
(1, 6);


select * from Product_1045_Customers_Who_Bought_All_Products
select * from Customer_1045_Customers_Who_Bought_All_Products

SELECT customer_id
FROM Customer_1045_Customers_Who_Bought_All_Products
GROUP BY customer_id
HAVING COUNT(DISTINCT product_key) = (SELECT COUNT(*) FROM Product_1045_Customers_Who_Bought_All_Products);
