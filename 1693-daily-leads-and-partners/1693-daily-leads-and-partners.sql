# Write your MySQL query statement below
SELECT date_id, make_name, count(Distinct lead_id) as unique_leads, count(Distinct partner_id) as unique_partners
FROM DailySales
GROUP BY date_id, make_name
ORDER BY date_id ASC