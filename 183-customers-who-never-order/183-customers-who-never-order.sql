# Write your MySQL query statement below
SELECT name AS customers
FROM Customers
LEFT JOIN Orders ON orders.customerID = customers.id
WHERE orders.id IS NULL;