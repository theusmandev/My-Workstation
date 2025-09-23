-- Table create
CREATE TABLE ActorDirector_1050_Actors_and_Directors (
    actor_id INT,
    director_id INT,
    timestamp INT PRIMARY KEY
);

-- Sample data insert
INSERT INTO ActorDirector_1050_Actors_and_Directors (actor_id, director_id, timestamp) VALUES
(1, 1, 0),
(1, 1, 1),
(1, 1, 2),
(1, 2, 3),
(1, 2, 4),
(2, 1, 5),
(2, 1, 6);


select * from ActorDirector_1050_Actors_and_Directors

SELECT actor_id, director_id
FROM ActorDirector_1050_Actors_and_Directors
GROUP BY actor_id, director_id
HAVING COUNT(*) >= 3;









