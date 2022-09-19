# Write your MySQL query statement below
SELECT p.product_id, p.product_name
FROM Product as p
JOIN Sales as s ON s.product_id = p.product_id
group by p.product_id
having min(s.sale_date) >= '2019-01-01' AND max(s.sale_date) <= '2019-03-31'