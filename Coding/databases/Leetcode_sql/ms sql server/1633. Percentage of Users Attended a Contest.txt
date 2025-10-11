-- Create Users table
CREATE TABLE Users_1633_Percentage_of_Users_Attended_a_Contest (
    user_id INT PRIMARY KEY,
    user_name VARCHAR(50)
);

-- Create Register table
CREATE TABLE Register_1633_Percentage_of_Users_Attended_a_Contest (
    contest_id INT,
    user_id INT,
    PRIMARY KEY (contest_id, user_id),
    FOREIGN KEY (user_id) REFERENCES Users_1633_Percentage_of_Users_Attended_a_Contest(user_id)
);


-- Insert data into Users table
INSERT INTO Users_1633_Percentage_of_Users_Attended_a_Contest (user_id, user_name) VALUES
(6, 'Alice'),
(2, 'Bob'),
(7, 'Alex');

-- Insert data into Register table
INSERT INTO Register_1633_Percentage_of_Users_Attended_a_Contest (contest_id, user_id) VALUES
(215, 6),
(209, 2),
(208, 2),
(210, 6),
(208, 6),
(209, 7),
(209, 6),
(215, 7),
(208, 7),
(210, 2),
(207, 2),
(210, 7);


select * from Register_1633_Percentage_of_Users_Attended_a_Contest
select * from Users_1633_Percentage_of_Users_Attended_a_Contest



select contest_id, round(count(distinct user_id)*100/(SELECT count(user_name) from Users_1633_Percentage_of_Users_Attended_a_Contest),2) as percentage
from Register_1633_Percentage_of_Users_Attended_a_Contest

group by contest_id
order by percentage desc , contest_id asc
