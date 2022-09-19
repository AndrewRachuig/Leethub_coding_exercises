# Write your MySQL query statement below
SELECT user_id, Max(time_stamp) AS last_stamp
FROM Logins
WHERE time_stamp BETWEEN DATE("2020-01-01") AND DATE("2021-01-01")
GROUP BY user_id;