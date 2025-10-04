CREATE TABLE Stocks_1393_Capital_GainLoss (
    stock_name VARCHAR(50),
    operation VARCHAR(10) CHECK (operation IN ('Buy', 'Sell')),
    operation_day INT,
    price INT,
    CONSTRAINT PK_Stocks PRIMARY KEY (stock_name, operation_day)
);


INSERT INTO Stocks_1393_Capital_GainLoss (stock_name, operation, operation_day, price) VALUES
('Leetcode', 'Buy', 1, 1000),
('Corona Masks', 'Buy', 2, 10),
('Leetcode', 'Sell', 5, 9000),
('Handbags', 'Buy', 17, 30000),
('Corona Masks', 'Sell', 3, 1010),
('Corona Masks', 'Buy', 4, 1000),
('Corona Masks', 'Sell', 5, 500),
('Corona Masks', 'Buy', 6, 1000),
('Handbags', 'Sell', 29, 7000),
('Corona Masks', 'Sell', 10, 10000);



select * from Stocks_1393_Capital_GainLoss


SELECT 
    stock_name,
    SUM(CASE WHEN operation = 'Sell' THEN price ELSE 0 END) -
    SUM(CASE WHEN operation = 'Buy' THEN price ELSE 0 END) AS capital_gain_loss
FROM Stocks_1393_Capital_GainLoss
GROUP BY stock_name;
