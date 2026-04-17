-- Lists all records of second_table where name is not NULL, ordered by score DESC
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
