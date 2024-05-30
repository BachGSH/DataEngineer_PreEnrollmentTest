-- Calculate total good amount and Count number of Order which were delivered in Sep.2019

SELECT 
    SUM(Good_Amount) as total_good_amound,
    COUNT(*) as total_order_delivered
FROM 
    ORDER as o1
INNER JOIN 
    ORDER_DELIVER as o2
ON
    o1.Order_ID = o2.Order_ID
WHERE 
    EXTRACT(MONTH FROM o2.Date_Delivery) = 'Sep'
AND 
    EXTRACT(YEAR FROM o2.Date_Devliery) = 2019

