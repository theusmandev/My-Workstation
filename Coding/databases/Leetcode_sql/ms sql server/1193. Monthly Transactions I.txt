-- Table create karna
CREATE TABLE Transactions_1193_Monthly_Transactions_I (
    id INT PRIMARY KEY,
    country VARCHAR(50) NOT NULL,
    state VARCHAR(10) NOT NULL CHECK (state IN ('approved', 'declined')),
    amount INT NOT NULL,
    trans_date DATE NOT NULL
);

-- Sample data insert karna
INSERT INTO Transactions_1193_Monthly_Transactions_I (id, country, state, amount, trans_date) VALUES
(121, 'US', 'approved', 1000, '2018-12-18'),
(122, 'US', 'declined', 2000, '2018-12-19'),
(123, 'US', 'approved', 2000, '2019-01-01'),
(124, 'DE', 'approved', 2000, '2019-01-07');

select * from Transactions_1193_Monthly_Transactions_I

SELECT 
    FORMAT(trans_date, 'yyyy-MM') AS month,
    country,
    COUNT(*) AS trans_count,
    SUM(CASE WHEN state = 'approved' THEN 1 ELSE 0 END) AS approved_count,
    SUM(amount) AS trans_total_amount,
    SUM(CASE WHEN state = 'approved' THEN amount ELSE 0 END) AS approved_total_amount
FROM Transactions_1193_Monthly_Transactions_I
GROUP BY FORMAT(trans_date, 'yyyy-MM'), country
ORDER BY month, country;
