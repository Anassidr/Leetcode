select distinct product_id, 10 as price
from Products
group by product_id
having (min(change_date) > "2019-08-16")

union

select p2.product_id, new_price
from Products p2
where (p2.product_id, p2.change_date) in

(
select product_id, max(change_date) as recent_date
from Products
where change_date <= "2019-08-16"
group by product_id
)

-- other solution : 

SELECT distinct a.product_id, ifnull(temp.new_price,10) as price 
FROM products as a
LEFT JOIN
(SELECT * 
FROM products 
WHERE (product_id, change_date) in 
(select product_id,max(change_date) from products where change_date<="2019-08-16" group by product_id)
) as temp
on a.product_id = temp.product_id;

-- other solution using window functions :

WITH b as (
    SELECT distinct product_id
    FROM Products
), t as (
    SELECT *,
    ROW_NUMBER() OVER(PARTITION BY product_id ORDER BY change_date DESC) rn
    FROM Products
    WHERE change_date <= '2019-08-16'
)

SELECT b.product_id, ifnull(t.new_price, 10) as price
FROM b left join t 
on b.product_id = t.product_id and t.rn = 1