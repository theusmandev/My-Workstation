CREATE TABLE Users_1517_Find_Users_With_Valid_E_Mails (
    user_id INT PRIMARY KEY,
    name VARCHAR(100),
    mail VARCHAR(100)
);

INSERT INTO Users_1517_Find_Users_With_Valid_E_Mails (user_id, name, mail)
VALUES
(1, 'Winston', 'winston@leetcode.com'),
(2, 'Jonathan', 'jonathanisgreat'),
(3, 'Annabelle', 'bella-@leetcode.com'),
(4, 'Sally', 'sally.come@leetcode.com'),
(5, 'Marwan', 'quarz#2020@leetcode.com'),
(6, 'David', 'david69@gmail.com'),
(7, 'Shapiro', '.shapo@leetcode.com');


select * from Users_1517_Find_Users_With_Valid_E_Mails

SELECT
    user_id,
    name,
    mail
FROM Users_1517_Find_Users_With_Valid_E_Mails
WHERE RIGHT(mail, 13) COLLATE Latin1_General_CS_AS = '@leetcode.com'
    AND mail LIKE '[a-zA-Z]%'
    AND LEFT(mail, LEN(mail)-13) NOT LIKE '%[^0-9a-zA-Z_\.\-]%'

