CREATE TABLE Customer_1321_Restaurant_Growth (
    customer_id INT NOT NULL,
    name VARCHAR(50) NOT NULL,
    visited_on DATE NOT NULL,
    amount INT NOT NULL,
    CONSTRAINT PK_Customer PRIMARY KEY (customer_id, visited_on)
);
INSERT INTO Customer_1321_Restaurant_Growth (customer_id, name, visited_on, amount) VALUES
(1, 'Jhon',    '2019-01-01', 100),
(2, 'Daniel',  '2019-01-02', 110),
(3, 'Jade',    '2019-01-03', 120),
(4, 'Khaled',  '2019-01-04', 130),
(5, 'Winston', '2019-01-05', 110),
(6, 'Elvis',   '2019-01-06', 140),
(7, 'Anna',    '2019-01-07', 150),
(8, 'Maria',   '2019-01-08', 80),
(9, 'Jaze',    '2019-01-09', 110),
(1, 'Jhon',    '2019-01-10', 130),
(3, 'Jade',    '2019-01-10', 150);


select * from Customer_1321_Restaurant_Growth


WITH daily_amount AS (
    SELECT 
        visited_on,
        SUM(amount) AS amount
    FROM Customer_1321_Restaurant_Growth
    GROUP BY visited_on
)
SELECT 
    visited_on,
    amount,
    CAST(
        SUM(amount) OVER (
            ORDER BY visited_on 
            ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
        ) / 7.0 AS DECIMAL(10,2)
    ) AS average_amount
FROM daily_amount
WHERE visited_on >= (
    SELECT DATEADD(DAY, 6, MIN(visited_on)) 
    FROM Customer_1321_Restaurant_Growth
)
ORDER BY visited_on;
