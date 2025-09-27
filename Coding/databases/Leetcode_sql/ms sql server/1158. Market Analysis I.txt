-- Users Table
CREATE TABLE Users_1158_Market_Analysis_I (
    user_id INT PRIMARY KEY,
    join_date DATE,
    favorite_brand VARCHAR(50)
);

-- Orders Table
CREATE TABLE Orders_1158_Market_Analysis_I (
    order_id INT PRIMARY KEY,
    order_date DATE,
    item_id INT,
    buyer_id INT,
    seller_id INT,
    FOREIGN KEY (buyer_id) REFERENCES Users_1158_Market_Analysis_I(user_id),
    FOREIGN KEY (seller_id) REFERENCES Users_1158_Market_Analysis_I(user_id)
);

-- Items Table
CREATE TABLE Items_1158_Market_Analysis_I (
    item_id INT PRIMARY KEY,
    item_brand VARCHAR(50)
);



-- Insert Users
INSERT INTO Users_1158_Market_Analysis_I (user_id, join_date, favorite_brand) VALUES
(1, '2018-01-01', 'Lenovo'),
(2, '2018-02-09', 'Samsung'),
(3, '2018-01-19', 'LG'),
(4, '2018-05-21', 'HP');

-- Insert Orders
INSERT INTO Orders_1158_Market_Analysis_I (order_id, order_date, item_id, buyer_id, seller_id) VALUES
(1, '2019-08-01', 4, 1, 2),
(2, '2018-08-02', 2, 1, 3),
(3, '2019-08-03', 3, 2, 3),
(4, '2018-08-04', 1, 4, 2),
(5, '2018-08-04', 1, 3, 4),
(6, '2019-08-05', 2, 2, 4);

-- Insert Items
INSERT INTO Items_1158_Market_Analysis_I (item_id, item_brand) VALUES
(1, 'Samsung'),
(2, 'Lenovo'),
(3, 'LG'),
(4, 'HP');





select * from Users_1158_Market_Analysis_I
select * from Orders_1158_Market_Analysis_I
select * from Items_1158_Market_Analysis_I




SELECT 
    u.user_id AS buyer_id,
    u.join_date,
    COUNT(o.order_id) AS orders_in_2019
FROM Users_1158_Market_Analysis_I u
LEFT JOIN Orders_1158_Market_Analysis_I o
    ON u.user_id = o.buyer_id
   AND YEAR(o.order_date) = 2019
GROUP BY u.user_id, u.join_date
ORDER BY u.user_id;
