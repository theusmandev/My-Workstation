-- Prices table
CREATE TABLE Prices_1251_Average_Selling_Price (
    product_id INT NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    price INT NOT NULL,
    CONSTRAINT PK_Prices PRIMARY KEY (product_id, start_date, end_date)
);

-- UnitsSold table
CREATE TABLE UnitsSold_1251_Average_Selling_Price (
    product_id INT NOT NULL,
    purchase_date DATE NOT NULL,
    units INT NOT NULL
);


-- Insert into Prices
INSERT INTO Prices_1251_Average_Selling_Price (product_id, start_date, end_date, price) VALUES
(1, '2019-02-17', '2019-02-28', 5),
(1, '2019-03-01', '2019-03-22', 20),
(2, '2019-02-01', '2019-02-20', 15),
(2, '2019-02-21', '2019-03-31', 30);

-- Insert into UnitsSold
INSERT INTO UnitsSold_1251_Average_Selling_Price (product_id, purchase_date, units) VALUES
(1, '2019-02-25', 100),
(1, '2019-03-01', 15),
(2, '2019-02-10', 200),
(2, '2019-03-22', 30);


select * from Prices_1251_Average_Selling_Price
select * from UnitsSold_1251_Average_Selling_Price 


SELECT 
    p.product_id,
    CAST(
      COALESCE(
        SUM(u.units * p.price) * 1.0 / NULLIF(SUM(u.units), 0)
      , 0)
    AS DECIMAL(10,2)) AS average_price
FROM Prices_1251_Average_Selling_Price p
LEFT JOIN UnitsSold_1251_Average_Selling_Price u
  ON p.product_id = u.product_id
 AND u.purchase_date BETWEEN p.start_date AND p.end_date
GROUP BY p.product_id
ORDER BY p.product_id;

