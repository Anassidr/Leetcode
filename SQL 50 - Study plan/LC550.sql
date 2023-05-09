SELECT ROUND(
    COUNT(DISTINCT a1.player_id)/(
    SELECT COUNT(DISTINCT player_id) FROM Activity
),2) fraction FROM (
  SELECT player_id, MIN(event_date) AS first_event_date
  FROM Activity
  GROUP BY player_id
) AS a1
INNER JOIN Activity a2 ON a2.player_id = a1.player_id 
AND DATEDIFF(a2.event_date, a1.first_event_date) = 1