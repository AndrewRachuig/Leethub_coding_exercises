# Write your MySQL query statement below
UPDATE Salary
set sex =
    CASE sex
        WHEN "m" THEN "f"
        ELSE "m"
    END;