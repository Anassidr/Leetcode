SELECT e1.employee_id,
e1.name, 
COUNT(e2.employee_id) reports_count, 
ROUND(AVG(e2.age)) average_age
FROM employees e1
CROSS JOIN employees e2
ON e2.reports_to = e1.employee_id 
GROUP BY e1.employee_id
ORDER BY e1.employee_id