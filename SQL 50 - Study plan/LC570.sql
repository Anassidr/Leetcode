SELECT e1.name from employee e1
inner join employee e2 on e1.id = e2.managerId
GROUP BY e2.managerId
HAVING COUNT(e2.managerId) > 4 

