create database SalesDB


CREATE TABLE AllSales (
    SaleID INT IDENTITY(1,1) PRIMARY KEY,
    ProductName VARCHAR(100),
    Amount DECIMAL(10,2),
    SaleDate DATE,
    LoadedAt DATETIME DEFAULT GETDATE() -- Ye khud bataega data kab load hua
);


select * from AllSales

SELECT COUNT(*) FROM AllSales