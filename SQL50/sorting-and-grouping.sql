--2356
select t.teacher_id, count(distinct subject_id) as cnt from Teacher t group by t.teacher_id

--1141
select a.activity_date as day, count(DISTINCT a.user_id) as active_users 
from Activity a where a.activity_date between "2019-06-28" AND "2019-07-27"
GROUP BY a.activity_date

--1070
SELECT 
    product_id,
    year AS first_year,
    quantity,
    price
FROM Sales
WHERE(product_id,year) IN (
    SELECT product_id, MIN(year) AS first_year
    FROM Sales
    GROUP BY product_id
)

--596
select class from Courses group by class having count(student) >= 5

--1729
select f.user_id, count(f.follower_id) as followers_count from Followers f group by f.user_id order by f.user_id asc

--619
select (select num from MyNumbers group by num having count(num) = 1 order by num desc limit 1) as num from dual