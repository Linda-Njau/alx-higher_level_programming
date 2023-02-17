-- list all the cities of cali in the database
SELECT `id`, `name`
FROM `cities`
WHERE `state_id` = 1
ORDER BY `id`;
