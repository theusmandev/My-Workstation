-- Department table create karna
CREATE TABLE Department_1179_Reformat_Department(
    id INT NOT NULL,
    revenue INT NOT NULL,
    month VARCHAR(3) NOT NULL,
    CONSTRAINT PK_Department PRIMARY KEY (id, month)
);

-- Sample data insert karna (example ke hisaab se)
INSERT INTO Department_1179_Reformat_Department(id, revenue, month) VALUES
(1, 8000, 'Jan'),
(2, 9000, 'Jan'),
(3, 10000, 'Feb'),
(1, 7000, 'Feb'),
(1, 6000, 'Mar');

select * from Department_1179_Reformat_Department



SELECT 
    id,
    [Jan] AS Jan_Revenue,
    [Feb] AS Feb_Revenue,
    [Mar] AS Mar_Revenue,
    [Apr] AS Apr_Revenue,
    [May] AS May_Revenue,
    [Jun] AS Jun_Revenue,
    [Jul] AS Jul_Revenue,
    [Aug] AS Aug_Revenue,
    [Sep] AS Sep_Revenue,
    [Oct] AS Oct_Revenue,
    [Nov] AS Nov_Revenue,
    [Dec] AS Dec_Revenue
FROM
(
    SELECT id, revenue, month
    FROM Department_1179_Reformat_Department
) AS SourceTable
PIVOT
(
    MAX(revenue) FOR month IN (
        [Jan],[Feb],[Mar],[Apr],[May],[Jun],
        [Jul],[Aug],[Sep],[Oct],[Nov],[Dec]
    )
) AS PivotTable
ORDER BY id;
