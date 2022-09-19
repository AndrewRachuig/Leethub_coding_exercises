# Write your MySQL query statement below

SELECT u.user_id as buyer_id, u.join_date, COUNT(o.order_id) as orders_in_2019
FROM Users as u
LEFT JOIN Orders as o
ON o.buyer_id = u.user_id AND O.order_date LIKE("2019%")
GROUP BY u.user_id;


# Alternative using YEAR instead of LIKE

# SELECT U.user_id as buyer_id, U.join_date,COUNT(O.order_id) as orders_in_2019
# FROM Users as U
# LEFT OUTER JOIN Orders as O
# ON O.buyer_id = U.user_id AND year(O.order_date) = 2019
# GROUP BY U.user_id,U.join_date;