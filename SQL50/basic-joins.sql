-- 1378
select eu.unique_id, e.name from EmployeeUNI as eu RIGHT JOIN Employees as e on e.id = eu.id