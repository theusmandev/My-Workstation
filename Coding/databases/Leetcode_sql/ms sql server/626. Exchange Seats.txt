 -- Problem table create karna

CREATE TABLE Seat_626_Exchange_Seats (

    id INT PRIMARY KEY,

    student VARCHAR(50)

);



-- Sample data insert karna

INSERT INTO Seat_626_Exchange_Seats (id, student) VALUES

(1, 'Abbot'),

(2, 'Doris'),

(3, 'Emerson'),

(4, 'Green'),

(5, 'Jeames');





select * from Seat_626_Exchange_Seats









SELECT 

    CASE 

        -- Agar last odd id hai to wahi rahe

        WHEN id % 2 = 1 AND id = (SELECT MAX(id) FROM Seat_626_Exchange_Seats

) THEN id

        -- Agar odd id hai to next id se swap

        WHEN id % 2 = 1 THEN id + 1

        -- Agar even id hai to previous id se swap

        ELSE id - 1

    END AS id,

    student

FROM Seat_626_Exchange_Seats



ORDER BY id;



