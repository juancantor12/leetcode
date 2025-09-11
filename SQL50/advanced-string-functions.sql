--1667
select u.user_id, concat(
    upper(left(u.name, 1)), 
    lower(substring(u.name, 2))
) as name from Users u order by u.user_id

--1527
select patient_id, patient_name, conditions from Patients 
where conditions like "% DIAB1%" or conditions like "DIAB1%" or conditions like "% DIAB1%"