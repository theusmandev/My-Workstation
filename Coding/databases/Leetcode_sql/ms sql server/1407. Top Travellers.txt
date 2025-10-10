 -- Create Users table

CREATE TABLE Users_1407_Top_Travellers (

    id INT PRIMARY KEY,

    name VARCHAR(50)

);



-- Insert sample data into Users

INSERT INTO Users_1407_Top_Travellers (id, name) VALUES

(1, 'Alice'),

(2, 'Bob'),

(3, 'Alex'),

(4, 'Donald'),

(7, 'Lee'),

(13, 'Jonathan'),

(19, 'Elvis');





-- Create Rides table

CREATE TABLE Rides_1407_Top_Travellers (

    id INT PRIMARY KEY,

    user_id INT,

    distance INT,

    FOREIGN KEY (user_id) REFERENCES Users_1407_Top_Travellers(id)

);



-- Insert sample data into Rides

INSERT INTO Rides_1407_Top_Travellers (id, user_id, distance) VALUES

(1, 1, 120),

(2, 2, 317),

(3, 3, 222),

(4, 7, 100),

(5, 13, 312),

(6, 19, 50),

(7, 7, 120),

(8, 19, 400),

(9, 7, 230);





select * from Users_1407_Top_Travellers

select * from Rides_1407_Top_Travellers







SELECT 

    U.name, 

    coalesce(SUM(R.distance),0) AS travelled_distance

FROM 

    Users_1407_Top_Travellers U

left JOIN 

    Rides_1407_Top_Travellers R 

    ON U.id = R.user_id

GROUP BY 

    U.name

ORDER BY 

    travelled_distance DESC;

