SELECT *,
CASE WHEN abs(x)+abs(y) > abs(z) AND abs(x)+abs(z) > abs(y) AND abs(y)+abs(z) > abs(x) THEN 'Yes'
WHEN abs(x)+abs(y) <= abs(z) OR abs(x)+abs(z) <= abs(y) OR abs(y)+abs(z) <= abs(x) THEN 'No'
END triangle
FROM Triangle


-- More concise

SELECT *, IF(x+y>z and x+z>y and y+z>x, 'Yes', 'No') as triangle FROM triangle