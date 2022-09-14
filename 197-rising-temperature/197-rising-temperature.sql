# Write your MySQL query statement below
Select b.id
FROM weather as w
JOIN weather as b on b.recordDate = (w.recordDate + interval 1 day)
WHERE b.temperature > w.temperature;