-- database dump from hbtn_0d_tvshows to your MySQL server
USE hbtn_0d_tvshows;

SELECT cities.id, cities.name, states.name
FROM states
RIGHT JOIN cities ON cities.state_id = states.id;