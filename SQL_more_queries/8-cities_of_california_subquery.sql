-- lists all the cities of California 
-- that can be found in the database hbtn_0d_usa
USE hbtn_0d_usa;

SELECT *
FROM states, cities
WHERE states.name = 'California' AND cities.state_id = states.id
ORDER BY cities.id ASC; 
