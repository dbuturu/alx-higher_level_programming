-- Select score and name where name is true
SELECT `score`, `name`
	FROM second_table
	WHERE name <> ''
	ORDER BY `score` DESC;
