# Write your MySQL query statement below

SELECT customer_id, count(Visits) AS count_no_trans
FROM (SELECT customer_id, v.visit_id as Visits
            FROM Visits AS v
            LEFT JOIN Transactions AS t ON t.visit_id = v.visit_id
            WHERE t.transaction_id IS NULL) AS just_visits
GROUP BY customer_id;