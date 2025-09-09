--1978
select employee_id from Employees where salary < 30000 and manager_id not in (select employee_id from Employees)
order by employee_id

--626
select if((id = (select max(id) from Seat) and id % 2 = 1) , id, if(id % 2, id+1 , id-1 )) as id, student from Seat order by id

--1341
select q1.name as results from (
        select u.name, count(mr.movie_id) as c 
        from Users u inner join MovieRating mr on u.user_id = mr.user_id group by u.name 
        order by c desc, u.name asc limit 1
    ) as q1
union all
    select q2.title as results from (
        select mr.movie_id, m.title, avg(mr.rating) as avg_rating from MovieRating mr inner join Movies m on mr.movie_id = m.movie_id
        where mr.created_at between "2020-02-01" and "2020-02-28" group by mr.movie_id order by avg_rating desc, m.title asc limit 1
    ) as q2

--1321
SELECT DISTINCT
    visited_on,
    SUM(amount) OVER(ORDER BY visited_on RANGE BETWEEN INTERVAL 6 DAY PRECEDING AND CURRENT ROW) AS amount,
    ROUND(SUM(amount) OVER(ORDER BY visited_on RANGE BETWEEN INTERVAL 6 DAY PRECEDING AND CURRENT ROW) / 7, 2) AS average_amount
FROM
    Customer
LIMIT 1000000
OFFSET 6

--602
select id, count(id) num  from (
    select requester_id id from RequestAccepted
    union all
    select accepter_id id from RequestAccepted
) as _ group by id order by num desc limit 1

--585
SELECT ROUND(SUM(tiv_2016), 2) AS tiv_2016 FROM Insurance
WHERE tiv_2015 IN (
    SELECT tiv_2015
    FROM Insurance
    GROUP BY tiv_2015
    HAVING COUNT(*) > 1
)
AND (lat, lon) IN (
    SELECT lat, lon
    FROM Insurance
    GROUP BY lat, lon
    HAVING COUNT(*) = 1
)

--185
select d.name as Department, e.name as Employee, e.salary
from Employee e join Department d on e.departmentId = d.id
where(
        select COUNT(distinct salary)
        from Employee e2
        where e2.departmentId = e.departmentId and e2.salary >= e.salary
    ) <= 3