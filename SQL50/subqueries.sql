--1978
select employee_id from Employees where salary < 30000 and manager_id not in (select employee_id from Employees)
order by employee_id

--626
select if((id = (select max(id) from Seat) and id % 2 = 1) , id, if(id % 2, id+1 , id-1 )) as id, student from Seat order by id