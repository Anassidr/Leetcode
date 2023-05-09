SELECT MAX(num) num FROM (
    SELECT num 
    FROM mynumbers
    GROUP BY num
    HAVING COUNT(num) = 1) m2