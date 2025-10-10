-- Create Users table
CREATE TABLE Users_1587_Bank_Account_Summary_II (
    account INT PRIMARY KEY,
    name VARCHAR(50)
);

-- Create Transactions table
CREATE TABLE Transactions_1587_Bank_Account_Summary_II (
    trans_id INT PRIMARY KEY,
    account INT,
    amount INT,
    transacted_on DATE,
    FOREIGN KEY (account) REFERENCES Users_1587_Bank_Account_Summary_II(account)
);


-- Insert data into Users
INSERT INTO Users_1587_Bank_Account_Summary_II(account, name) VALUES
(900001, 'Alice'),
(900002, 'Bob'),
(900003, 'Charlie');

-- Insert data into Transactions
INSERT INTO Transactions_1587_Bank_Account_Summary_II (trans_id, account, amount, transacted_on) VALUES
(1, 900001, 7000, '2020-08-01'),
(2, 900001, 7000, '2020-09-01'),
(3, 900001, -3000, '2020-09-02'),
(4, 900002, 1000, '2020-09-12'),
(5, 900003, 6000, '2020-08-07'),
(6, 900003, 6000, '2020-09-07'),
(7, 900003, -4000, '2020-09-11');


select * from Users_1587_Bank_Account_Summary_II
select * from Transactions_1587_Bank_Account_Summary_II

select name, sum(amount) as balance
from Users_1587_Bank_Account_Summary_II
join
Transactions_1587_Bank_Account_Summary_II
on
Users_1587_Bank_Account_Summary_II.account=Transactions_1587_Bank_Account_Summary_II.account

group by name
having sum(amount)>10000






