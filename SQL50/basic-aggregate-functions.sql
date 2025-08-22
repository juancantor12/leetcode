-- 620
SELECT * from Cinema where MOD(id, 2) <> 0 and description != "boring"
order by rating desc

-- 1251
select p.product_id, IFNULL(round(SUM(p.price * u.units)/sum(u.units), 2), 0) as average_price
from Prices p left join UnitsSold u on p.product_id = u.product_id AND (u.purchase_date between p.start_date and p.end_date)
group by p.product_id

--1633
select r.contest_id, ROUND(count(u.user_id)/(select count(user_id) from Users)*100, 2) as percentage
from  Users u right join Register r on u.user_id = r.user_id
group by r.contest_id
order by percentage desc, r.contest_id asc

--1211
select 
    q.query_name, 
    round((avg(q.rating/q.position)), 2) as quality, 
    round(sum(q.rating < 3)/count(q.rating)*100, 2) as poor_query_percentage 
from Queries q
group by q.query_name

--1193
select 
    DATE_FORMAT(trans_date,'%Y-%m') as month,
    country,
    count(id) as trans_count,
    sum(state = "approved") as approved_count,
    sum(amount) as trans_total_amount,
    sum( IF(state = "approved", amount, 0) ) as approved_total_amount
from Transactions
Group by month, country

--1174
select round(avg(order_date = customer_pref_delivery_date)*100, 2) as immediate_percentage
from Delivery
where (customer_id, order_date) in (
    SELECT customer_id, min(order_date)
    from Delivery
    group by customer_id
)

--550
select round(count(f.player_id)/count(distinct a.player_id), 2) as fraction
from Activity a 
left join ( 
    select player_id, min(event_date) as event_date from Activity group by player_id
) f on a.player_id = f.player_id and date_add(f.event_date, interval 1 day) = a.event_date