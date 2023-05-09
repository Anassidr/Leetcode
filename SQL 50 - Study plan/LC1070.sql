SELECT s1.product_id, s1.year first_year, s1.quantity, s1.price from Sales s1
LEFT JOIN Sales s2 on s1.product_id = s2.product_id 
AND s2.year < s1.year
WHERE s2.price IS NULL 