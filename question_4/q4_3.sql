-- From the above list of client: get information of first and second last order of client (Order date, good type, and amount)
WITH cte AS  (
    SELECT 
        DISTINCT Client_ID,
        COUNT(*) as total_count
    FROM 
        ORDER
    GROUP BY 
        Client_ID
    HAVING 
        OUNT(*) > 10
)

WITH RankedOrders AS (
    SELECT
        *,
        ROW_NUMBER() OVER (PARTITION BY Client_id ORDER BY Date_Order ASC) AS order_rank_asc,
        ROW_NUMBER() OVER (PARTITION BY Client_id ORDER BY Date_Order DESC) AS order_rank_desc
    FROM
        ORDER
)

SELECT 
    r.Client_ID,
    Date_Order,
    Good_Type,
    Good_Amount
FROM 
    RankedOrders as r
INNER JOIN 
    cte
ON 
    r.Client_ID = cte.Client_ID
WHERE 
    order_rank_asc = 1

UNION

SELECT 
    r.Client_ID,
    Date_Order,
    Good_Type,
    Good_Amount
FROM 
    RankedOrders as r
INNER JOIN 
    cte
ON 
    r.Client_ID = cte.Client_ID
WHERE 
    order_rank_desc = 2
