SELECT p.product_id, ROUND(SUM(p.price*u.units)/SUM(u.units),2) average_price from prices p 
inner join unitssold u on p.product_id = u.product_id
and (u.purchase_date between p.start_date and p.end_date)
GROUP BY u.product_id 