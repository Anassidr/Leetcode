SELECT s.user_id, 
COUNT(CASE WHEN c.action = 'confirmed' THEN 1 END)/COUNT(c.action) as confirmation_rate
FROM signups s 
LEFT JOIN confirmations c ON s.user_id = c.user_id
GROUP BY s.user_id