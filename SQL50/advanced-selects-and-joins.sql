--1731
select e.employee_id, e.name, count(e2.employee_id) as reports_count, round(avg(e2.age)) as average_age
from Employees e inner join Employees e2 on e.employee_id = e2.reports_to
group by e.employee_id, e.name
order by e.employee_id

--1789
select employee_id, department_id from Employee where primary_flag = "Y"
UNION
select employee_id, department_id from Employee group by employee_id having count(department_id) = 1

--610
SELECT x, y, z, IF( (x+y>z AND x+z > y AND y+z>x), "Yes", "No") as triangle from Triangle

--180
# Write your MySQL query statement below
select distinct current.num as ConsecutiveNums 
from Logs previous inner join Logs current on previous.id-1 = current.id inner join Logs next on current.id = next.id+1
where current.num = previous.num and current.num = next.num

--1164
select product_id, new_price as price from Products where (product_id,change_date) in (
    select product_id , max(change_date) as date from Products where change_date <='2019-08-16' group by product_id
    )
union
select distinct product_id, 10 as price from Products where product_id not in (
    select distinct product_id from Products where change_date <='2019-08-16'
)

--1204
select person_name from (
    select person_id, person_name, sum(weight) over (order by turn asc) as cumulative_weight from Queue
) xx where cumulative_weight <= 1000 order by cumulative_weight desc limit 1

--1907
select "Low Salary" as category, count(income) as accounts_count  from Accounts where income < 20000
union
select "Average Salary" as category, count(income) as accounts_count from Accounts where income >= 20000 and income <= 50000
union
select "High Salary" as category, count(income) as accounts_count  from Accounts where income > 50000