-- script that lists all cities contained in the database 
SELECT cities.id, cities.name, states.name
FROM states
RIGHT JOIN tv_shows ON cities.state_id = states.id;