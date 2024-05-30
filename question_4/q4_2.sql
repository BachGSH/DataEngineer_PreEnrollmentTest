-- List of client who have more than 10 orders in this year

SELECT 
    DISTINCT Client_ID,
    COUNT(*) as total_count
FROM 
    ORDER
GROUP BY 
    Client_ID
HAVING 
    COUNT(*) > 10


