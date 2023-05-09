SELECT activity_date day, COUNT(DISTINCT user_id) active_users
FROM activity a 
WHERE activity_date BETWEEN DATE_ADD('2019-07-27', INTERVAL -29 DAY) AND DATE('2019-07-27')
GROUP BY activity_date