SELECT email
FROM (SELECT email, count(id) as total
        FROM Person
        GROUP BY email) as first
WHERE total > 1;