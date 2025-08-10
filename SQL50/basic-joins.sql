-- 1378
select eu.unique_id, e.name from EmployeeUNI as eu RIGHT JOIN Employees as e on e.id = eu.id

1068
select p.product_name, s.year, s.price from Product as p inner join Sales as s on p.product_id = s.product_id

1581
select v.customer_id, count(v.visit_id) as count_no_trans from Visits as v left join Transactions as t on v.visit_id = t.visit_id
where t.transaction_id is null
group by v.customer_id

197
SELECT today.id
from Weather as yesterday 
cross join Weather as today 
where DATEDIFF(today.recordDate, yesterday.recordDate) = 1 and today.temperature > yesterday.temperature

1661
select 
    start.machine_id, round(avg(end.timestamp - start.timestamp), 3) as processing_time
from 
    (select a.machine_id, a.process_id, a.timestamp from Activity a where activity_type = "start") as start
inner join (select a.machine_id, a.process_id, a.timestamp from Activity a where activity_type = "end") as end on
    start.machine_id = end.machine_id and start.process_id = end.process_id
group by start.machine_id