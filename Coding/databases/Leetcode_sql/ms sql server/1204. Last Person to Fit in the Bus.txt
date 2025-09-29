-- Table create karna
CREATE TABLE Queue_1204_Last_Person_to_Fit_in_the_Bus (
    person_id INT PRIMARY KEY,
    person_name VARCHAR(100) NOT NULL,
    weight INT NOT NULL,
    turn INT NOT NULL UNIQUE
);

-- Sample data insert karna (example ke hisaab se)
INSERT INTO Queue_1204_Last_Person_to_Fit_in_the_Bus (person_id, person_name, weight, turn) VALUES
(5, 'Alice', 250, 1),
(3, 'Alex', 350, 2),
(6, 'John Cena', 400, 3),
(2, 'Marie', 200, 4),
(4, 'Bob', 175, 5),
(1, 'Winston', 500, 6);


select * from Queue_1204_Last_Person_to_Fit_in_the_Bus

WITH Cumulative AS (
    SELECT 
        person_name,
        turn,
        weight,
        SUM(weight) OVER (ORDER BY turn) AS cum_weight
    FROM Queue_1204_Last_Person_to_Fit_in_the_Bus
)
SELECT TOP 1 person_name
FROM Cumulative
WHERE cum_weight <= 1000
ORDER BY turn DESC;
