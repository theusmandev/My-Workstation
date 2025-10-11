-- Create Users table
CREATE TABLE Users_1667_FixNames (
    user_id INT PRIMARY KEY,
    name VARCHAR(100)
);

-- Insert sample data
INSERT INTO Users_1667_FixNames (user_id, name) VALUES
(1, 'aLice'),
(2, 'bOB'),
(3, 'joHN'),
(4, 'MARy'),
(5, 'aLEX');

select * from Users_1667_FixNames

select user_id, upper(left(name,1))+lower(substring(name,2,len(name)-1)) as name
from Users_1667_FixNames
order by user_id 



