-- 1378
select eu.unique_id, e.name from EmployeeUNI as eu RIGHT JOIN Employees as e on e.id = eu.id

-- 1068
select p.product_name, s.year, s.price from Product as p inner join Sales as s on p.product_id = s.product_id

-- 1581
select v.customer_id, count(v.visit_id) as count_no_trans from Visits as v left join Transactions as t on v.visit_id = t.visit_id
where t.transaction_id is null
group by v.customer_id

-- 197
SELECT today.id
from Weather as yesterday 
cross join Weather as today 
where DATEDIFF(today.recordDate, yesterday.recordDate) = 1 and today.temperature > yesterday.temperature

-- 1661
select 
    start.machine_id, round(avg(end.timestamp - start.timestamp), 3) as processing_time
from 
    (select a.machine_id, a.process_id, a.timestamp from Activity a where activity_type = "start") as start
inner join (select a.machine_id, a.process_id, a.timestamp from Activity a where activity_type = "end") as end on
    start.machine_id = end.machine_id and start.process_id = end.process_id
group by start.machine_id

-- 577
select e.name, b.bonus from Employee e left join Bonus b on e.empId = b.empId where b.bonus < 1000 or b.bonus is null

-- 1280
select st.student_id, st.student_name, su.subject_name, count(ex.student_id) as attended_exams
from Students st join Subjects su left join Examinations ex on ex.student_id = st.student_id and su.subject_name = ex.subject_name
group by st.student_id, st.student_name, su.subject_name
order by st.student_id asc, su.subject_name asc

--570
select e2.name from Employee e inner join Employee e2 on e.managerId = e2.id
group by e2.id, e2.name
having count(e2.id) >= 5

--1934
select b.user_id, IFNULL(ROUND(a.confirmed/b.total, 2), 0) as confirmation_rate
from (
    select s.user_id, count(c.action) as confirmed from Signups s left join Confirmations c on s.user_id = c.user_id where c.action = "confirmed" group by s.user_id
) a right join (
    select s.user_id, count(c.action) as total from Signups s left join Confirmations c on s.user_id = c.user_id group by s.user_id
) b on a.user_id = b.user_id
