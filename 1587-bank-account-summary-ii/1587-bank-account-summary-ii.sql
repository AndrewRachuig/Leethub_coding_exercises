# Write your MySQL query statement below
SELECT name, sum(t.amount) AS balance
FROM Users
JOIN Transactions AS t ON t.account = users.account
GROUP BY t.account
HAVING balance > 10000;