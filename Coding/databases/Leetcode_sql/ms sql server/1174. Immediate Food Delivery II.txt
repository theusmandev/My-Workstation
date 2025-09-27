-- Table create karne ka code
CREATE TABLE Delivery_1174_Immediate_Food_Delivery_II (
    delivery_id INT PRIMARY KEY,
    customer_id INT NOT NULL,
    order_date DATE NOT NULL,
    customer_pref_delivery_date DATE NOT NULL
);

-- Sample data insert karne ka code (jo aapke example mein diya hai)
INSERT INTO Delivery_1174_Immediate_Food_Delivery_II (delivery_id, customer_id, order_date, customer_pref_delivery_date)
VALUES
(1, 1, '2019-08-01', '2019-08-02'),
(2, 2, '2019-08-02', '2019-08-02'),
(3, 1, '2019-08-11', '2019-08-12'),
(4, 3, '2019-08-24', '2019-08-24'),
(5, 3, '2019-08-21', '2019-08-22'),
(6, 2, '2019-08-11', '2019-08-13'),
(7, 4, '2019-08-09', '2019-08-09');


select * from Delivery_1174_Immediate_Food_Delivery_II



SELECT 
    delivery_id,
    CASE 
        WHEN order_date = (customer_pref_delivery_date) THEN 'immediate'
        ELSE 'scheduled'
    END AS order_status
FROM Delivery_1174_Immediate_Food_Delivery_II;



WITH FirstOrders AS (
    SELECT d.*
    FROM Delivery_1174_Immediate_Food_Delivery_II d
    WHERE d.order_date = (
        SELECT MIN(order_date)
        FROM Delivery_1174_Immediate_Food_Delivery_II
        WHERE customer_id = d.customer_id
    )
)
SELECT 
    CAST(
        100.0 * SUM(CASE WHEN order_date = customer_pref_delivery_date THEN 1 ELSE 0 END) 
        / COUNT(*) 
    AS DECIMAL(5,2)) AS immediate_percentage
FROM FirstOrders;

