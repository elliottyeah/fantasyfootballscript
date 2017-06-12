DROP DATABASE IF EXISTS `fantasy.db.mysql`;
CREATE DATABASE `fantasy.db.mysql`
    DEFAULT CHARACTER SET utf8
    DEFAULT COLLATE utf8_general_ci;

USE 'mysql';
GRANT ALL PRIVILEGES ON mydb.* TO 'elliott1'@'localhost' IDENTIFIED BY 'elliott1'

WITH GRANT OPTION;
FLUSH PRIVILEGES;