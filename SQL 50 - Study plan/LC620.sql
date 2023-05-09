SELECT * from cinema
WHERE description <> 'boring'
HAVING MOD(id,2)=1 
ORDER BY rating desc

