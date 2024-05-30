-- Count number of unique client order
SELECT 
    DISTINCT Client_ID,
    COUNT(*) as total_count
FROM 
    ORDER
GROUP BY 
    Client_ID

-- Count number of orders by order month
SELECT 
    EXTRACT(MONTH FROM Date_Order) as month,
    COUNT(*) as total_count
FROM 
    ORDER  
GROUP BY 
    month
ORDER BY 
    month