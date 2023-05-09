# Write your MySQL query statement below

SELECT contest_id, ROUND(COUNT(DISTINCT user_id)/(SELECT COUNT(user_id) from users)*100,2) percentage from register r
GROUP BY contest_id 
ORDER BY percentage desc, contest_id asc
