-- 1757
SELECT product_id from Products where low_fats = "Y" and recyclable = "Y";

-- 584
select name from Customer where referee_id != 2 or referee_id is NULL

-- 595
SELECT w.name, w.population, w.area from world as w where w.area >= 3000000 or w.population >= 25000000

-- 1148
select distinct author_id as id from Views where author_id = viewer_id order by id ASC

-- 1683
select tweet_id from Tweets where LENGTH(content) > 15