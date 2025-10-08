 CREATE TABLE Activities_1484_Group_Sold_Products_By_The_Date (

    sell_date DATE,

    product VARCHAR(50)

);







INSERT INTO Activities_1484_Group_Sold_Products_By_The_Date(sell_date, product)

VALUES

('2020-05-30', 'Headphone'),

('2020-06-01', 'Pencil'),

('2020-06-02', 'Mask'),

('2020-05-30', 'Basketball'),

('2020-06-01', 'Bible'),

('2020-06-02', 'Mask'),

('2020-05-30', 'T-Shirt');



select * from Activities_1484_Group_Sold_Products_By_The_Date









SELECT 

    sell_date,

    COUNT(DISTINCT product) AS num_sold,

    STRING_AGG(product, ',') WITHIN GROUP (ORDER BY product ASC) AS products

FROM (

    -- Remove duplicates just in case

    SELECT DISTINCT sell_date, product

    FROM Activities_1484_Group_Sold_Products_By_The_Date

) AS distinct_sales

GROUP BY sell_date

ORDER BY sell_date;











