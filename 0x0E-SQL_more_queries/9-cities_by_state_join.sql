-- A script that lists all the cities that can be found in the database
SELECT cities.id, cities.name, states.name
FROM cities JOIN states ON cities.state_id = states.id;
