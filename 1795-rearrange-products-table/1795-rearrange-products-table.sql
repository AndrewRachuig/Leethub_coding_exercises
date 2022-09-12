# Write your MySQL query statement below
SELECT *
FROM
    (SELECT product_id, "store1" AS store, store1 as price
        FROM Products

    UNION

    SELECT product_id, "store2" AS store, store2 as price
        FROM Products

    UNION

    SELECT product_id, "store3" AS store, store3 as price
        FROM Products) AS compiled
    
WHERE price IS NOT NULL;