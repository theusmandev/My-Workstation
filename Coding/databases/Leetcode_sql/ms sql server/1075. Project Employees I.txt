-- Project table
CREATE TABLE Project_1075_Project_Employees (
    project_id INT NOT NULL,
    employee_id INT NOT NULL,
    PRIMARY KEY (project_id, employee_id)
);

-- Employee table
CREATE TABLE Employee_1075_Project_Employees (
    employee_id INT PRIMARY KEY,
    name VARCHAR(50),
    experience_years INT NOT NULL
);

-- Sample data for Project table
INSERT INTO Project_1075_Project_Employees (project_id, employee_id) VALUES
(1, 1),
(1, 2),
(1, 3),
(2, 1),
(2, 4);

-- Sample data for Employee table
INSERT INTO Employee_1075_Project_Employees (employee_id, name, experience_years) VALUES
(1, 'Khaled', 3),
(2, 'Ali', 2),
(3, 'John', 1)



select * from Project_1075_Project_Employees
select * from Employee_1075_Project_Employees




SELECT 
    p.project_id,
    ROUND(AVG(CAST(e.experience_years AS DECIMAL(10,2))), 2) AS average_years
FROM Project_1075_Project_Employees AS p
JOIN Employee_1075_Project_Employees AS e
    ON p.employee_id = e.employee_id
GROUP BY p.project_id;
