-- Salary table create karna
CREATE TABLE Salary_627_Swap_Salary (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    sex CHAR(1) CHECK (sex IN ('m','f')), -- ENUM ka SQL Server version
    salary INT
);

-- Sample data insert karna
INSERT INTO Salary_627_Swap_Salary(id, name, sex, salary) VALUES
(1, 'A', 'm', 2500),
(2, 'B', 'f', 1500),
(3, 'C', 'm', 5500),
(4, 'D', 'f', 500);


select * from Salary_627_Swap_Salary


UPDATE Salary_627_Swap_Salary
SET sex = CASE 
             WHEN sex = 'm' THEN 'f'
             ELSE 'm'
          END;
