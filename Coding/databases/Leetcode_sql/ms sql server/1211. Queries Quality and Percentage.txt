-- Table create karna
CREATE TABLE Queries_1211_Queries_Quality (
    query_name VARCHAR(50) NOT NULL,
    result VARCHAR(100) NOT NULL,
    position INT NOT NULL CHECK (position BETWEEN 1 AND 500),
    rating INT NOT NULL CHECK (rating BETWEEN 1 AND 5)
);

-- Sample data insert karna (example ke hisaab se)
INSERT INTO Queries_1211_Queries_Quality (query_name, result, position, rating) VALUES
('Dog', 'Golden Retriever', 1, 5),
('Dog', 'German Shepherd', 2, 5),
('Dog', 'Mule', 200, 1),
('Cat', 'Shirazi', 5, 2),
('Cat', 'Siamese', 3, 3),
('Cat', 'Sphynx', 7, 4);


select * from Queries_1211_Queries_Quality

SELECT 
    query_name,
    CAST(AVG(1.0 * rating / position) AS DECIMAL(5,2)) AS quality,
    CAST(100.0 * SUM(CASE WHEN rating < 3 THEN 1 ELSE 0 END) / COUNT(*) AS DECIMAL(5,2)) AS poor_query_percentage
FROM Queries_1211_Queries_Quality
GROUP BY query_name;

