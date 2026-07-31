-- Write your query below
select name from customers c where NOT EXISTS (select 1 from orders o where o.customer_id = c.id)