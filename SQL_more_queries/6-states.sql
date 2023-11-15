-- script 6
--  that creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) 
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states(
    id INT NOT NULL UNIQUE,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY(id)
);