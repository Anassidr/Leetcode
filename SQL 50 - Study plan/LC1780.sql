SELECT employee_id, department_id 
FROM employee
GROUP BY employee_id
HAVING count(employee_id) = 1
UNION 
SELECT employee_id, department_id
FROM employee
WHERE primary_flag = 'Y'
ORDER BY employee_id


-- Other solution using Case when

SELECT employee_id, 
CASE WHEN COUNT(employee_id)=1 THEN department_id
WHEN COUNT(employee_id)>1 THEN MAX(CASE WHEN primary_flag = 'Y' THEN department_id ELSE -1 END)
END AS department_id
FROM Employee e
GROUP BY employee_id