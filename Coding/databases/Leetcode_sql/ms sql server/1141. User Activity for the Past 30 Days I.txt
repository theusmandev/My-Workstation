-- Activity table
CREATE TABLE Activity_1141_User_Activity (
    user_id INT,
    session_id INT,
    activity_date DATE,
    activity_type VARCHAR(20) CHECK (activity_type IN ('open_session', 'end_session', 'scroll_down', 'send_message'))
);

-- Sample Data Insertion
INSERT INTO Activity_1141_User_Activity (user_id, session_id, activity_date, activity_type) VALUES
(1, 1, '2019-07-20', 'open_session'),
(1, 1, '2019-07-20', 'scroll_down'),
(1, 1, '2019-07-20', 'end_session'),
(2, 4, '2019-07-20', 'open_session'),
(2, 4, '2019-07-21', 'send_message'),
(2, 4, '2019-07-21', 'end_session'),
(3, 2, '2019-07-21', 'open_session'),
(3, 2, '2019-07-21', 'send_message'),
(3, 2, '2019-07-21', 'end_session'),
(4, 3, '2019-06-25', 'open_session'),
(4, 3, '2019-06-25', 'end_session');



select * from Activity_1141_User_Activity 

SELECT 
    activity_date AS day,
    COUNT(DISTINCT user_id) AS active_users
FROM Activity_1141_User_Activity
WHERE activity_date BETWEEN DATEADD(DAY, -29, '2019-07-27') AND '2019-07-27'
GROUP BY activity_date
ORDER BY activity_date;
