-- script that lists all cities contained in the database 
SELECT *
FROM states
JOIN cities ON states.id = cities.states_id 
ORDER BY cities.id ASC;