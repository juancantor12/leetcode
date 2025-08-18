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