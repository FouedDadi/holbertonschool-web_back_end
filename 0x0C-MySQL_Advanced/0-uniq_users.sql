-- create table users

CREATE TABLE IF not EXISTS (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    email varchar(255) NOT NULL UNIQUE,
    name varchar(255)
)