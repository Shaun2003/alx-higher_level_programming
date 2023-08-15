-- list number of records with same score in second_table of database hbtn_0c_0 in MySQL server
SELECT score, COUNT(score) AS number FROM second_table GROUP BY score ORDER BY score DESC;
