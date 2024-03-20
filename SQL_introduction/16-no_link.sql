-- Script to list all records of the table second_table with names, ordered by descending score
SELECT score, name FROM hbtn_0c_0.second_table WHERE name IS NOT NULL ORDER BY score DESC;
