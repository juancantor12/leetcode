--2356
select t.teacher_id, count(distinct subject_id) as cnt from Teacher t group by t.teacher_id