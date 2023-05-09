SELECT query_name,
ROUND(AVG(rating/position),2) quality,
ROUND(COUNT((CASE WHEN rating < 3 THEN 1 END))/COUNT(rating)*100,2) poor_query_percentage from queries
GROUP BY query_name 