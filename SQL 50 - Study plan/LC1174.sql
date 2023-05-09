SELECT ROUND(COUNT(CASE WHEN d1.order_date = d1.customer_pref_delivery_date THEN 1 END) / COUNT(d1.customer_id) * 100, 2) AS immediate_percentage
FROM Delivery d1 
LEFT JOIN Delivery d2 ON d1.customer_id = d2.customer_id AND d2.order_date < d1.order_date
WHERE d2.delivery_id IS NULL;

-- By doing the Left Join, I take all rows from d1 and try to find a row in d2 where d2.order_date < d1.order_date
-- There is actually no row where this condition is satisfied, so the d2 columns will be NULL
-- Since these are particularly the rows of interest, we filter them out
