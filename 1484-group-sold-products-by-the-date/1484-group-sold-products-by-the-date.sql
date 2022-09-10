# Write your MySQL query statement below
SELECT sell_date, count(DISTINCT product) as num_sold, group_concat(distinct product) AS products
FROM Activities
GROUP BY sell_date;