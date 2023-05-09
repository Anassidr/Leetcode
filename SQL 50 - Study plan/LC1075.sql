SELECT p.project_id, ROUND(SUM(e.experience_years)/COUNT(p.employee_id),2) average_years from project p 
inner join employee e on p.employee_id = e.employee_id
GROUP BY p.project_id 