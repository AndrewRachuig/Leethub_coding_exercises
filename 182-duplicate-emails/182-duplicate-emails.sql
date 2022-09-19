SELECT email
FROM (SELECT email, count(id) as total
        FROM Person
        GROUP BY email) as first
WHERE total > 1;


# Alternate form using HAVING
# select Email
# from Person
# group by Email
# having count(Email)>1 